from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings   # to access the current logged-in User object: settings.AUTH_USER_MODEL
from django.urls import reverse
import uuid

# Create your models here.

class PublicComment(models.Model):
    '''
    Class representing a comment submitted by a member of the public
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.CharField("Comment", max_length=500, blank=False)
    first_name = models.CharField("First Name", max_length=24, blank=True)
    last_name = models.CharField("Last Name", max_length=50, blank=True)
    email = models.EmailField("Email Address", max_length=80, blank=True)
    phone = models.CharField("Phone", max_length=12, blank=True, help_text="Phone: xxx-xxx-xxxx")
    address1 = models.CharField("Address 1", max_length=60, blank=True)
    address2 = models.CharField("Address 2", max_length=24, blank=True)
    city = models.CharField("City", max_length=40, blank=True)
    state = models.CharField("State", max_length=2, blank=True, default="UT")
    zipcode = models.CharField("ZIP", max_length=10, blank=True)
    submitted = models.DateTimeField('Submitted', auto_now_add=True)  #stores the time and date this Comment was created
    location = models.PointField('Point Location', srid=4326, null=True)
    bcookie = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    
    class Meta:
        ordering = ["-submitted"]

    def __str__(self):
        return self.first_name +" " + self.last_name

    