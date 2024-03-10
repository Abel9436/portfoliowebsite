from django.db import models

# Create your models here.
class Skill(models.Model):

    Skill_name=models.CharField( max_length=50)
    skill_level=models.IntegerField()

    class Meta:
        
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.Skill_name

class Project(models.Model):
    class Meta:
        verbose_name_plural = "Projects"
    
    project_name=models.CharField(max_length=50)
    project_description=models.TextField()
    project_image=models.ImageField(default='fallback.png',blank=True)
    
    def __str__(self):
        return self.project_name
class ClientMassage(models.Model):
    sender_name=models.CharField(max_length=50)
    sender_email=models.CharField(max_length=50)
    subject=models.CharField( max_length=70)
    massage=models.CharField(default='',max_length=1000)
    
    def __str__(self):
        return self.sender_name
    
        
