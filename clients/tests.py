from django.test import TestCase

from clients.models import Company


class CompanyModelTestCase(TestCase):
    def setUp(self):
        self.company = {
            'name': 'Test Company',
            'contact_person': 'Super Manager',
            'description': 'Company description',
            'address': 'company address'
        }

    def test_create_company(self):
        first_company = Company.objects.create(**self.company)
        self.assertEqual(Company.objects.count(), 1)

        self.assertEqual(first_company.name, self.company['name'])
        self.assertEqual(first_company.contact_person, self.company['contact_person'])
        self.assertEqual(first_company.description, self.company['description'])
        self.assertEqual(first_company.address, self.company['address'])
