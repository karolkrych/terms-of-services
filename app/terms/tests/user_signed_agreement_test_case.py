from django.contrib.auth import get_user_model
from django.test import TestCase

from terms.models import UserSignedAgreement, AgreementTemplate

User = get_user_model()


class UserSignedAgreementTestCase(TestCase):
    def setUp(self):
        self.agreement_template = AgreementTemplate.objects.create(
            name='terms_of_use',
            content='<p>Hello {{ first_name }} {{ last_name }}</p>'
        )
        self.user = User.objects.create_user(
            username='test_user',
            email='john@example.com',
            first_name='John',
            last_name='Doe',
            street='High Street',
            postcode='M1 1AE'
        )
        self.user_agreement = UserSignedAgreement.objects.create(user=self.user, agreement=self.agreement_template)

    def test_get_agreement_content(self):
        self.assertEqual(self.user_agreement.get_agreement_content(), '<p>Hello {{ first_name }} {{ last_name }}</p>')

    def test_get_agreement_content_after_changing_agreement_content(self):
        self.agreement_template.content = '<p>Agreement content changed</p>'
        self.agreement_template.save()
        self.assertEqual(self.user_agreement.get_agreement_content(), '<p>Hello {{ first_name }} {{ last_name }}</p>')

    def test_get_rendered_agreement_content(self):
        self.assertEqual(self.user_agreement.get_rendered_agreement_content(), '<p>Hello John Doe</p>')

    def test_get_rendered_agreement_content_after_changing_user_personal_data(self):
        self.user.first_name = 'Karl'
        self.user.last_name = 'Smith'
        self.user.save()
        self.assertEqual(self.user_agreement.get_rendered_agreement_content(), '<p>Hello John Doe</p>')
