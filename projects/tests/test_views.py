from django.test import TestCase
from django.urls import reverse

from projects.models import Project
from projects.tests.factories import ProjectFactory


class ProjectListViewTestCase(TestCase):
    """Testing the project list view."""
    def test_no_projects(self):
        response = self.client.get(reverse('project:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list.html')
        self.assertContains(response, "Список проектов пуст.")
        self.assertQuerysetEqual(response.context['project_list'], [])

    def test_projects_list_is_not_empty(self):
        for _ in range(3):
            ProjectFactory()

        response = self.client.get(reverse('project:list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Список проектов пуст.")
        self.assertEqual(response.context['project_list'].count(), 3)


class ProjectDetailViewTestCase(TestCase):
    """Testing the project detail view."""
    @classmethod
    def setUpTestData(cls):
        for _ in range(3):
            ProjectFactory()

    def setUp(self):
        self.project_list = Project.objects.all()

    def test_project_not_found(self):
        not_exist_pk = self.project_list.last().pk + 1
        response = self.client.get(reverse('project:detail', kwargs={'pk': not_exist_pk}))
        self.assertEqual(response.status_code, 404)

    def test_project_page(self):
        last_project = self.project_list.last()
        url = reverse('project:detail', kwargs={'pk': last_project.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_detail.html')
        self.assertEqual(response.context['project'], last_project)


class ProjectCreateViewTestCase(TestCase):
    """Testing the project create view."""
    def test_project_create_page(self):
        response = self.client.get(reverse('project:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_form.html')

    def test_create_new_project(self):
        project = ProjectFactory()
        new_project_data = {
            'name': project.name,
            'description': project.description,
            'start_date': project.start_date,
            'end_date': project.end_date,
            'price': project.price,
            'company': project.company.pk
        }
        project.delete()
        response = self.client.post(reverse('project:create'), new_project_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_project_data['name'], Project.objects.last().name)


class ProjectEditViewTestCase(TestCase):
    """Testing the project edit view."""
    @classmethod
    def setUpTestData(cls):
        ProjectFactory()

    def setUp(self):
        self.project = Project.objects.first()

    def test_project_edit_page(self):
        response = self.client.get(reverse('project:edit', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_form.html')
        self.assertContains(response, self.project.name)

    def test_update_project(self):
        project_update = {
            'name': f'{self.project.name} UPD',
            'description': self.project.description,
            'start_date': self.project.start_date,
            'end_date': self.project.end_date,
            'price': self.project.price,
            'company': self.project.company.pk
        }
        url = reverse('project:edit', kwargs={'pk': self.project.pk})
        response = self.client.post(url, project_update)
        self.assertEqual(response.status_code, 302)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, project_update['name'])


class ProjectDeleteViewTestCase(TestCase):
    """Testing the project delete view."""
    @classmethod
    def setUpTestData(cls):
        for _ in range(3):
            ProjectFactory()

    def setUp(self):
        self.project = Project.objects.last()

    def test_project_confirm_delete(self):
        response = self.client.get(reverse('project:delete', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_confirm_delete.html')
        self.assertEqual(response.context['project'], self.project)

    def test_project_delete(self):
        response = self.client.post(reverse('project:delete', kwargs={'pk': self.project.pk}))
        self.assertEqual(Project.objects.count(), 2)
        self.assertRedirects(response, reverse('project:list'), 302)
