from django.db import models
import uuid


class user(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.fname + " " + self.lname


class report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    context = models.CharField(max_length=100)
    submit_date = models.DateField(null=True, blank=True)
    ANSWER_STATUS = (
        ('P', 'Positive'),
        ('N', 'Negative'),
        ('U', 'Unknown'),
    )
    status = models.CharField(max_length=1, choices=ANSWER_STATUS, blank=True, default='U', help_text='Report response')
    user = models.ForeignKey('user', on_delete=models.SET_NULL, null=True)
