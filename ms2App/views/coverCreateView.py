from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ms2App.serializers.coverSerializer import CoverSerializer
from ms2App.models.cover import Cover
from rest_framework.views import APIView


class CoverCreateView(generics.CreateAPIView):

    queryset = Cover.objects.all()
    serializer_class = CoverSerializer

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)
