from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Product, Category
from modeltranslation.admin import TabbedTranslationAdmin


class ProductAdmin(TabbedTranslationAdmin):
    list_display = ['name', 'slug', 'status', 'price', 'image']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(DraggableMPTTAdmin, TabbedTranslationAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
