from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Allow only admin users to access the view
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff and request.user.is_superuser
  
    
class IsStaff(permissions.BasePermission):
    """
        Allow only staff users to access view
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
 
#רק למשתמש שכתב את התגובה מותר לערוך אותה
#כל משתמש יכול לקרוא את התגובות אבל לא לערוך אותן   
class CommentOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        # if the method is GET/OPTIONS/HEAD(read-only) allow access
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if hasattr(obj,"author") and hasattr(obj.author,"user"):
            return obj.author.user == request.user
        
        return False

class ArticlePermission(permissions.BasePermission):
    # regular user can only view
    # admin can also edit and delete
    
    def has_permission(self, request, view):
        
        # all users can read
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_superuser  or request.user.is_staff
    
class TagPermission(ArticlePermission):
    """
    Allow admin to write Tags, all users can read
    """

class UserProfilePermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser
    

class UserLikesPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.user == request.user or request.user.is_superuser