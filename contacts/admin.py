from django.contrib import admin
from django.contrib.gis import admin
from contacts.models import Organization, Contact, Subject, Comment

# Register your models here.
admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(Subject, admin.OSMGeoAdmin)
admin.site.register(Comment)
