from rest_framework import authentication
from business.models import CompanyText
from .serializers import CompanyTextSerializer
from rest_framework import viewsets


class CompanyTextViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTextSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CompanyText.objects.all()
