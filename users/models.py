from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageFile
from match.models import Propose
from django.urls import reverse



ImageFile.LOAD_TRUNCATED_IMAGES = True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0, related_name='profile')
    name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices = [('male', 'Male'), ('female', 'Female'), ('other', 'Other'),])
    about = models.TextField(max_length=100)
    interestedin = models.CharField(max_length=20, choices = [('male', 'Male'), ('female', 'Female'),])
    city = models.CharField(max_length=50)
    about = models.TextField(max_length=100)
    relationshipstatus = models.CharField(max_length=50, choices=[('single', 'Single'), ('committed', 'Committed'), ],
                                          default='single')
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    def age(self):
        bd = self.dob
        if bd:
            td = date.today()
            return td.year - bd.year - ((td.month, td.day) < (bd.month, bd.day))


    def profile_create_url(self):
        return reverse('profile_create', kwargs={'pk': self.pk})




    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
