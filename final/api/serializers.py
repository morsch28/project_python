from rest_framework.serializers import ModelSerializer
from api.models import Comment,UserProfile,Article,Tag,ArticleUserLikes
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.fields import HiddenField,SerializerMethodField
from core.auth import CurrentProfileDefault ,CurrentUserDefault

##serializer - ממיר את האובייקט לג'ייסון

class UserSerializer(ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        validators = [
        RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)([A-Za-z\d]{8,}$)',
                       message="Password must contain.."
                       )
    ])
    class Meta:
        model = User
        fields = ["id","email","username","password"]

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)#דריסה של הפונקציה של סריאלייזר לטובת פונצקיה שמצפינה את הסיסמה
        return user
    
    
    def update(self, instance, validated_data):
        ##חילוץ הסיסמא מהמילון
        password = validated_data.pop("password",None)
        
        for key,value in validated_data.items():
            setattr(instance,key,value)
         
        #מתודה מובנית במחלקה - User 
        #המתודה מצפינה סיסמאות
        if password:
            instance.set_password(password)
        instance.save()
        return instance
         
    
    
class CommentSerializer(ModelSerializer):
    # take the author from jwt
    author = HiddenField(default = CurrentProfileDefault())
    
    # add the author_id to the json
    author_id = SerializerMethodField("get_author_id")
    class Meta:
        model = Comment
        fields = "__all__"
    
    # a helper method that returns id of the author
    def get_author_id(self,obj):
        return obj.author.id
    
class UserProfileSerializer(ModelSerializer):
    user = HiddenField(default = CurrentUserDefault)
    user_id = SerializerMethodField("get_user_id")
    class Meta:
        model = UserProfile
        fields = "__all__"
        
    def get_user_id(self,obj):
        return obj.user.id   

        
class ArticleSerializer(ModelSerializer):
    author = HiddenField(default = CurrentProfileDefault())
    author_id = SerializerMethodField("get_author_id")
    class Meta:
        model = Article
        fields = "__all__"
    
    def get_author_id(self,obj):
        return obj.author.id        
        
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        
class ArticleUserLikesSerializer(ModelSerializer):
    class Meta:
        model = ArticleUserLikes
        fields = "__all__"        
    