from django.db import IntegrityError
from django.test import TestCase

from clients.models import Phone, Email, Company
from clients.tests.factories import PhoneFactory, EmailFactory, CompanyFactory


class PhoneModelTestCase(TestCase):
    """Testing the phone model class."""
    def test_create_phone(self):
        phone = PhoneFactory()
        self.assertEqual(Phone.objects.count(), 1)
        self.assertEqual(
            Phone.objects.first().__str__(),
            f'{phone.owner} <+{phone.number}>'
        )

        PhoneFactory()
        self.assertEqual(Phone.objects.count(), 2)

    def test_unique_number(self):
        phone = PhoneFactory()

        with self.assertRaises(IntegrityError):
            PhoneFactory(number=phone.number)


class EmailModelTestCase(TestCase):
    """Testing the email model class."""
    def test_create_email(self):
        email = EmailFactory()
        self.assertEqual(Email.objects.count(), 1)
        self.assertEqual(
            Email.objects.first().__str__(),
            f'{email.owner} <{email.address}>'
        )

        EmailFactory()
        self.assertEqual(Email.objects.count(), 2)

    def test_unique_email(self):
        email = EmailFactory()

        with self.assertRaises(IntegrityError):
            EmailFactory(address=email.address)


class CompanyModelTestCase(TestCase):
    """Testing the company model class."""
    def test_create_company(self):
        company_from_factory = CompanyFactory()
        self.assertEqual(Company.objects.count(), 1)

        company_from_db = Company.objects.first()
        self.assertEqual(company_from_factory.name, company_from_db.name)
        self.assertEqual(company_from_factory.contact_person, company_from_db.contact_person)
        self.assertEqual(company_from_factory.description, company_from_db.description)
        self.assertEqual(company_from_factory.address, company_from_db.address)

    def test_unique_name_company(self):
        company = CompanyFactory()

        with self.assertRaises(IntegrityError):
            CompanyFactory(name=company.name)
