import datetime

import factory.fuzzy

from projects.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    """Project factory."""
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: f"Project {n}")
    description = factory.Faker('paragraph')
    start_date = factory.fuzzy.FuzzyDate(
        datetime.date(2020, 1, 1),
        datetime.date(2021, 1, 1)
    )
    end_date = factory.LazyAttribute(
        lambda o: o.start_date + datetime.timedelta(days=5)
    )
    price = factory.fuzzy.FuzzyDecimal(10000)
    company = factory.SubFactory('companies.tests.factories.CompanyFactory')
