from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('organizations/', views.OrganizationListView.as_view(), name='organizations'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('comments/', views.CommentListView.as_view(), name='comments'),
    path('contact/<int:pk>', views.ContactDetailView.as_view(), name='contact-detail'),
    path('organization/<int:pk>', views.OrganizationDetailView.as_view(), name='org-detail'),
    path('subject/<int:pk>', view.SubjectDetailView.as_view(), name='subject-detail'),
    path('comment/<int:pk>', view.CommentDetailView.as_view(), name='comment-detail'),
]