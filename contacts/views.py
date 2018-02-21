from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SubjectForm
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


# Generic Editing Views
# template for Create and Update views are located by default at: 
#   /templates/contacts/[modelname]_form.html
# template for Delete view is at: 
#   /templates/contacts/[modelname]_confirm_delete.html

# Note: There may not be enough flexibility in these Generic views to format the
#       forms in an attractive way


class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'


class ContactUpdate(UpdateView):
    model = Contact
    fields = '__all__'


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts')


class CommentCreate(CreateView):
    model = Comment
    fields = '__all__'


class CommentUpdate(UpdateView):
    model = Comment
    fields = '__all__'


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comments')


class OrganizationCreate(CreateView):
    model = Organization
    fields = '__all__'


class OrganizationUpdate(UpdateView):
    model = Organization
    fields = '__all__'


class OrganizationDelete(DeleteView):
    model = Organization
    success_url = reverse_lazy('organizations')


# NOTE:
# the Create and Update Subject forms require the Leaflet widget
# and cannot be created as generic views

def subject_update_view(request, pk):

    subject = get_object_or_404(Subject, pk=pk)

    form = SubjectForm(instance=subject)
    template = 'contacts/subject_form.html'


    return render(request, template, {'form': form})


def subject_create_view(request):
    form = SubjectForm()
    template = 'contacts/subject_form.html'

    if request.method == 'POST':

        form = SubjectForm(request.POST)

        # check whether it's valid
        if form.is_valid():
            form.save(commit=True)

            # redirect to a new URL
            return HttpResponseRedirect(reverse('subjects'))

    # if request is GET or anything else, create a blank form
    
    else:
        print('Error, form invalid') #testing purposes 

    return render(request, template, {'form': form})




class SubjectDelete(DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects')

