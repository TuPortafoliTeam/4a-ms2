from django.conf import settings
from rest_framework import generics, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ms2App.models.cover import Cover
from ms2App.serializers.coverSerializer import CoverSerializer

class CoverDeleteView(generics.DestroyAPIView):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self,request,*args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({'mensaje':'Cover borradas'},status=status.HTTP_200_OK)