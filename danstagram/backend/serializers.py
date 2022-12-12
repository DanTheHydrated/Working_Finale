from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # pfp = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.pfp = validated_data.get('pfp', instance.pfp)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.followers = validated_data('followers', instance.followers)
        instance.following = validated_data('following', instance.following)
        instance.modified = validated_data('modified', instance.modified)
        instance.save()
        return instance
    
    def get_following(self, obj):
        return FollowingSerializer(obj.users_followed.all(),many=True).data

    def get_followers(self,obj):
        return FollowerSerializer(obj.users_following.all(), many=True).data


class CommentSerializer(serializers.Serializer):
    commenter = serializers.ReadOnlyField(source='Profile.username')
    class Meta:
        model = Comments
        fields = ('id', 'commenter', 'post', 'comment', 'parent_comment', 'created', 'modified')



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    picture = serializers.URLField(required=True)
    user = serializers.ReadOnlyField(source='Profile.id')
    class Meta:
        model = Post 
        fields = '__all__'




class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('following', 'followers')

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'followers', 'created_at')

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'following', 'created_at')