import graphene

# import grapheen.schema
import grapheen.schema_relay # schema using relay


class Query(
    # grapheen.schema.Query,
    grapheen.schema_relay.RelayQuery,
    graphene.ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
    # grapheen.schema.Mutation,
    grapheen.schema_relay.RelayMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
