from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Category


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'keywords', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'keywords', 'description')


translator.register(Product, ProductTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
