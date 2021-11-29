from django.conf import settings
from rest_framework import generics



from ms2App.models.skills import Skills
from ms2App.serializers.skillsSerializer import SkillsSerializer

class SkillsDetailView(generics.RetrieveAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    
    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
