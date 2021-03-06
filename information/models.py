from django.db import models
from people.models import Students, Teachers
from university_structure.models import Groups
from departments.models import Subjects

# Create your models here.


class StartYears(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=False)


class Terms(models.Model):
    id = models.AutoField(primary_key=True)
    start_year_id = models.ForeignKey(StartYears, on_delete=models.CASCADE, null=False)
    number = models.IntegerField(null=False)


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)


class ControlTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)


class Records(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=False)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, null=False)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=False)
    term_id = models.ForeignKey(Terms, on_delete=models.CASCADE, null=False)
    control_type_id = models.ForeignKey(ControlTypes, on_delete=models.CASCADE, null=False)
    mark_id = models.ForeignKey(Marks, on_delete=models.CASCADE, null=False)
    datetime = models.DateTimeField(null=False, default=None)
    retake_count = models.SmallIntegerField(null=False, default=0)
