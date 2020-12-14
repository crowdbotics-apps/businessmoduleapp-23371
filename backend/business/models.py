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


# Create your models here.
