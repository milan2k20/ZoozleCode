from rest_framework_jwt.serializers import JSONWebTokenSerializer


class UserLoginSerializer(JSONWebTokenSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(UserLoginSerializer, cls).get_token(user)

        # Add custom claims

        token['username'] = user.username
        return token
