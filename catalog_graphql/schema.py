import graphene
from graphene_django import DjangoObjectType
from catalog.models import Product as ProductModel


class Product(DjangoObjectType):
    class Meta:
        model = ProductModel


class Query(graphene.ObjectType):
    products = graphene.List(Product)

    @graphene.resolve_only_args
    def resolve_products(self):
        return ProductModel.objects.all()
