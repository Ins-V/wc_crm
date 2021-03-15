from django.conf import settings
from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField

from projects.models import Project
from companies.models import Company


UserModel = settings.AUTH_USER_MODEL


class Keyword(models.Model):
    """Keyword model."""
    class Meta:
        verbose_name = "ключевое слово"
        verbose_name_plural = "ключевые слова"

    word = models.CharField(verbose_name="слово", max_length=20, unique=True)
    slug = models.SlugField(verbose_name="слаг", max_length=20)

    def __str__(self):
        return self.word


class Interaction(models.Model):
    """Interaction model."""
    class Meta:
        verbose_name = "взаимодействие"
        verbose_name_plural = "взаимодействия"

    CHANNEL_CHOICES = (
        (0, 'Заявка'),
        (1, 'Письмо'),
        (2, 'Сайт'),
        (3, 'Инициатива компании'),
    )

    project = models.ForeignKey(Project, verbose_name="проект", on_delete=models.CASCADE)
    channel = models.PositiveSmallIntegerField(
        verbose_name="канал обращения",
        choices=CHANNEL_CHOICES,
        default=0
    )
    manager = models.ForeignKey(UserModel, verbose_name="менеджер", on_delete=models.CASCADE)
    description = HTMLField(verbose_name="описание")
    evaluation = models.PositiveSmallIntegerField(
        verbose_name="оценка",
        choices=[(i, i) for i in range(1, 6)],
        default=0
    )
    created = models.DateTimeField(verbose_name="дата создания записи", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="дата изменения записи", auto_now=True)
    keywords = models.ManyToManyField(Keyword, verbose_name="ключевые слова", blank=True)

    def __str__(self):
        return f"Взаимодействие с компанией {self.project.company.name} #{self.pk}"

    def get_absolute_url(self):
        return reverse('interaction:detail', kwargs={'pk': self.pk})
