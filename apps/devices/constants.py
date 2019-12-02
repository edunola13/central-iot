
TYPE_SENSOR = 'SENSOR'
TYPE_ACTUATOR = 'ACTUATOR'
TYPE_STATION = 'STATION'
TYPE_IR = 'IR'
TYPE_ALARM = 'ES_AL_1'

DEVICE_TYPES = (
    (TYPE_SENSOR, 'Dispositivo de Sensores'),
    (TYPE_ACTUATOR, 'Dispositivo de Actuadores Simples'),
    (TYPE_STATION, 'Disposivo de estacion de sensores y actuadores'),
    (TYPE_IR, 'Dispositivo de Control Infrarojo (Envio y Recibo)'),
    (TYPE_ALARM, 'Dispositivo Alarma ESP')
)

DEVICE_STATUS_INI = 'INI'
DEVICE_STATUS_ERR = 'ERR'
DEVICE_STATUS_CON = 'CON'
DEVICE_STATUS_NO_CON = 'NO_CON'
DEVICE_STATUS_CHOICES = (
    (DEVICE_STATUS_INI, 'Inicial'),
    (DEVICE_STATUS_ERR, 'Error'),
    (DEVICE_STATUS_CON, 'Conectado'),
    (DEVICE_STATUS_NO_CON, 'Desconectado'),
)
