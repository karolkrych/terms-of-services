from rest_framework.serializers import ModelSerializer

from terms.models import AgreementTemplate


class AgreementTemplateSerializer(ModelSerializer):
    class Meta:
        model = AgreementTemplate
        fields = '__all__'
