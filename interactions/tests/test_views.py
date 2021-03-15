from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from interactions.models import Interaction
from interactions.tests.factories import InteractionFactory
from companies.tests.factories import CompanyFactory
from projects.tests.factories import ProjectFactory


UserModel = get_user_model()


class InteractionListViewTestCase(TestCase):
    """Testing the interaction list view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_no_interactions(self):
        response = self.client.get(reverse('interaction:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interactions/interaction_list.html')
        self.assertContains(response, "Список взаимодействий пуст.")
        self.assertQuerysetEqual(response.context['interaction_list'], [])

    def test_interaction_list_is_not_empty(self):
        for _ in range(3):
            InteractionFactory()

        response = self.client.get(reverse('interaction:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Список взаимодействий пуст.")
        self.assertEqual(response.context['interaction_list'].count(), 3)

    def test_interaction_with_filter_by_company(self):
        company_1 = CompanyFactory()
        company_2 = CompanyFactory()

        for _ in range(2):
            InteractionFactory(company=company_1)

        InteractionFactory(company=company_2)

        response = self.client.get(f"{reverse('interaction:list')}?company={company_1.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interaction_list'].count(), 2)

        response = self.client.get(f"{reverse('interaction:list')}?company={company_2.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interaction_list'].count(), 1)

    def test_interaction_with_filter_by_project(self):
        project_1 = ProjectFactory()
        project_2 = ProjectFactory()

        for _ in range(2):
            InteractionFactory(project=project_1)

        InteractionFactory(project=project_2)

        response = self.client.get(f"{reverse('interaction:list')}?project={project_1.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interaction_list'].count(), 2)

        response = self.client.get(f"{reverse('interaction:list')}?project={project_2.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interaction_list'].count(), 1)

    def test_interaction_filter_404(self):
        response = self.client.get(f"{reverse('interaction:list')}?project=1")
        self.assertEqual(response.status_code, 404)


class InteractionDetailViewTestCase(TestCase):
    """Testing the interaction detail view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

        for _ in range(3):
            InteractionFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.interaction_list = Interaction.objects.all()

    def test_interaction_not_found(self):
        not_exist_pk = self.interaction_list.last().pk + 1
        response = self.client.get(reverse('interaction:detail', kwargs={'pk': not_exist_pk}))
        self.assertEqual(response.status_code, 404)

    def test_interaction_page(self):
        last_interaction = self.interaction_list.last()
        url = reverse('interaction:detail', kwargs={'pk': last_interaction.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interactions/interaction_detail.html')
        self.assertEqual(response.context['interaction'], last_interaction)


class InteractionEditViewTestCase(TestCase):
    """Testing the interaction edit view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')
        InteractionFactory()

    def setUp(self):
        self.client.login(username='Tester', password='test_password')
        self.interaction = Interaction.objects.first()

    def test_interaction_edit_page(self):
        response = self.client.get(reverse('interaction:edit', kwargs={'pk': self.interaction.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interactions/interaction_form.html')

    def test_update_interaction(self):
        interaction_update = {
            'project': self.interaction.project.pk,
            'company': self.interaction.company.pk,
            'channel': self.interaction.channel,
            'manager': self.interaction.manager.pk,
            'description': self.interaction.description,
            'evaluation': 5 if self.interaction.evaluation != 5 else 1
        }
        url = reverse('interaction:edit', kwargs={'pk': self.interaction.pk})
        response = self.client.post(url, interaction_update)
        self.assertEqual(response.status_code, 302)
        self.interaction.refresh_from_db()
        self.assertEqual(self.interaction.evaluation, interaction_update['evaluation'])


class InteractionCreateViewTestCase(TestCase):
    """Testing the interaction create view."""
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create_user(username='Tester', password='test_password')

    def setUp(self):
        self.client.login(username='Tester', password='test_password')

    def test_interaction_create_page(self):
        response = self.client.get(reverse('interaction:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interactions/interaction_form.html')

    def test_create_new_interaction(self):
        interaction = InteractionFactory()
        new_interaction_data = {
            'project': interaction.project.pk,
            'company': interaction.company.pk,
            'channel': interaction.channel,
            'manager': interaction.manager.pk,
            'description': interaction.description,
            'evaluation': interaction.evaluation
        }
        interaction.delete()
        response = self.client.post(reverse('interaction:create'), new_interaction_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_interaction_data['description'], Interaction.objects.last().description)
