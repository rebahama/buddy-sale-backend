from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    content = models.CharField(max_length=2000, blank=False)
    image = models.ImageField(upload_to='images/',
                              default='../default_profile_irrizg_dcehz0',
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.title}'