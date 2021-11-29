from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from ms2App.models.skills import Skills


from ms2App.serializers.skillsSerializer import SkillsSerializer


class SkillsCreateView(generics.CreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)
