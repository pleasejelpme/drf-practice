from rest_framework import permissions

class StaffEditorPermitions(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        return request.user.is_staff
