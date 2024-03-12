from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# For class Based View
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# Create your views here.

# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form= forms.PostForm(request.POST)
#         if post_form.is_valid():
#             # post_form.cleaned_data['author']= request.user
#             post_form.instance.author= request.user
#             post_form.save()
#             return redirect('add_post')
#     else:
#         post_form= forms.PostForm()
#     return render(request, 'add_post.html', {'form' : post_form})


# Class Based Add Post View
@method_decorator(login_required, name= 'dispatch')
class AddPostView(CreateView):
    model= models.Post
    form_class= forms.PostForm
    success_url=reverse_lazy('add_post')
    template_name= 'add_post.html'
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)


# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id)
#     post_form= forms.PostForm(instance=post)
#     if request.method == 'POST':
#         post_form= forms.PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.instance.author= request.user
#             post_form.save()
#             return redirect('homepage')
#     # else:
#     #     post_form= forms.PostForm(instance=post) # eta thakleo hobe na thakleo hobe.
#     return render(request, 'add_post.html', {'form' : post_form})

# Class Baded Edit Post View
@method_decorator(login_required, name= 'dispatch')
class EditPostView(UpdateView):
    model= models.Post
    form_class= forms.PostForm
    pk_url_kwarg = 'id'
    success_url= reverse_lazy('profile')
    template_name= 'add_post.html'


# @login_required
# def delete_post(request, id):
#     post= models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect('homepage')


# Class Based Delete Post View
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model= models.Post
    success_url= reverse_lazy('profile')
    template_name= 'delete.html'
    pk_url_kwarg= 'id'

class DetailPostView(DetailView):
    model= models.Post
    pk_url_kwarg= 'id'
    template_name= 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data= self.request.POST)
        post= self.get_object()
        if comment_form.is_valid():
            new_comment= comment_form.save(commit= False)
            new_comment.post= post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        post= self.object
        comments=post.comments.all()
        if self.request.method == 'POST':
            comment_form= forms.CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment= comment_form.save(commit=False)
                new_comment.post= post
                new_comment.save()
        else:
            comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context




