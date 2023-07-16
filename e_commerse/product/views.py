from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
# from .forms import CheckoutForm, CouponForm, RefundForm
from .models import Product, Category, User
from .models import Product, Category, Cart
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth

from user.models import Profile
# Create your views here.
import random

# Create your views here.


class ShopView(LoginRequiredMixin, ListView):
    login_url = '/user/signin/'
    # redirect_field_name = ''
    model = Product
    paginate_by = 6
    template_name = "shop.html"

    def get(self, request):
        products_list = Product.objects.all()
        count_products = products_list.distinct().count()
        # count_products = Cart.objects.filter(user=request.user).distinct().count()
        context = {
            "object_list": products_list,
            "no_of_products_in_cart": count_products,
        }
        return render(request, self.template_name, context)


class ItemDetailView(LoginRequiredMixin, DetailView):
    login_url = '/user/signin/'
    model = Product
    template_name = "product-detail.html"

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(ItemDetailView, self).get_context_data(*args, **kwargs)
        # add extra field
        count_products = Product.objects.all().distinct().count()
        context["no_of_products_in_cart"] = count_products
        return context


class HomeView(ListView):
    template_name = "index.html"
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'items'


class CategoryView(View):
    def get(self, *args, **kwargs):
        category = Category.objects.get(slug=self.kwargs['slug'])
        item = Product.objects.filter(category=category, is_active=True)
        context = {
            'object_list': item,
            'category_title': category,
            # 'category_description': category.description,
            # 'category_image': category.image
        }
        return render(self.request, "category.html", context)

class CartView(View):
    def get(self, request):
        # profile = request.session.get('Profile')
        print(request.user.id)
        profile = "92f0b649-8700-4da1-a598-b8c46bdc1d8e"
        add_to_cart = Cart.get_cart_details(profile)
        print(add_to_cart)
        return render(request, 'cart.html', {'addttocart': add_to_cart})