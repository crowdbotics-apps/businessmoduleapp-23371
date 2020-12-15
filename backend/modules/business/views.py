from .content import TERMS_AND_CONDITIONS, PRIVACY_POLICY
from rest_framework import authentication, views
from rest_framework.response import Response


DEFAULT_AUTH_CLASSES = (
    authentication.SessionAuthentication,
    authentication.TokenAuthentication,
)


class TermsAndConditionsView(views.APIView):
    authentication_classes = DEFAULT_AUTH_CLASSES

    def get(self, request, *args, **kwargs):
        return Response(TERMS_AND_CONDITIONS, status=200)


class PrivacyPolicyView(views.APIView):
    authentication_classes = DEFAULT_AUTH_CLASSES

    def get(self, request, *args, **kwargs):
        return Response(PRIVACY_POLICY, status=200)
