from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods
from .forms import SubjectForm, CommentForm, ContactForm
from .models import Organization, Contact, Subject, Comment


def workflow(request):
    '''
    View for developing and testing the Workflow form. Ultimately will replace the index view
    '''
    contact_form = ContactForm(prefix="contact")
    subject_form = SubjectForm(prefix="contact")
    comment_form = CommentForm(prefix="comment")

    if request.method == 'POST':

        contact_form = ContactForm(request.POST, prefix="contact")
        subject_form = SubjectForm(request.POST, prefix="contact")
        comment_form = CommentForm(request.POST, prefix="comment")

        if all([contact_form.is_valid(), subject_form.is_valid(), comment_form.is_valid()]):

            # should each model be tested to see if an object currently exists?
            # Look at the specific actions behind the .save() method
            #   does it create a new object if one exists?
            #   does it overwrite fields if some or none have changed?

            # Here is where the individual forms are saved and committed
            # There is a specific order that needs to be followed:

            # subject_form.save(commit=False)
            # subject_form.contact = contact_form.save()
            # subject_form.save()
            # comment_form.save(commit=False)
            # comment_form.subject = subject_form
            # comment_form.save()






    context = {
        'contact_form': ContactForm(prefix="contact"),
        'subject_form': SubjectForm(prefix="subject"),
        'comment_form': CommentForm(prefix="comment"),
    }

    return render(request, 'contacts/index.html', context)


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

    context = {
        'subjects': subjects,
        'num_org': num_org,
        'num_contact': num_contact,
        'num_subject': num_subject,
        'num_comment': num_comment,
    }

    return render(request, 'contacts/index.html', context)


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
    paginate_by = 10


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


# Forms  NOTE:
# the Create and Update Subject forms require the Leaflet widget and cannot be created as generic views
# the Create and Update Comment forms require more Bootstrap styling than generic views


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
        print('Render empty unbound form') #testing purposes

    return render(request, template, {'form': form})


@login_required
def comment_update_view(request, pk):

    comment = get_object_or_404(Comment, pk=pk)

    template = 'contacts/comment_form.html'

    if request.method == 'POST':

        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()

            return redirect('comment-detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, template, {'form': form})


@login_required
def comment_create_view(request):
    form = CommentForm()
    template = 'contacts/comment_form.html'

    if request.method == 'POST':

        form = CommentForm(request.POST)

        # check whether it's valid
        if form.is_valid():
            form.save(commit=True)

            # redirect to a new URL
            return HttpResponseRedirect(reverse('comments'))

    else:
        print('Render empty unbound form') #testing purposes 

    return render(request, template, {'form': form})
