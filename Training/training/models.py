from django.db import models

# Create your models here.
class Fresher(models.Model):

    employee_id = models.CharField(

        max_length=20,

        unique=True

    )

    name = models.CharField(

        max_length=100

    )

    email = models.EmailField()

    phone = models.CharField(

        max_length=15

    )

    technology = models.CharField(

        max_length=50

    )

    batch = models.CharField(

        max_length=50

    )

    joining_date = models.DateField()


    def __str__(self):

        return self.name



# Daily Progress Table

class DailyProgress(models.Model):

    fresher = models.ForeignKey(

        Fresher,

        on_delete=models.CASCADE

    )

    date = models.DateField()

    topic = models.CharField(

        max_length=200

    )

    hours = models.IntegerField()

    tasks = models.TextField()

    challenges = models.TextField(

        blank=True

    )


    def __str__(self):

        return self.topic



# Assignment Table

class Assignment(models.Model):

    fresher = models.ForeignKey(

        Fresher,

        on_delete=models.CASCADE

    )

    assignment_name = models.CharField(

        max_length=200

    )

    github_link = models.URLField(

        blank=True

    )

    status = models.CharField(

        max_length=30

    )


    def __str__(self):

        return self.assignment_name



# Project Table

class Project(models.Model):

    fresher = models.ForeignKey(

        Fresher,

        on_delete=models.CASCADE

    )

    project_name = models.CharField(

        max_length=200

    )

    technology = models.CharField(

        max_length=100

    )

    progress = models.IntegerField()

    github_link = models.URLField(

        blank=True

    )


    def __str__(self):

        return self.project_name