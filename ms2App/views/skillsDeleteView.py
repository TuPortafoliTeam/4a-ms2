from django.conf import settings
from rest_framework import generics, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ms2App.serializers.skillsSerializer import SkillsSerializer
from ms2App.models.skills import Skills

class SkillsDeleteView(generics.DestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self,request,*args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({'mensaje':'skills borradas'},status=status.HTTP_200_OK)