from typing import Any
from django.shortcuts import render,redirect, get_object_or_404
from . import forms
from . import models
from django.views.generic.detail import DetailView

# Create your views here.
class CarDetail(DetailView):
    model= models.Car
    pk_url_kwarg= 'pk'
    template_name= 'car_detail.html'

    def post(self, request, *args, **kwargs):
        comment_form= forms.CommentForm(data= self.request.POST)
        car= self.get_object()
        if comment_form.is_valid():
            new_comment= comment_form.save(commit= False)
            new_comment.car= car
            new_comment.save()
            return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        car= self.object
        comments= car.comments.all()

        if self.request.method == 'POST':
            comment_form= forms.CommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment= comment_form.save(commit=False)
                new_comment.car= car
                new_comment.save()
        else:
            comment_form = forms.CommentForm()
        
        context["comments"] = comments
        context["comment_form"] = comment_form

        return context
    
def update_quantity(request, pk):
    car = get_object_or_404(models.Car, pk=pk)
    car.quantity -= 1
    car.buyers.add(request.user)
    car.save()
    return redirect("profile")