from random import randint

import factory

from companies.models import Phone, Email, Company


class PhoneFactory(factory.django.DjangoModelFactory):
    """Client phone factory."""
    class Meta:
        model = Phone

    owner = factory.Faker('name')
    number = factory.Sequence(lambda n: ''.join([str(randint(0, 9)) for _ in range(0, 12)]))


class EmailFactory(factory.django.DjangoModelFactory):
    """Client email factory."""
    class Meta:
        model = Email

    owner = factory.Faker('name')
    address = factory.Faker('email')


class CompanyFactory(factory.django.DjangoModelFactory):
    """Company factory."""
    class Meta:
        model = Company

    name = factory.Sequence(lambda n: f"Company {n}")
    contact_person = factory.Faker('name')
    description = factory.Faker('paragraph')
    address = factory.Faker('address')
