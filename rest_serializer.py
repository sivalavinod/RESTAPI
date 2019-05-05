from rest_framework.serializers import ModelSerializer
from .models import Empmodel

class StuSerilizer(ModelSerializer):
    class Meta:
        model=Empmodel
        fields=["idno","name","salary"]