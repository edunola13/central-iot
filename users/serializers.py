# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('id', 'name',)

#Este es solo para retornar, ya que para guardar no me sirve ya que al tener una nested relathion me hace hacer el create
#a mano y no tiene sentido. Ademas de que me validaria que cada campo grupo tengo todos los atributos que indica el serializer
class UserSerializer(serializers.ModelSerializer):    
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'groups',)
        write_only = ('password',)

#Con este serializer a diferencia al de arriba con pasar un array con id ya guarda lo mas bien la relacion
class UserSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'groups',)
        write_only = ('password',)