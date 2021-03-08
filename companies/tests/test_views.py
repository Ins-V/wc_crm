from django.test import TestCase
from django.urls import reverse

from companies.tests.factories import CompanyFactory
from companies.models import Company


class CompanyListViewTestCase(TestCase):
    """Testing the company list view."""
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
        for _ in range(3):
            CompanyFactory()

    def setUp(self):
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
        CompanyFactory()

    def setUp(self):
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
