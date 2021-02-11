from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article

#if there is new user registration he must get a token
from rest_framework.authtoken.views import Token




class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']


#default django user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # it is a build in django model
        fields = ['id', 'username', 'password']
        
        #  password not visible in postman
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}
    
    # harsh password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user) #here is to create token when user signup
        return user
    












'''

from api.serializers import ArticleSerializer
serializer = ArticleSerializer()
print(repr(serializer))


'''









# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=400)
    
#     #validate data method
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
    
    