from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from ms2App.models.skills import Skills
from rest_framework.permissions import IsAuthenticated


from ms2App.serializers.skillsSerializer import SkillsSerializer


class SkillsCreateView(generics.CreateAPIView):

    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)