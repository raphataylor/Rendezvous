from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    CountryID = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CountryName

    class Meta:
        verbose_name_plural = 'countries'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BornInCountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='born_users')
    LivingInCountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='living_users')
    Picture = models.ImageField(upload_to='profile_images', blank=True)
    Bio = models.CharField(max_length=500)
    CountriesVisited = models.ManyToManyField(Country, related_name='countries_visited')

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    TagID = models.AutoField(primary_key=True)
    TagName = models.CharField(max_length=30)

    def __str__(self):
        return self.TagName
    
class Post(models.Model):
    # post id, primary key
    PostID = models.AutoField(primary_key=True)
    # profile.user.username, foreign key
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    Picture = models.ImageField()
    Title = models.CharField(max_length=100, default='Post Title')
    Text = models.CharField(max_length=10000)
    Upvotes = models.IntegerField(default=0)  # Provide a default value
    Downvotes = models.IntegerField(default=0)  # Provide a default value
    CountryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='posts')
    Tags = models.ManyToManyField(Tag, related_name='posts')
    is_featured = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    upvoted_by = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    downvoted_by = models.ManyToManyField(User, related_name='downvoted_posts', blank=True)

    def __str__(self):
        return f"Post ID: {self.PostID}"

class Comment(models.Model):
    CommentID = models.AutoField(primary_key=True)
    Content = models.CharField(max_length=280)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    Upvotes = models.IntegerField(default=0)
    Downvotes = models.IntegerField(default=0)
    PostID = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    upvoted_by = models.ManyToManyField(User, related_name='upvoted_comments', blank=True)
    downvoted_by = models.ManyToManyField(User, related_name='downvoted_comments', blank=True)

    def __str__(self):
        return f"Comment ID: {self.CommentID}"