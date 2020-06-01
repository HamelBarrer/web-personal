import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from users.models import User


class Commentarie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='commentaries/', null=True, blank=True)
    slug = models.SlugField(max_length=100, null=False,
                            blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=Commentarie)
def edit_text(sender, instance, *args, **kwargs):
    if instance.title and instance.description:
        instance.title = instance.title.capitalize()
        instance.description = instance.description.capitalize()


@receiver(pre_save, sender=Commentarie)
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
        while Commentarie.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.title}-{str(uuid.uuid4())[:8]}'
            )
        instance.slug = slug
