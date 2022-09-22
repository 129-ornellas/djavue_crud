from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    color = models.TextField(max_length=400)

    def projects(self):
       return {
           'name': self.name,
           'color': self.color,
       }
    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def users(self):
       return {
           'name': self.name,
           'username': self.username,
           'email': self.email,
       }
    def __str__(self):
        return self.name

class Tasks (models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.DateField()
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, default='1')
    
    def tasks(self):
       return {
           'title': self.title,
           'project': self.project,
           'status': self.status,
           'date': self.date,
       }
    def __str__(self):
        return self.title



