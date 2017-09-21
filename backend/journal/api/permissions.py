from rest_framework import permissions


class UserPermission(permissions.BasePermission):
     def has_permission(self, request, view):
        return request.user and request.user.is_admin

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class AdminPermission(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    return obj.id == request.user.id or request.user.is_admin