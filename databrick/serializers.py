from rest_framework import serializers
from .models import DatabrickModel

class DatabrickSerializer(serializers.ModelSerializer):
    class Meta:
        model=DatabrickModel
        fields=('id','instruction','context','response','category')