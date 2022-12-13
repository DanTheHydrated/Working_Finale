from django.db import models
from django.contrib.auth.models import  AbstractUser

class Profile(AbstractUser):
    # handle = models.CharField(unique=True, max_length=15)
    bio = models.CharField(blank=True, max_length=300)
    # pfp = models.ForeignKey('Post', on_delete=models.PROTECT, null=True, blank=True)
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

    # def get_Followers(self):
    #     print(self.followers.count())
    #     if self.followers.count():
    #         return self.followers.count()
    #     else:
    #         return 0

    # def get_Following(self):
    #     if self.following.count():
    #         return self.following.count()
    #     else:
    #         return 0

    def __str__(self):
        return self.username

# def pfp_Upload(instance, filename):
#     return 'users/{filename}'.format(filename=filename)

class Post(models.Model):
    poster = models.ForeignKey('Profile', on_delete=models.PROTECT, null=True, blank=True)
    picture = models.URLField(null=False, blank=False, max_length=200, default='https://firebasestorage.googleapis.com/v0/b/danstagram-ad70a.appspot.com/o/posts%2FAnon.png?alt=media&token=25131999-4c9d-4362-b093-dccadb402b2d')
    title = models.CharField(max_length=20, null= True, blank = True)
    description = models.CharField(blank=True, max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def get_Likes(self):
        return self.likes_set.count()

# Path for the Photos
    # def upload_to(instance, filename):
    #     return 'images/{filename}'.format(filename=filename)


class Likes(models.Model):
    post = models.ForeignKey('Post', on_delete=models.PROTECT)
    user = models.ForeignKey('Profile', on_delete=models.PROTECT)

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title

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

class Follow(models.Model):
    following = models.ForeignKey('Profile', on_delete=models.PROTECT, default=None, null=False, related_name='users_followed')
    followers = models.ForeignKey('Profile', on_delete=models.PROTECT, default=None, null=False, related_name='users_following')
    created_at = models.DateField(auto_now_add=True, db_index=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['following','followers'],  name="unique_followers")
        ]

        ordering = ["-created_at"]

        def __str__(self):
            return self.followers
