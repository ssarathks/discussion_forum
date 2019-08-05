from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import Detailsform,ItemCreateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from accounts.models import Items
# Create your views here.


class IndexView(TemplateView):
    template_name='accounts/account_index.html'

class LandingPageView(TemplateView):
    template_name='accounts/landingpage.html'

class ItemListView(LoginRequiredMixin,ListView):
    login_url='/accounts/login'
    redirect_field_name='accounts/items_list.html'
    model=Items
    context_object_name='items'

    def get_queryset(self):
        return Items.objects.all().order_by('name')

class ItemDetailView(DetailView):
    model=Items
@login_required
def itemCreateView(request):
    if request.method=='POST':
        itemform=ItemCreateForm(request.POST)
        if itemform.is_valid():
            item=itemform.save(commit=False)
            item.user=request.user
            item.save()
            return redirect('accounts:itemlist')
    else:
        itemform=ItemCreateForm()
    return render(request,'accounts/item_createpage.html',context={'itemform':itemform})

def signup(request):
    if request.method == 'POST':
        userform=UserCreationForm(request.POST)
        detailform=Detailsform(request.POST)
        if userform.is_valid() and detailform.is_valid():
            user=userform.save()
            user.save()
            detail=detailform.save(commit=False)
            detail.user=user
            detail.save()
            return redirect('accounts:login')
    else:
        userform=UserCreationForm()
        detailform=Detailsform()
    return render(request,'accounts/signup.html',context={'userform':userform,
                                                            'detailform':detailform})
