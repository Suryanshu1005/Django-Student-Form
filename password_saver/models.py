from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length = 100, null = False)
    idNum = models.CharField(max_length = 100, null = False)
    address = models.CharField(max_length = 100, null = False)
    dept = models.CharField(max_length = 100, null = False)

    def __str__(self):
        return(self.name)

        def _get_absolute_url(self):
            return reverse('student_edit', kwargs = {'pk':self.pk})
