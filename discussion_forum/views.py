from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from discussion_forum.forms import CommentForm,ThreadForm
from discussion_forum.models import Comments,Thread

# Create your views here.


class ThreadListView(LoginRequiredMixin,ListView):
    template_name='discussion_forum/discussion_index.html'
    login_url='/accounts/login'
    redirect_field_name='discussion_forum/discussion_index.html'
    model=Thread
    context_object_name='threads'
class ThreadDetailView(LoginRequiredMixin,DetailView):
    model=Thread

@login_required
def create_thread(request):
    if request.method=='POST':
        threadform=ThreadForm(request.POST)
        if threadform.is_valid():
            thread=threadform.save(commit=False)
            thread.user=request.user
            thread.save()
            return redirect('discussion_forum:discussion_homepage')
    else:
        threadform=ThreadForm()
    return render(request,'discussion_forum/create_thread.html',context={'threadform':threadform})

@login_required
def create_comment(request,pk):
    thread=get_object_or_404(Thread,pk=pk)
    if request.method=='POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            comment=commentform.save(commit=False)
            comment.thread=thread
            comment.save()
            return redirect('discussion_forum:thread_detail',pk=thread.pk)
    else:
        commentform=CommentForm()
    return render(request,'discussion_forum/create_comment.html',context={'commentform':commentform})
