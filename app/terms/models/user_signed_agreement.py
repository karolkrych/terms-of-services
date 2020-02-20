from django.template import Template, Context
from reversion.models import Version

from django.contrib.auth import get_user_model
from django.db import models

from terms.models import AgreementTemplate

User = get_user_model()


class UserSignedAgreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agreement = models.ForeignKey(AgreementTemplate, on_delete=models.CASCADE)
    first_name = models.CharField('User first name', max_length=255)
    last_name = models.CharField('User last name', max_length=255)
    street = models.CharField('User street', max_length=255)
    postcode = models.CharField('User postcode', max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def _get_agreement_version(self):
        versions = Version.objects.get_for_object(self.agreement)   # versions are ordered from the newest
        for version in versions:
            if version.revision.date_created < self.date_created:
                return version

    def get_agreement_content(self) -> str:
        version = self._get_agreement_version()
        return version.field_dict['content'] if version else self.agreement.content

    def get_rendered_agreement_content(self) -> str:
        content = self.get_agreement_content()
        template = Template(content)
        context = Context({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'street': self.street,
            'postcode': self.postcode
        })
        return template.render(context)

    def save(self, **kwargs):
        if self._state.adding:
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
            self.street = self.user.street
            self.postcode = self.user.postcode
        return super().save(**kwargs)
