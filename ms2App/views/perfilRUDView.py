from rest_framework import generics
from ms2App.models import Perfil
from ms2App.serializers import PerfilSerializer


class PerfilRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    lookup_field = 'usuario'
