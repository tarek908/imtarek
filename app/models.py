'''
Models.

1. Testimonial
	i. description
	ii. name
	ii. title
	iv. image

2. Projects.
	i. Projects name
	ii. title
	iii. cover img
	iv. descriptions
	v. demo link

'''


from django.db import models

# Create your models here.
class subscribe(models.Model):
    email = models.EmailField(default="")
    date = models.DateTimeField(auto_now_add=True)

#// Testimonial
class testimonials(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="app/testimonal")
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)

#// Projects
class projects(models.Model):
    proName = models.CharField(max_length=200)
    proTitle = models.CharField(max_length=500)
    cover = models.ImageField(upload_to="app/projects")
    description = models.TextField(default="")
    live = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)