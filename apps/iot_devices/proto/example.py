
# RELAYS - ACTUATOR

traits = [
    {
        'id': '1',
        'type': 'ON_OFF',
        'values': {
            'on': 'true'
        }
    },
    {
        'id': '2',
        'type': 'ON_OFF',
        'values': {
            'on': 'false'
        }
    }
]

device = {
    'device_id': 'asa',
    'type': 'ACTUATOR',
    'values': {},
    'traits': traits
}

# ESTACION METEOROLOGICA - SENSOR

traits = [  # AUNQUE DEN LOS MISMOS VALORES PODRIA TENER 2 TRAITS AL MISMO TIEMPO PARA EL FRONT
    {
        'id': '1',
        'type': 'SENSOR',
        'values': {
            'temperature': '38.9',
            'precion': '12.3',
            'MORE...': '...'
        }
    },
    {
        'id': '2',
        'type': 'TEMPERATURE',
        'values': {
            'temperature': '38.9',
        }
    },
    {  # Ver donde configurar
        'id': 'setting',
        'type': 'SETTING',
        'values': {
            'altitude': '12',
        }
    }
]

device = {
    'device_id': 'sas',
    'type': 'SENSOR',
    'values': {
        'altitude': '12'
    },
    'traits': traits
}

# SYNC TO DEVICE (Estacion)

body = {
    'type': 'SYNC',
    'sub_type': 'NONE',
    'device': {
        'values': {  # Only settings level system (optional)
            'report': '10000',  # every x seconds
        }
    },
    'traits': [
        {  # Only settings level device (optional)
            'id': 'setting',
            'type': 'setting',
            'values': {
                'altitude': '12',
            }
        }
    ]
}

# SYNC TO SERVER (Estacion)

body = {
    'type': 'SYNC',
    'sub_type': 'NONE',
    'device': {
        'values': {  # All
            'report': '10000'
        }
    },
    'traits': [
        {
            'id': '1',
            'type': 'SENSOR',
            'values': {
                'temperature': '38.9',
                'precion': '12.3',
                'MORE...': '...'
            }
        },
        {
            'id': '2',
            'type': 'TEMPERATURE',
            'values': {
                'temperature': '38.9',
            }
        },
        {
            'id': 'setting',
            'type': 'setting',
            'values': {
                'altitude': '12'
            }
        }
    ]
}

# EXECUTE TO DEVICE (Estacion)

body = {
    'type': 'EXECUTE',
    'sub_type': 'NONE',
    'traits': [
        {
            'id': 'setting',
            'type': 'SETTING',
            'values': {
                'altitude': '26'
            }
        }
    ]
}

# EXECUTE TO DEVICE (Relays)

body = {
    'type': 'EXECUTE',
    'sub_type': 'NONE',
    'traits': [
        {
            'id': '1',
            'type': 'ON_OFF',
            'values': {
                'on': 'true'
            }
        }
    ]
}

# STATE / REPORT TO SERVER (Estacion)

body = {
    'type': 'STATE',
    'sub_type': 'REPORT',
    'traits': [
        {
            'id': '1',
            'type': 'SENSOR',
            'values': {
                'temperature': '38.9',
                'precion': '12.3',
                'MORE...': '...'
            }
        },
        {
            'id': '2',
            'type': 'TEMPERATURE',
            'values': {
                'temperature': '38.9',
            }
        }
    ]
}

# STATE / NOTIFY TO SERVER (Relays)

body = {
    'type': 'STATE',
    'sub_type': 'NOTIFY',
    'traits': [
        {
            'id': '1',
            'type': 'ON_OFF',
            'values': {
                'on': 'true'
            }
        },
        {
            'id': '2',
            'type': 'ON_OFF',
            'values': {
                'on': 'false'
            }
        }
    ]
}

# STATE / NONE TO DEVICE (any)

body = {
    'type': 'STAT',
    'sub_type': 'NONE',
}

# STATE / NODE TO SERVER (Relays)

body = {
    'type': 'SYNC',
    'sub_type': 'NONE',
    'device': {
        'values': {  # All
            'report': '10000'
        }
    },
    'traits': [
        {
            'id': '1',
            'type': 'SENSOR',
            'values': {
                'temperature': '38.9',
                'precion': '12.3',
                'MORE...': '...'
            }
        },
        {
            'id': '2',
            'type': 'TEMPERATURE',
            'values': {
                'temperature': '38.9',
            }
        },
        {
            'id': 'setting',
            'type': 'setting',
            'values': {
                'altitude': '12'
            }
        }
    ]
}
