from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CommentViewSet,PostUserLikesViewSet,UserProfileViewSet,UserViewSet,TagViewSet,PostViewSet,AuthViewSet

router =  DefaultRouter()

router.register("auth",AuthViewSet,basename="auth")
router.register("tags",TagViewSet,basename="tag")
router.register("comments",CommentViewSet,basename="comment")
router.register("posts",PostViewSet,basename="post")
router.register("users",UserViewSet,basename="user")
router.register("userProfiles",UserProfileViewSet,basename="userProfile")
router.register("likes",PostUserLikesViewSet,basename="like")

urlpatterns = router.urls
