from django.db import models

# Create your models here.
class Contact(models.Model):
  full_name = models.CharField("Full Name", max_length=50, blank=False, null=False)
  email = models.EmailField("Email", max_length=50, blank=False, null=False)
  subject = models.CharField("Subject", max_length=50, blank=False, null=False)
  message = models.TextField("Message", blank=False, null=False)
  created_at = models.DateTimeField("Created At", auto_now_add=True)

  def __str__(self):
    return f'{self.full_name} wants to connect regarding {self.subject}'  