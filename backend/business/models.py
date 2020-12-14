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

    @classmethod
    def terms_and_conditions(cls):
        from business.content import TERMS_AND_CONDITIONS

        t_and_cond, _ = cls.objects.get_or_create(
            title__iexact="Terms and Conditions",
            defaults={"content": TERMS_AND_CONDITIONS},
        )
        return t_and_cond

    @classmethod
    def privacy_policy(cls):
        from business.content import PRIVACY_POLICY

        p_policy, _ = cls.objects.get_or_create(
            title__iexact="Privacy Policy", defaults={"content": PRIVACY_POLICY}
        )
        return p_policy


# Create your models here.
