from django.shortcuts import render
from django.views import generic
from .models import Organization, Contact, Subject, Comment

# Create your views here.


def index(request):
    '''
    View function for the home page of site
    '''

    # Generate counts of some of the main objects
    num_org = Organization.objects.count()
    num_contact = Contact.objects.count()
    num_subject = Subject.objects.count()
    num_comment = Comment.objects.count()

    return render(
        request,
        'contacts/index.html',
        context={
            'num_org': num_org,
            'num_contact': num_contact,
            'num_subject': num_subject,
            'num_comment': num_comment,
        }
    )


# Generic CBVs
# templates are set by default in the CBVs at: 
#   /templates/contacts/[modelname]_list.html
#   /templates/contacts/[modelname]_detail.html


class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 10


class OrganizationListView(generic.ListView):
    model = Organization


class SubjectListView(generic.ListView):
    model = Subject
    paginate_by = 10


class CommentListView(generic.ListView):
    model = Comment
    paginate_by = 20


class ContactDetailView(generic.DetailView):
    model = Contact


class OrganizationDetailView(generic.DetailView):
    model = Organization


class SubjectDetailView(generic.DetailView):
    model = Subject


class CommentDetailView(generic.DetailView):
    model = Comment
