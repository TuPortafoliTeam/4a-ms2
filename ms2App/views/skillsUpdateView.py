from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from ms2App.serializers.skillsSerializer import SkillsSerializer
from ms2App.models.skills import Skills


class SkillsUpdateView(generics.UpdateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = (IsAuthenticated,)
