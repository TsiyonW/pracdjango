import graphene
from graphene_django import DjangoObjectType

from users.models import Profile

class UserType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    profiles = graphene.List(UserType)

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()

#1
class CreateUser(graphene.Mutation):
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
        user = Profile(
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

        return CreateUser(
                id=profile.id,
                username=profile.username,
                first_name=profile.first_name,
        )


#4
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()














# import graphene
# from graphene_django import DjangoObjectType
# from users.models import Profile
# from django.contrib.auth.models  import User

# class UserType(DjangoObjectType):
#     class Meta:
#         model = Profile 
# class CreateUser(graphene.Mutation):
#     user = graphene.Field(UserType)

#     class Arguments:
#         username = graphene.String(required=True)
#         password = graphene.String(required=True)
#         email = graphene.String(required=True)
#         last_name = graphene.String(required=True)
#         first_name = graphene.String(required=True)
#         phoneNo = graphene.String(required=True)
#         sex =graphene.String(required=True) 
#         subcity = graphene.String() 
#         woreda = graphene.Int()
#         nationality = graphene.String()
#         # birth_date = graphene.DateTime()

#     def mutate(self, info, username, password, email, last_name, first_name
#     , 
#     phoneNo, sex, subcity, woreda
#     , nationality
#     # , birth_date
#     ):
#         user = Profile(
#             username=username,
#             password = password,
#             email=email,
#             last_name = last_name,
#             first_name = first_name,
#             phoneNo = phoneNo,
#             sex = sex,
#             subcity = subcity,
#             woreda = woreda
#             # ,nationality = nationality
#             # ,
#             # birth_date = birth_date
#         )
#         # user.set_password(password)
#         user.save()

#         # return CreateUser(user=user)

# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field(UserType)


# class Query(graphene.AbstractType):
#     me = graphene.Field(UserType)
#     users = graphene.List(UserType)

#     def resolve_users(self, info):
#         # return User.objects.all().select_related('profile')
#         return "Profile.objects.all()"

#     def resolve_me(self, info):
#         user = info.context.user
#         if user.is_anonymous:
#             raise Exception('Not logged in!')

#         return "user"
