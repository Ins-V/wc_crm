from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from companies.tests.factories import CompanyFactory, PhoneFactory, EmailFactory
from companies.models import Company, Phone, Email


UserModel = get_user_model()


class CompanyListViewTestCase(TestCase):
    """Testing the company list view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_no_companies(self):
        response = self.client.get(reverse('company:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_list.html')
        self.assertContains(response, "Список компаний пуст.")
        self.assertQuerysetEqual(response.context['company_list'], [])

    def test_company_list_is_not_empty(self):
        for _ in range(3):
            CompanyFactory()

        response = self.client.get(reverse('company:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Список компаний пуст.")
        self.assertEqual(response.context['company_list'].count(), 3)


class CompanyDetailViewTestCase(TestCase):
    """Testing the company detail view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

        for _ in range(3):
            CompanyFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.company_list = Company.objects.all()

    def test_company_not_found(self):
        not_exist_pk = self.company_list.last().pk + 1
        response = self.client.get(reverse('company:detail', kwargs={'pk': not_exist_pk}))
        self.assertEqual(response.status_code, 404)

    def test_company_page(self):
        last_company = self.company_list.last()
        url = reverse('company:detail', kwargs={'pk': last_company.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_detail.html')
        self.assertEqual(response.context['company'], last_company)


class CompanyCreateViewTestCase(TestCase):
    """Testing the company create view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_company_create_page(self):
        response = self.client.get(reverse('company:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_form.html')

    def test_create_new_company(self):
        new_company_data = {
            'name': 'Test company name',
            'description': '<p>Test company description.</p>',
            'contact_person': 'Test contact person',
            'address': 'Test address'
        }
        response = self.client.post(reverse('company:create'), new_company_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_company_data['name'], Company.objects.last().name)


class CompanyEditViewTestCase(TestCase):
    """Testing the company edit view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')
        CompanyFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.company = Company.objects.first()

    def test_company_edit_page(self):
        response = self.client.get(reverse('company:edit', kwargs={'pk': self.company.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_form.html')
        self.assertContains(response, self.company.name)

    def test_update_company(self):
        company_update = {
            'name': f'{self.company.name} UPD',
            'description': self.company.description,
            'contact_person': self.company.contact_person,
            'address': self.company.address
        }
        url = reverse('company:edit', kwargs={'pk': self.company.pk})
        response = self.client.post(url, company_update)
        self.assertEqual(response.status_code, 302)
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, company_update['name'])


class CompanyContactsViewTestCase(TestCase):
    """Testing the company contacts view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_company_contacts_page(self):
        response = self.client.get(reverse('company:contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/company_contacts.html')


class CompanyPhoneListViewTestCase(TestCase):
    """Testing the company phone list view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_phone_list_is_empty(self):
        response = self.client.get(reverse('company:phone_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/phone_list.html')
        self.assertContains(response, "Список контактных номеров пуст.")
        self.assertQuerysetEqual(response.context['phone_list'], [])

    def test_phone_list_is_not_empty(self):
        for _ in range(3):
            PhoneFactory()

        response = self.client.get(reverse('company:phone_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Список контактных номеров пуст.")
        self.assertEqual(response.context['phone_list'].count(), 3)


class CompanyPhoneCreateViewTestCase(TestCase):
    """Testing the company phone create view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_phone_create_page(self):
        response = self.client.get(reverse('company:phone_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/phone_form.html')

    def test_create_new_phone(self):
        new_phone_data = {
            'number': '380931112233',
            'owner': 'Test owner'
        }
        response = self.client.post(reverse('company:phone_add'), new_phone_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_phone_data['number'], Phone.objects.last().number)


class CompanyPhoneEditViewTestCase(TestCase):
    """Testing the company phone edit view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')
        PhoneFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.phone = Phone.objects.first()

    def test_phone_edit_page(self):
        response = self.client.get(reverse('company:phone_edit', kwargs={'pk': self.phone.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/phone_form.html')

    def test_update_phone(self):
        phone_update = {
            'number': self.phone.number,
            'owner': f'{self.phone.owner} UPD'
        }
        url = reverse('company:phone_edit', kwargs={'pk': self.phone.pk})
        response = self.client.post(url, phone_update)
        self.assertEqual(response.status_code, 302)
        self.phone.refresh_from_db()
        self.assertEqual(self.phone.owner, phone_update['owner'])


class CompanyPhoneDeleteViewTestCase(TestCase):
    """Testing the company phone delete view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

        for _ in range(3):
            PhoneFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.phone = Phone.objects.last()

    def test_phone_confirm_delete(self):
        response = self.client.get(reverse('company:phone_delete', kwargs={'pk': self.phone.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/phone_confirm_delete.html')
        self.assertEqual(response.context['phone'], self.phone)

    def test_phone_delete(self):
        response = self.client.post(reverse('company:phone_delete', kwargs={'pk': self.phone.pk}))
        self.assertEqual(Phone.objects.count(), 2)
        self.assertRedirects(response, reverse('company:phone_list'), 302)


class CompanyEmailListViewTestCase(TestCase):
    """Testing the company email list view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_email_list_is_empty(self):
        response = self.client.get(reverse('company:email_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/email_list.html')
        self.assertContains(response, "Список контактных email адресов пуст.")
        self.assertQuerysetEqual(response.context['email_list'], [])

    def test_email_list_is_not_empty(self):
        for _ in range(3):
            EmailFactory()

        response = self.client.get(reverse('company:email_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Список контактных email адресов пуст.")
        self.assertEqual(response.context['email_list'].count(), 3)


class CompanyEmailCreateViewTestCase(TestCase):
    """Testing the company email create view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_email_create_page(self):
        response = self.client.get(reverse('company:email_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/email_form.html')

    def test_create_new_email(self):
        new_email_data = {
            'address': 'test@mail.com',
            'owner': 'Test owner'
        }
        response = self.client.post(reverse('company:email_add'), new_email_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_email_data['address'], Email.objects.last().address)


class CompanyEmailEditViewTestCase(TestCase):
    """Testing the company email edit view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')
        EmailFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.email = Email.objects.first()

    def test_email_edit_page(self):
        response = self.client.get(reverse('company:email_edit', kwargs={'pk': self.email.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/email_form.html')

    def test_update_email(self):
        email_update = {
            'address': self.email.address,
            'owner': f'{self.email.owner} UPD'
        }
        url = reverse('company:email_edit', kwargs={'pk': self.email.pk})
        response = self.client.post(url, email_update)
        self.assertEqual(response.status_code, 302)
        self.email.refresh_from_db()
        self.assertEqual(self.email.owner, email_update['owner'])


class CompanyEmailDeleteViewTestCase(TestCase):
    """Testing the company email delete view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

        for _ in range(3):
            EmailFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.email = Email.objects.last()

    def test_email_confirm_delete(self):
        response = self.client.get(reverse('company:email_delete', kwargs={'pk': self.email.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'companies/email_confirm_delete.html')
        self.assertEqual(response.context['email'], self.email)

    def test_email_delete(self):
        response = self.client.post(reverse('company:email_delete', kwargs={'pk': self.email.pk}))
        self.assertEqual(Email.objects.count(), 2)
        self.assertRedirects(response, reverse('company:email_list'), 302)
