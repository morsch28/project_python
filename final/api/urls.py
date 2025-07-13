from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CommentViewSet,ArticleUserLikesViewSet,UserProfileViewSet,UserViewSet,TagViewSet,ArticleViewSet,AuthViewSet

router =  DefaultRouter()

router.register("auth",AuthViewSet,basename="auth") 
router.register("tags",TagViewSet,basename="tag")
router.register("comments",CommentViewSet,basename="comment")
router.register("articles",ArticleViewSet,basename="article")
router.register("users",UserViewSet,basename="user")
router.register("userProfiles",UserProfileViewSet,basename="userProfile")
router.register("likes",ArticleUserLikesViewSet,basename="like")

urlpatterns = router.urls
