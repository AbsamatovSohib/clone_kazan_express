from rest_framework import permissions


class HasRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method == "GET":
            required_roles = getattr(view, 'required_roles', [])
            if request.user.role.filter(name__in=required_roles).exists():
                return True
        return False

class HasRolePermissionPost(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has any of the required roles
        SAFE_METHODS = ("PUT","PATCH","GET")
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            required_roles = getattr(view, 'required_roles', [])
            if request.user.role.filter(name__in=required_roles).exists():
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.category.shop.owner:
            return True
        return False
