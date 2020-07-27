from apps.devices.constants import *

from apps.devices.clients.alarm_esp_client import AlarmESPClient


CLIENT_OF_DEVICE = {
    TYPE_ALARM: AlarmESPClient
}
