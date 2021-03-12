from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField

from companies.models import Company


class Project(models.Model):
    """Companies project model."""
    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"

    name = models.CharField(verbose_name="название", max_length=100)
    description = HTMLField(verbose_name="описание")
    start_date = models.DateField(verbose_name="начало")
    end_date = models.DateField(verbose_name="окончание")
    price = models.DecimalField(verbose_name="цена", max_digits=20, decimal_places=2)
    company = models.ForeignKey(Company, verbose_name="компания", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project:detail', kwargs={'pk': self.pk})
