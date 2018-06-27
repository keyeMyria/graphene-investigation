import graphene

import grapheen.schema
# import grapheen.schema_relay # schema using relay


# NOTE: EITHER INCLUDE grapheen.schema.Query OR grapheen.schema_relay.RelayQuery.
# DON"T INCLUDE BOTH
class Query(
    grapheen.schema.Query,
    # grapheen.schema_relay.RelayQuery,
    graphene.ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


# NOTE: EITHER INCLUDE grapheen.schema.Mutation OR grapheen.schema_relay.RelayMutation.
# DON"T INCLUDE BOTH
class Mutation(
    grapheen.schema.Mutation,
    # grapheen.schema_relay.RelayMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
