from django.test import TestCase
from django.urls import reverse

from interactions.models import Interaction
from interactions.tests.factories import InteractionFactory


class InteractionModelTestCase(TestCase):
    """Testing the interaction model class."""
    def test_create_interaction(self):
        interaction_from_factory = InteractionFactory()
        interaction_from_db = Interaction.objects.first()

        self.assertEqual(Interaction.objects.count(), 1)
        self.assertEqual(interaction_from_factory.project, interaction_from_db.project)
        self.assertEqual(interaction_from_factory.company, interaction_from_db.company)
        self.assertEqual(interaction_from_factory.channel, interaction_from_db.channel)
        self.assertEqual(interaction_from_factory.manager, interaction_from_db.manager)
        self.assertEqual(interaction_from_factory.description, interaction_from_db.description)
        self.assertEqual(interaction_from_factory.evaluation, interaction_from_db.evaluation)
        self.assertEqual(
            reverse('interaction:detail', kwargs={'pk': interaction_from_factory.pk}),
            interaction_from_db.get_absolute_url()
        )
        self.assertEqual(
            f"Взаимодействие с компанией {interaction_from_factory.company.name} #{interaction_from_factory.pk}",
            interaction_from_db.__str__()
        )
