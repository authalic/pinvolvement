from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from contacts.models import Organization, Contact, Subject, Comment

# Define admin classes here
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'textnote', 'organization', 'org_title', 'address1', 'address2', 'city', 'state', 'zipcode','created')
    fields = (('first_name', 'last_name'), 'textnote', ('org_title', 'organization'), ('address1', 'address2'), ('city', 'state', 'zipcode'))
    

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'org_address1', 'org_address2', 'org_city', 'org_state', 'org_zipcode')
    fields = (('org_name'), ('org_address1', 'org_address2'), ('org_city', 'org_state', 'org_zipcode'))


class CommentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'contact', 'employee', 'direction', 'method', 'comment_datetime', 'commentxt', 'attachment')
    fields = ('subject', ('contact', 'employee'), ('direction', 'method'), 'comment_datetime', 'commentxt', 'attachment')


# Extend LeafletGeoAdmin for leaflet map window
class SubjectAdmin(LeafletGeoAdmin):
    list_display = ('summary', 'employee', 'contact', 'initial_date', 'last_activity', 'coordinates')
    fields = ('summary', ('contact', 'employee'), 'initial_date', 'coordinates')



# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subject, SubjectAdmin)  # can't seem to include SubjectAdmin here... research needed
admin.site.register(Comment, CommentAdmin)
