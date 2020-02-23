from django.urls import include, path
from rest_framework.routers import DefaultRouter

from terms.views import AgreementTemplateViewSet, SignAgreementAPIView, UserSignedAgreementViewSet

router = DefaultRouter()
router.register('agreement-templates', AgreementTemplateViewSet, basename='agreement_template')
router.register('signed-agreements', UserSignedAgreementViewSet, basename='signed_agreements')

urlpatterns = [
    path('', include(router.urls)),
    path('sign-agreement/', SignAgreementAPIView.as_view(), name='sign-agreement'),
]
