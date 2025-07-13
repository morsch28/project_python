from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator,MinLengthValidator

class Tag(models.Model):
    #props
    name = models.CharField(unique=True,max_length=32)
    
    
    #str representation for the admin panel
    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    bio = models.TextField(blank=True,max_length=1000) #blank-empty string
    birthday = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} Profile"


STATUS_CHOICES = [
    ('draft','Draft'),
    ('published','Published'),
    ('archived','Archived')
]
    

class Article(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True,validators=[
        MinLengthValidator(5),
        RegexValidator(regex = '^[a-zA-Z].*$')    
    ])
    text = models.TextField(validators=[MinLengthValidator(5)])
    tags = models.ManyToManyField(Tag,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,default='draft')
    image = models.URLField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.title} by {self.author.user.username}"
    
    
class Comment(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    text = models.TextField(validators=[MinLengthValidator(1)],max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    replay_to = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return super().__str__()
    
LIKE_CHOICES = [
    ('like','Like'),
    ('dislike','Dislike')
]

class ArticleUserLikes(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    article  =  models.ForeignKey(Article,on_delete=models.CASCADE)
    like_type = models.CharField(choices=LIKE_CHOICES,default='like')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # prevent users from liking twice
    class Meta:
        unique_together = ['user','article']
        
    def __str__(self):
        return f"{self.user.user.username} {self.like_type} {self.post.title}"