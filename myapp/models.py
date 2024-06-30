from django.db import models

class Summarization(models.Model):
    text = models.TextField()
    summary = models.TextField(default='default summary')

class Audio(models.Model):
    text = models.TextField()
    summary = models.TextField(default='default summary')
    audio = models.FileField(upload_to='audio/')

class PowerPoint(models.Model):
    text=models.TextField()
    file=models.FileField(upload_to='file/')

class Video(models.Model):
    text=models.TextField()
    summary=models.TextField(null=True)
    audio=models.FileField(upload_to='audio/')
    image=models.ImageField(upload_to='image/')
    video=models.FileField(upload_to='video/',default='/home/ahmed/myGraduationProject/myapp/ai/Easy_Wav2Lip/test_audio1_Easy-Wav2Lip.mp4')
    
