from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods
from .forms import SubjectForm
from .models import Organization, Contact, Subject, Comment


# Create your views here.

@login_required
def index(request):
    '''
    View function for the home page of site
    '''
    # Send all of the current Subject points to the main page

    subjects = Subject.objects.all()


    # Generate counts of some of the main objects
    num_org = Organization.objects.count()
    num_contact = Contact.objects.count()
    num_subject = Subject.objects.count()
    num_comment = Comment.objects.count()

    return render(
        request,
        'contacts/index.html',
        context={
            'subjects': subjects,
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


class ContactListView(LoginRequiredMixin, generic.ListView):
    model = Contact
    paginate_by = 10


class OrganizationListView(LoginRequiredMixin, generic.ListView):
    model = Organization


class SubjectListView(LoginRequiredMixin, generic.ListView):
    model = Subject
    paginate_by = 10


class CommentListView(LoginRequiredMixin, generic.ListView):
    model = Comment
    paginate_by = 20


class ContactDetailView(LoginRequiredMixin, generic.DetailView):
    model = Contact


class OrganizationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Organization


class CommentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Comment


# Generic Editing Views
# template for Create and Update views are located by default at: 
#   /templates/contacts/[modelname]_form.html
# template for Delete view is at: 
#   /templates/contacts/[modelname]_confirm_delete.html

# Note: There may not be enough flexibility in these Generic views to format the
#       forms in an attractive way


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = '__all__'


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = '__all__'


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts')


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = '__all__'


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = '__all__'


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('comments')


class OrganizationCreate(LoginRequiredMixin, CreateView):
    model = Organization
    fields = '__all__'


class OrganizationUpdate(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = '__all__'


class OrganizationDelete(LoginRequiredMixin, DeleteView):
    model = Organization
    success_url = reverse_lazy('organizations')


class SubjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Subject


class SubjectDelete(LoginRequiredMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects')



# NOTE:
# the Create and Update Subject forms require the Leaflet widget and cannot be created as generic views

@login_required
def subject_update_view(request, pk):

    subject = get_object_or_404(Subject, pk=pk)

    template = 'contacts/subject_form.html'

    if request.method == 'POST':

        form = SubjectForm(request.POST, instance=subject)
        
        if form.is_valid():
            form.save()

            return redirect('subject-detail', pk=subject.pk)
    else:
        form = SubjectForm(instance=subject)

    return render(request, template, {'form': form})


@login_required
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

    else:
        print('Error, form invalid') #testing purposes 

    return render(request, template, {'form': form})


