from rest_framework import generics
from ms2App.models import PerfilEmpresa
from ms2App.serializers import PerfilEmpresaSerializer


class PerfilEmpresaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerfilEmpresa.objects.all()
    serializer_class = PerfilEmpresaSerializer
