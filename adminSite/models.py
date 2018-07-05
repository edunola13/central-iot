from django.contrib import admin
from devices.models import Device
from sensors.models import Sensor, SensorReading

class DeviceAdmin(admin.ModelAdmin):
    #Campos que se van a usar, puede no inluirse
    #fields = ('campo1', 'campo2', 'funcionX-definida aca o en el model')
    #Campos a excluir
    #exclude = ('campo1',)
    #Lo que muestra en el listado
    readonly_fields = ('code', 'deviceType', 'created')
    list_display = ('code', 'name', 'deviceType', 'created')
    search_fields = ['code', 'name']
    list_filter = ('deviceType',)

    pass

class SensorAdmin(admin.ModelAdmin):
    readonly_fields = ('code', 'sensorType', 'device', 'lastUpdate', 'created')
    list_display = ('code', 'name', 'sensorType', 'device', 'created')
    search_fields = ['code', 'name']
    list_filter = ('sensorType', 'device')
    pass

admin.site.register(Device, DeviceAdmin)
admin.site.register(Sensor, SensorAdmin)