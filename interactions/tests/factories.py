import factory

from django.conf import settings

from interactions.models import Interaction


class UserFactory(factory.django.DjangoModelFactory):
    """User factory."""
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: f"Username_{n}")
    password = factory.PostGenerationMethodCall('set_password', 'password')


class InteractionFactory(factory.django.DjangoModelFactory):
    """Interaction factory."""
    class Meta:
        model = Interaction

    project = factory.SubFactory('projects.tests.factories.ProjectFactory')
    company = factory.SubFactory('companies.tests.factories.CompanyFactory')
    channel = factory.Faker(
        'random_element', elements=[x[0] for x in Interaction.CHANNEL_CHOICES]
    )
    manager = factory.SubFactory(UserFactory)
    description = factory.Faker('paragraph')
    evaluation = factory.Faker(
        'random_element', elements=[x for x in range(1, 6)]
    )
