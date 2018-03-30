from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pubinput import views


app_name = 'pubinput'

urlpatterns = [
   path('comments/', views.CommentList.as_view(), name='commentlist'),
   path('comments/<uuid:pk>', views.CommentView.as_view(), name='commentdetail'),
   path('addcomment', views.CommentCreateOnly.as_view(), name='commentcreateonly'),  #  WHY DOESN'T THIS WORK?????
   path('viewcomments', views.CommentListOnly.as_view(), name='commentviewonly'),
   path('adminview', views.CommentListAdminView.as_view(), name='admincommentview'),
]

# DRF: Returns a URL pattern list which includes format suffix patterns appended to each of the URL patterns provided.
urlpatterns = format_suffix_patterns(urlpatterns)