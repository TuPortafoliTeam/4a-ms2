from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response

from ms2App.models.cover import Cover
from ms2App.serializers.coverSerializer import CoverSerializer

class CoverUpdateView(generics.UpdateAPIView):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer
    permission_classes = (IsAuthenticated,)