from django.conf import settings
from django.db import models


class CompanyText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )

    @classmethod
    def terms_and_conditions(cls):
        return cls.objects.filter(title__iexact="Terms and Conditions").first()

    @classmethod
    def privacy_policy(cls):
        return cls.objects.filter(title__iexact="Privacy Policy").first()

    @classmethod
    def terms_and_conditions(cls):
        return cls.objects.filter(title__iexact="Terms and Conditions").first()

    @classmethod
    def privacy_policy(cls):
        return cls.objects.filter(title__iexact="Privacy Policy").first()


# Create your models here.
