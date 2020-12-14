from rest_framework import serializers
from business.models import CompanyText


class CompanyTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyText
        fields = "__all__"
