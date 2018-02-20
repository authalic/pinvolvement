from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from contacts.models import Organization, Contact, Subject, Comment

# Define admin classes here
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'textnote', 'organization', 'address1', 'address2', 'city', 'state', 'zipcode','created')
    fields = (('first_name', 'last_name'), 'textnote', 'organization', ('address1', 'address2'), ('city', 'state', 'zipcode'))
    

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'org_address1', 'org_address2', 'org_city', 'org_state', 'org_zipcode')
    fields = (('org_name'), ('org_address1', 'org_address2'), ('org_city', 'org_state', 'org_zipcode'))


# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('summary', 'employee', 'contact', 'initial_date', 'last_activity', 'coordinates')
#     fields = ('summary', ('contact', 'employee'), 'initial-date', 'last_activity', 'coordinates')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'contact', 'employee', 'comment_datetime', 'commentxt', 'attachment')
    fields = ('subject', ('contact', 'employee'), 'comment_datetime', 'commentxt', 'attachment')





# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subject, LeafletGeoAdmin)  # can't seem to include SubjectAdmin here... research needed
admin.site.register(Comment, CommentAdmin)
