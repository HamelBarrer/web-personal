from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png', upload_to='profiles/')
    biography = models.TextField(default='Esta es mi Biografia :v')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def custom_image(sender, instance, *args, **kwargs):
    if instance.avatar:
        img = Image.open(instance.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(instance.avatar.path)
