from django.contrib import admin
from .models import Slides, Category, Product, Cart
from django.contrib import messages


@admin.action(description="deactivate selected products")
def deactivate_products(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="activate selected products")
def activate_products(self, request, queryset):
    queryset.update(is_active=True)
    self.message_user(
        request,
        "selected products were marked as active",
        messages.SUCCESS,
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "mrp_price", "discount_price", "is_active"]
    actions = [deactivate_products, activate_products]


# Register your models here.
admin.site.register(Slides)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
