import reversion
from django.db import models


@reversion.register()
class AgreementTemplate(models.Model):
    name = models.CharField('Name', help_text='This name is for internal purpose and cannot be changed', max_length=255)
    description = models.CharField('Description', max_length=255, null=True, blank=True)
    content = models.TextField('HTML content of agreement')

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        with reversion.create_revision():
            super().save(**kwargs)
