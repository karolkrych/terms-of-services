from django.contrib import admin

from terms.models import AgreementTemplate, UserSignedAgreement

admin.site.register(AgreementTemplate)
admin.site.register(UserSignedAgreement)
