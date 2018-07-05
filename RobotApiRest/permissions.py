from rest_framework import permissions

#Esta clase permita que todos lean y solo el grupo "Automatizador" pueda editar
#Si se quiere que todos esten logueados agregar el permiso en la vista
class AutomatizadorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    GROUP = 'Automatizador'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_staff or request.user.groups.filter(name=self.GROUP);
        

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.groups.filter(name=self.GROUP);
        