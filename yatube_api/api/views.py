from rest_framework import filters
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from posts.models import Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, FollowSerializer
from .serializers import GroupSerializer, PostSerializer

User = get_user_model()


class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        if not self.kwargs:
            serializer.save(author=self.request.user)
        else:
            serializer.save(
                author=self.request.user,
                post_id=int(self.kwargs.get('post_id'))
            )


class PostViewSet(ContentViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(ContentViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        username = serializer.validated_data.get('following')
        following = get_object_or_404(User, username=username)
        user = self.request.user
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        serializer.save(
            user=user,
            following=following
        )
