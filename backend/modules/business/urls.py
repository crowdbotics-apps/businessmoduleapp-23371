from django.urls import path

from modules.business.views import PrivacyPolicyView, TermsAndConditionsView

urlpatterns = [
    path("privacy-policy", PrivacyPolicyView.as_view()),
    path("terms-and-conditions", TermsAndConditionsView.as_view())
]
