
from rest_framework import permissions


class CustomPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        
        user_permission = self.__get_user_permissions(
            method=request.method, 
            meta_class=view.queryset.model._meta
        )
        return request.user.has_perm(user_permission) if user_permission else False
    
    def __get_user_permissions(self, method, meta_class):
        try:
            model_name = meta_class.model_name
            app_label = meta_class.app_label
            action = self.__get_user_actions(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_user_actions(self, method):
        methods = {
            'OPTIONS': 'view',
            'HEAD': 'view',
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
        }
        return methods.get(method, '')