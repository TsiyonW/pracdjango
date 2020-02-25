import graphene
from graphene_django import DjangoObjectType
from businessowner.models import  Businessowner
from account.models import Account
from account.schema import AccountType
class BusinessownerType(DjangoObjectType):
    class Meta:
        model =  Businessowner


class Query(graphene.ObjectType):
    businessowner = graphene.List( BusinessownerType )

    def resolve_businessowner(self, info, **kwargs):
        return  Businessowner.objects.all()

#1
class CreateBusinessowner(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)
    # last_name = graphene.String(required=True)
    first_name = graphene.String(required=True)
    # phoneNo = graphene.String(required=True)
    sex =graphene.String(required=True) 
    # subcity = graphene.String() 
    # woreda = graphene.Int()
    # nationality = graphene.String()       
    business = graphene.String()
    website = graphene.String()
    category =  graphene.String()
    legality  = graphene.String()
    account = graphene.Field(AccountType)
    #2
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        # last_name = graphene.String(required=True)
        first_name = graphene.String(required=True)
        # phoneNo = graphene.String(required=True)
        sex =graphene.String(required=True) 
        # subcity = graphene.String(required=True) 
        # woreda = graphene.Int(required=True)
        # nationality = graphene.String(required=True)    
        business = graphene.String(required=True)
        website = graphene.String(required=True)
        category =  graphene.String(required=True)
        legality  = graphene.String(required=True)

    #3
    def mutate(self, info, username, password, email,
        #  last_name, 
        first_name,
        #  phoneNo, 
        sex,
        #  , subcity, woreda, nationality
        business,website, legality, category
        ):
        user =  Account(
            username=username,
            password = password,
            email=email,
            # subcity = subcity,
            # last_name = last_name,
            first_name = first_name,
            # phoneNo = phoneNo,
            sex = sex
            # ,woreda = woreda,
            # nationality = nationality
        )
        user.set_password(password)
        user.save()

        businessowner = Businessowner(
            business = business, 
            website = website,
            category = category,
            legality = legality,
            account = user
        )
        businessowner.save()


        return CreateBusinessowner(
            id = businessowner.id,
            business = businessowner.business, 
            website  = businessowner.website,
            category = businessowner.category,
            legality = businessowner.legality,
            account  = businessowner.account,
            email = user.email,
            username=user.username,
            password =user.password,
            # subcity = subcity,
            # last_name = last_name,
            first_name = user.first_name,
            # phoneNo = phoneNo,
            sex = user.sex
        )


#4
class Mutation(graphene.ObjectType):
    create_businessowner = CreateBusinessowner.Field()