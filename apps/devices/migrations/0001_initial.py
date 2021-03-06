# Generated by Django 2.2.7 on 2019-11-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('device_id', models.CharField(max_length=50)),
                ('device_type', models.CharField(choices=[('SENSOR', 'Dispositivo de Sensores'), ('ACTUATOR', 'Dispositivo de Actuadores Simples'), ('STATION', 'Disposivo de estacion de sensores y actuadores'), ('IR', 'Dispositivo de Control Infrarojo (Envio y Recibo)'), ('ALARM', 'Dispositivo alarma')], max_length=15)),
                ('version', models.PositiveIntegerField(default=1)),
                ('address', models.CharField(max_length=40, null=True)),
                ('status', models.CharField(choices=[('INI', 'Inicial'), ('ERR', 'Error'), ('CON', 'Conectado'), ('NO_CON', 'Desconectado')], default='INI', max_length=10)),
                ('access_key', models.CharField(max_length=40, null=True)),
                ('status_data', models.TextField(max_length=500)),
                ('last_connection', models.DateTimeField(null=True)),
                ('record_history', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
