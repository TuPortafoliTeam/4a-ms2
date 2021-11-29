from django.conf import settings
from rest_framework import generics



from ms2App.models.cover import Cover
from ms2App.serializers.coverSerializer import CoverSerializer

class CoverDetailView(generics.RetrieveAPIView):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer
    
    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)