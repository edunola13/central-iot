from rest_framework import permissions

from ir.models import IrControl

class ControlPermissions(permissions.BasePermission):
    GROUP = 'Automatizador'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user or request.user.is_staff or request.user.groups.filter(name=self.GROUP)


#Esta clase permita que todos lean y solo el grupo "Automatizador" pueda editar
#Si se quiere que todos esten logueados agregar el permiso en la vista
class ActionPermissions(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    GROUP = 'Automatizador'

    def has_permission(self, request, view):
        print (request.method)
        if request.method != 'POST':
            return True
        
        print (request.data)
        if ('control' not in request.data):
            return True
                
        control = IrControl.objects.get(pk=request.data['control'])
        if control is None:
            return True

        return control.owner == request.user or request.user.is_staff or request.user.groups.filter(name=self.GROUP)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.control.owner == request.user or request.user.is_staff or request.user.groups.filter(name=self.GROUP)
        