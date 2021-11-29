from ms2App.models.skills import Skills
from rest_framework import serializers

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Skills
       fields = ['idSkills','nombre','experiencia','dominio','usuario']