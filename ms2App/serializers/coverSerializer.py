from ms2App.models.cover import Cover
from rest_framework import serializers

class CoverSerializer(serializers.ModelSerializer):
    class Meta:
       model = Cover
       fields = ['idCover','idUsuario','trabajo','contenido']
       