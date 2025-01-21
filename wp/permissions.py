from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsEditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'editor'

class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'author'

class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'contributor'

class IsSubscriber(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'subscriber'
class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj == request.user    
