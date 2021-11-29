from ms2App.models.perfilEmpresa import PerfilEmpresa
from rest_framework import serializers

class PerfilEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
       model = PerfilEmpresa
       fields = ['idPerfilEmpresa','vacantes','calificacion','añoCreacion','usuario']