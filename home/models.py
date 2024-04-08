from django.db import models


class VerificationImage(models.Model):
    image = models.ImageField(upload_to='verification_images')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='verification_images')


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profiles', null=True, blank=True)


class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    sentiment = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)
    caption = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

