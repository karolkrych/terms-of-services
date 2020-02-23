from rest_framework.viewsets import ReadOnlyModelViewSet

from terms.models import UserSignedAgreement
from terms.serializers.user_signed_agreement_serializer import UserSignedAgreementSerializer


class UserSignedAgreementViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSignedAgreementSerializer

    def get_queryset(self):
        return UserSignedAgreement.objects.all()
