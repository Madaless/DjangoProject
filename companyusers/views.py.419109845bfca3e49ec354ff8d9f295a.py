from django.shortcuts import render, redirect
from .forms import (CompanyRegisterForm, CompanyAddOfferForm, CompanyUpdateForm)
from django.contrib import messages
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
#from ..jobservice.models import JobOffer
from jobservice.models import JobOffer
from .decorators import (company_required, person_required)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.urls import reverse


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CompanyRegisterForm()
    return render(request, 'companyusers/register.html', {'form': form})

def signup(request):
    return render(request,'companyusers/signup.html',{'title':'signup'})

class OfferListView(ListView):
    model = JobOffer
    template_name = 'jobservice/home.html'
    context_object_name = 'joboffers'
    ordering = ['-postdate']
    paginate_by = 10

class OfferDetailView(DetailView):
    model = JobOffer
    template_name = 'jobservice/offer.html'
    context_object_name = 'joboffers'

@method_decorator([login_required, company_required], name='dispatch')
class OfferCreateView(LoginRequiredMixin, CreateView):
    model = JobOffer
    fields = ['title', 'industry', 'proffesion' ,'jobPosition', 'jobType', 'ExperienceLevel', 'postdate', 'location', 'jobDescription','salary' ]
    template_name = 'companyusers/createoffer_form.html'
    context_object_name = 'joboffers'
    def form_valid(self, form):
        form.instance.companyName = self.request.user.company
        return super().form_valid(form)

@method_decorator([login_required, company_required], name='dispatch')
class OfferUpdateView(UpdateView):
    model = JobOffer
    fields = ['title', 'industry', 'proffesion' ,'jobPosition', 'jobType', 'ExperienceLevel', 'postdate', 'location', 'jobDescription','salary' ]
    template_name = 'companyusers/createoffer_form.html'
    context_object_name = 'joboffers'

@method_decorator([login_required, company_required], name='dispatch')
class OfferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobOffer
    template_name = 'companyusers/offer_confirm_delete.html'
    context_object_name = 'joboffers'
    success_url = '/'

    def test_func(self):
        JobOffer = self.get_object()
        if self.request.user == JobOffer.companyName:
            return True
        return False

@login_required
@company_required
def editcompany(request):
    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, instance=request.user.company)

        if form.is_valid():
            form.save()
            return redirect(reverse('profilecompany'))
    else:
        form = CompanyUpdateForm(instance=request.user.company)
        args = {'form': form}
        return render(request, 'companyusers/editcompany.html', args)


 


