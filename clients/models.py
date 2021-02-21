from django.db import models

from tinymce.models import HTMLField


class Company(models.Model):
    """Client company model."""
    class Meta:
        verbose_name = "компания"
        verbose_name_plural = "компании"

    name = models.CharField(verbose_name="название", max_length=150, blank=False)
    contact_person = models.CharField(verbose_name="контактное лицо", max_length=150, blank=False)
    description = HTMLField(verbose_name="описание", blank=False)
    address = models.CharField(verbose_name="адрес", max_length=200, blank=False)
    created = models.DateTimeField(verbose_name="дата создания записи", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="дата изменения записи", auto_now=True)

    def __str__(self):
        return self.name
