from rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView

from terms.models import UserSignedAgreement
from terms.serializers import SignAgreementSerializer


class SignAgreementAPIView(CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SignAgreementSerializer

    def perform_create(self, serializer):
        if not UserSignedAgreement.objects.filter(
                user=self.request.user,
                agreement_id=serializer.validated_data.get('agreement')
        ).exists():
            serializer.save(user=self.request.user)
