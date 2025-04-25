from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('merchant', 'Merchant'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')



class AudioJournal(models.Model):
    CATEGORY_CHOICES = [
        ('secular', 'Secular'),
        ('gospel', 'Gospel'),
    ]
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio_journals/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImageUpload(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='creator_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    audio_journal = models.ForeignKey(AudioJournal, on_delete=models.CASCADE, null=True, blank=True)
    image_upload = models.ForeignKey(ImageUpload, on_delete=models.CASCADE, null=True, blank=True)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.audio_journal:
            return f"{self.customer.username} purchased audio: {self.audio_journal.title}"
        elif self.image_upload:
            return f"{self.customer.username} purchased image: {self.image_upload.title}"
        return f"{self.customer.username} made a purchase"
