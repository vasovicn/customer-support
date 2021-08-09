from django.db import models


# Create your models here.

class Ticket(models.Model):
    submitted_date_and_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    name=models.TextField()
    number=models.TextField()
    company=models.TextField()
    email=models.TextField()
    subject=models.TextField()
    problem=models.TextField()
    date_and_time_for_callback=models.DateTimeField(blank=True, null=True)
    comment=models.TextField(blank=True, null=True)
    archive = models.BooleanField(default=False)
    class Meta:
        ordering = ['date_and_time_for_callback', 'submitted_date_and_time']

    def __str__(self):
        return self.subject

