from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist


def file_upload_helper(instance, filename):
    """File upload helper.

    Changes the filename to the username.

    Args:
        instance (User): User instance.
        filename (str): Image name.

    Returns:
        str: Path to image.
    """
    return f"photos/{instance.username}.{filename.split('.')[-1]}"


class User(AbstractUser):
    """Custom user model."""
    photo = models.ImageField(
        verbose_name="фото",
        upload_to=file_upload_helper,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        # If a new image is uploaded, delete the old one.
        try:
            this = User.objects.get(pk=self.pk)

            if this.photo != self.photo:
                this.photo.delete(save=False)
        except ObjectDoesNotExist:
            pass

        super().save(*args, **kwargs)
