from django.test import TestCase
from django.urls import reverse

from projects.models import Project
from projects.tests.factories import ProjectFactory


class ProjectModelTestCase(TestCase):
    """Testing the project model class."""
    def test_create_project(self):
        project_from_factory = ProjectFactory()
        project_from_db = Project.objects.first()

        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(project_from_factory.name, project_from_db.name)
        self.assertEqual(project_from_factory.description, project_from_db.description)
        self.assertEqual(project_from_factory.start_date, project_from_db.start_date)
        self.assertEqual(project_from_factory.end_date, project_from_db.end_date)
        self.assertEqual(project_from_factory.price, project_from_db.price)
        self.assertEqual(project_from_factory.company, project_from_db.company)
        self.assertEqual(project_from_factory.name, project_from_db.__str__())
        self.assertEqual(
            reverse('project:detail', kwargs={'pk': project_from_factory.pk}),
            project_from_db.get_absolute_url()
        )
