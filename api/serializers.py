from rest_framework import serializers
from .models import Generos, Opinions,Usuarios

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = "__all__"

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = "__all__"

class OpinionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinions
        fields = "__all__"
