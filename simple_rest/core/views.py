from django.http import HttpResponse
from rest_framework import viewsets, filters, permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from oauth2_provider.models import AccessToken

from simple_rest.core.models import NewsItem
from simple_rest.core.serializers import NewsItemSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the article.
        return obj.author == request.user


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('author__id',)
    ordering = ('created',)
    permission_classes = (TokenHasReadWriteScope, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


def revoke_access(request):
    """
    Revokes access for the given access token
    """
    token = request.META['HTTP_AUTHORIZATION'].replace('Bearer ', '')
    AccessToken.objects.filter(token=token).delete()
    return HttpResponse()