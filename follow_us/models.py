from django.db import models

# Create your models here.
class FollowUs(models.Model):
    platform = models.CharField(max_length=50)
    platform_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Follow Us Links"

    def __str__(self):
        return self.platform