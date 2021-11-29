from rest_framework import generics
from ms2App.models import Perfil
from ms2App.serializers import PerfilSerializer


class PerfilCreateView(generics.CreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
