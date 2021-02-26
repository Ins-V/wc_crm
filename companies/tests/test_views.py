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
        self.assertContains(response, "Список клиентов пуст.")
        self.assertQuerysetEqual(response.context['company_list'], [])

    def test_company_list_is_not_empty(self):
        for _ in range(3):
            CompanyFactory()

        response = self.client.get(reverse('company:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Список клиентов пуст.")
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
