from django.urls import path
from . import views


urlpatterns = [
    # views.workflow is the main index page view of the application
    path('', views.workflow, name='index'),

    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('contact/<uuid:pk>', views.ContactDetailView.as_view(), name='contact-detail'),
    path('contact/create', views.ContactCreate.as_view(), name='contact_create'),
    path('contact/<uuid:pk>/update', views.ContactUpdate.as_view(), name='contact_update'),
    path('contact/<uuid:pk>/delete', views.ContactDelete.as_view(), name='contact_delete'),
    path('contact/post', views.ContactCreateOnly.as_view(), name='contactApi_post'),

    path('organizations/', views.OrganizationListView.as_view(), name='organizations'),
    path('organization/<uuid:pk>', views.OrganizationDetailView.as_view(), name='org-detail'),
    path('organization/create', views.OrganizationCreate.as_view(), name='organization_create'),
    path('organization/<uuid:pk>/update', views.OrganizationUpdate.as_view(), name='organization_update'),
    path('organization/<uuid:pk>/delete', views.OrganizationDelete.as_view(), name='organization_delete'),

    path('comments/', views.CommentListView.as_view(), name='comments'),
    path('comment/<uuid:pk>', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comment/<uuid:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),

    # use view functions to create or update new Comment objects using Bootstrap
    path('comment/create', views.comment_create_view, name='comment_create'), 
    path('comment/<uuid:pk>/update', views.comment_update_view, name='comment_update'),


    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subject/<uuid:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
    
    # use view functions to create or update new Subject objects using Leaflet widget
    path('subject/create', views.subject_create_view, name='subject_create'),
    path('subject/<uuid:pk>/update', views.subject_update_view, name='subject_update'),

    # use the generic view to delete
    path('subject/<uuid:pk>/delete', views.SubjectDelete.as_view(), name='subject_delete'),

]
