from django.db import models

from tinymce.models import HTMLField

from clients.validators import PhoneValidator


class Phone(models.Model):
    """Client phone model."""
    class Meta:
        verbose_name = "телефон"
        verbose_name_plural = "телефоны"

    owner = models.CharField(verbose_name="владелец", max_length=150)
    number = models.CharField(
        verbose_name="номер",
        max_length=15,
        unique=True,
        validators=[PhoneValidator]
    )

    def __str__(self):
        return f"{self.owner} <+{self.number}>"


class Email(models.Model):
    """Client email model."""
    class Meta:
        verbose_name = "email"
        verbose_name_plural = "emails"

    owner = models.CharField(verbose_name="владелец", max_length=150)
    address = models.EmailField(verbose_name="адрес электронной почты", unique=True)

    def __str__(self):
        return f"{self.owner} <{self.address}>"


class Company(models.Model):
    """Client company model."""
    class Meta:
        verbose_name = "компания"
        verbose_name_plural = "компании"

    name = models.CharField(verbose_name="название", max_length=150, unique=True)
    contact_person = models.CharField(verbose_name="контактное лицо", max_length=150)
    description = HTMLField(verbose_name="описание")
    address = models.CharField(verbose_name="адрес", max_length=200)
    created = models.DateTimeField(verbose_name="дата создания записи", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="дата изменения записи", auto_now=True)
    phones = models.ManyToManyField(Phone, verbose_name="телефоны", blank=True)
    emails = models.ManyToManyField(Email, verbose_name="адреса электронной почты", blank=True)

    def __str__(self):
        return self.name
