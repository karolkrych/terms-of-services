from rest_framework.serializers import ModelSerializer

from terms.models import UserSignedAgreement


class SignAgreementSerializer(ModelSerializer):
    class Meta:
        model = UserSignedAgreement
        fields = ['agreement', ]
