from rest_framework import serializers

from terms.models import UserSignedAgreement


class UserSignedAgreementSerializer(serializers.ModelSerializer):
    agreement_content = serializers.SerializerMethodField()

    class Meta:
        model = UserSignedAgreement
        fields = ['id', 'user', 'agreement', 'first_name', 'last_name', 'street', 'postcode', 'agreement_content']

    def get_agreement_content(self, obj):
        return obj.get_rendered_agreement_content()
