from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings   # to access the current logged-in User object: settings.AUTH_USER_MODEL
from django.urls import reverse
import uuid

# NOTE:  setting the default User to settings.AUTH_USER_MODEL seems not to work

class Organization(models.Model):
    '''
    Class representing Organizations to which Contacts may belong
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_name = models.CharField("Organization Name", max_length=80, blank=False)
    org_address1 = models.CharField("Address1", max_length=60, blank=True)
    org_address2 = models.CharField("Address2", max_length=24, blank=True)
    org_city = models.CharField("City", max_length=40, blank=True)
    org_state = models.CharField("State", max_length=2, blank=True, default="UT")
    org_zipcode = models.CharField("ZIP", max_length=10, blank=True)
    org_phone = models.CharField("Phone", max_length=12, blank=True, help_text="Phone: xxx-xxx-xxxx")

    class Meta:
            ordering = ["org_name"]

    def get_members(self):
        return Contact.objects.filter(organization=self.pk).order_by('last_name', 'first_name')

    def get_absolute_url(self):
        return reverse('org-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.org_name


class Contact(models.Model):  # AKA:  Person
    '''
    Class representing an individual person with whom contact has been made on
    this project Address, Phone, Email information are attached to this person,
    not necessarily the location of the incident or the resident at that location.
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField("First Name", max_length=24, blank=True)
    last_name = models.CharField("Last Name", max_length=50, blank=True)
    textnote = models.CharField("Note", max_length=120, blank=True)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, blank=True, null=True, related_name='members')
    org_title = models.CharField("Title", max_length=40, blank=True)
    email = models.EmailField("Email Address", max_length=80, blank=True)
    phone = models.CharField("Phone", max_length=12, blank=True, help_text="Phone: xxx-xxx-xxxx")
    address1 = models.CharField("Address 1", max_length=60, blank=True)
    address2 = models.CharField("Address 2", max_length=24, blank=True)
    city = models.CharField("City", max_length=40, blank=True)
    state = models.CharField("State", max_length=2, blank=True, default="UT")
    zipcode = models.CharField("ZIP", max_length=10, blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)  #stores the time and date this Contact was created

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_comments(self):
        return Comment.objects.filter(contact=self.pk)
    
    def get_subjects(self):  # this isn't working correctly. Returning incomplete lists???
        return Subject.objects.filter(contact=self.pk)

    def get_absolute_url(self):
        return reverse('contact-detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Subject(models.Model):  # AKA: Topic
    '''
    The description and location of an issue reported by a Contact.
    Subjects are linked to the Contact who initiated the issue.
    Subjects are attached to points on a map.  There are no pointless subjects.
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    summary = models.CharField(max_length=60)
    employee = models.ForeignKey(User, on_delete=models.PROTECT)
    contact = models.ForeignKey('Contact', on_delete=models.PROTECT, blank=True, null=True)
    initial_date = models.DateTimeField('Start Date', editable=True, default=timezone.now)
    last_activity = models.DateTimeField('Last Activity', editable=False, auto_now=True)
    coordinates = models.PointField('Point Location', srid=4326, null=True)

    class Meta:
        ordering = ["-initial_date"]

    def get_absolute_url(self):
        return reverse('subject-detail', args=[str(self.id)])
    
    def lon(self):
        pointLocation = GEOSGeometry(self.coordinates)
        return pointLocation[0]

    def lat(self):
        pointLocation = GEOSGeometry(self.coordinates)
        return pointLocation[1]

    def get_comments(self):
        return Comment.objects.filter(subject=self.pk)

    def get_contacts(self):
        return Contact.objects.filter(contact=self.contact).distinct()
    
    def __str__(self):
        return self.summary


class Comment(models.Model):  # AKA:  Interaction
    '''
    Class representing the single comments attached to a Subject
    to/from one Contact to/from a Employee
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact = models.ForeignKey('Contact', on_delete=models.PROTECT, help_text="Individual who contacted PI")
    employee = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True) # stores the time the comment was created (not editable)
    comment_datetime = models.DateTimeField(default=timezone.now, editable=True) # editable datetime to allow user to backdate
    subject = models.ForeignKey('Subject', blank=True, null=True, on_delete=models.PROTECT)
    commentxt = models.TextField('Comment Summary')
    followup = models.BooleanField(default=False)
    attachment = models.FileField('Attachment', upload_to='contacts/', null=True, blank=True) # attach photos, flyers, random files

    DIRECTION_CHOICES = [
        ('in', 'Incoming'),
        ('out', 'Outgoing')
    ]
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES)

    METHOD_CHOICES = [
        ('phone', 'Phone Conversation'),
        ('email', 'Email Correspondence'),
        ('person', 'In-Person Conversation'),
        ('web', 'Submitted on Web Form'),
    ]
    method = models.CharField(max_length=6, choices=METHOD_CHOICES)

    class Meta:
        ordering = ["-comment_datetime"]

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])
        
    def __str__(self):
        return '%s: %s' % (self.contact, self.subject)

    # helper function for styling the back-and-forth Comments in a Subject
    def is_incoming(self):
        if self.direction == 'in':
            return True
        else:
            return False

