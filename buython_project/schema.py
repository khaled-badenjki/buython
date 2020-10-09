import graphene
import catalog_graphql.schema


class Query(catalog_graphql.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
