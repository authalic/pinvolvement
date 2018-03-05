from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from pubinput.models import PublicComment

# Register your models here.

class PubCommentAdmin(LeafletGeoAdmin):
    list_display = ('comment', 'first_name', 'last_name', 'email', 'phone', 'address1', 'address2', 'city')
    fields = ('comment', ('first_name', 'last_name'), ('email', 'phone'), ('address1', 'address2'), ('city', 'state', 'zipcode'), 'location')

admin.site.register(PublicComment, PubCommentAdmin)
