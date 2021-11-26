from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from ms2App.models.skills import Skills
from ms2App.serializers.skillsSerializer import SkillsSerializer

class SkillsView(generics.RetrieveAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    
    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
