import graphene
import graphql_jwt
import links.schema
import investor.schema
import account.schema
import users.schema
import businessowner.schema

class Query(businessowner.schema.Query, account.schema.Query, investor.schema.Query,users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

class Mutation(businessowner.schema.Mutation, account.schema.Mutation , investor.schema.Mutation, users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    pass

schema = graphene.Schema(query=Query, mutation=Mutation)