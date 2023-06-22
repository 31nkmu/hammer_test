from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class FullRegisteredOrReadOnly(permissions.BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        """
        Только зарегистрированный пользователь может добавлять продукты
        """
        if request.method == 'GET':
            return True
        try:
            return request.user.full_registered and request.user.is_authenticated
        except AttributeError:
            return False

    # RETRIEVE, UPDATE, DELETE
    def has_object_permission(self, request, view, obj):
        """
        Только полностью зарегистрированный пользователь товара может его изменять или удалять
        """
        if request.method in SAFE_METHODS:
            return True
        try:
            return request.user.is_authenticated and (
                    (request.user == obj.user and request.user.full_registered) or request.user.is_staff)
        except AttributeError:
            return False
