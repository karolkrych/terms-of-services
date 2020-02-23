from rest_framework.viewsets import ModelViewSet

from terms.models import AgreementTemplate
from terms.serializers import AgreementTemplateSerializer


class AgreementTemplateViewSet(ModelViewSet):
    serializer_class = AgreementTemplateSerializer

    def get_queryset(self):
        return AgreementTemplate.objects.all()
