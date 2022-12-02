from django.db import models
from django.contrib.auth.models import  AbstractUser

class Profile(AbstractUser):
    # handle = models.CharField(unique=True, max_length=15)
    bio = models.CharField(blank=True, max_length=300)
    pfp = models.ImageField(upload_to='pfp/photos', blank=True)
    followers = models.ManyToManyField(
        'Profile',
        related_name='Follower_Profiles',
        blank=True
        )
    following = models.ManyToManyField(
        'Profile',
        related_name='Following_Profiles',
        blank=True
        )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_Followers(self):
        print(self.followers.count())
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_Following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.username


class Post(models.Model):
    poster = models.ForeignKey('Profile', on_delete=models.PROTECT)
    picture = models.ImageField(upload_to='posts/pictures')
    title = models.CharField(max_length=20)
    description = models.CharField(blank=True, max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def get_Likes(self):
        return self.likes_set.count()

class Likes(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    user = models.ForeignKey('Profile', on_delete=models.PROTECT)

    def __str__(self):
        return 'Like: ' + self.user.handle + ' ' + self.post.title

    class Meta:
        unique_together = ('post', 'user')


class Comments(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    user = models.ForeignKey('Profile', on_delete=models.PROTECT)
    comment = models.CharField(max_length=150)
    parent_comment = models.ForeignKey('Comments', on_delete=models.PROTECT, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment