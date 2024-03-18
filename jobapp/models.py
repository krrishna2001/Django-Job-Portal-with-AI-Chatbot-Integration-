from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from jobapp.validators import validate_file_size
import cv2
import numpy as np
User = get_user_model()


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_description = RichTextField(blank=True, null=True)
    url = models.URLField(max_length=200)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

 

class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title


  

class BookmarkJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title 

class Application(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/', validators=[validate_file_size])
    apply_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.applicant.get_full_name()} applied for {self.job.title}'
class VideoInterview(models.Model):
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    interviewee = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='video_interviews/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.interviewer.username} interviewed {self.interviewee.user.username}"


class FaceDetection:
    def detect_faces(self, image):
        face_cascade = cv2.C