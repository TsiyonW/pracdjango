import graphene
from graphene_django import DjangoObjectType

from investor.models import Investor

class InvestorType(DjangoObjectType):
    class Meta:
        model = Investor


class Query(graphene.ObjectType):
    profiles = graphene.List(InvestorType)

    def resolve_profiles(self, info, **kwargs):
        return Investor.objects.all()

#1
class CreateInvestor(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)
    last_name = graphene.String(required=True)
    first_name = graphene.String(required=True)
    phoneNo = graphene.String(required=True)
    sex =graphene.String(required=True) 
    subcity = graphene.String() 
    woreda = graphene.Int()
    nationality = graphene.String()
    #2
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        last_name = graphene.String(required=True)
        first_name = graphene.String(required=True)
        phoneNo = graphene.String(required=True)
        sex =graphene.String(required=True) 
        subcity = graphene.String() 
        woreda = graphene.Int()
        nationality = graphene.String()
        # birth_date = graphene.DateTime()

    #3
    def mutate(self, info, username, password, email, last_name, first_name,phoneNo, sex, subcity, woreda, nationality):
        user = Investor(
            username=username,
            password = password,
            email=email,
            last_name = last_name,
            first_name = first_name,
            phoneNo = phoneNo,
            sex = sex,
            subcity = subcity,
            woreda = woreda
            ,nationality = nationality
                # ,
                # birth_date = birth_date
        )
        # user.set_password(password)
        user.save()

        return CreateInvestor(
                id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name = user.last_name,
                email = user.email,
                phoneNo = user.phoneNo,
                sex = user.sex,
                subcity = user.subcity,
                nationality = user.nationality,
                woreda = user.woreda
        )


#4
class Mutation(graphene.ObjectType):
    create_investor = CreateInvestor.Field()