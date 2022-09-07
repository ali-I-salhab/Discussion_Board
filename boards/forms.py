from dataclasses import fields
from email import message
from pyexpat import model
from django import forms
from .models import Topic
# we create an form to use it in Newtopic.html 
# this form contain two fields

class NewTopicForm(forms.ModelForm):
   
   
    message=forms.CharField(
        help_text="the max length is 400",widget=forms.Textarea
        (attrs={'rows':"5",'placeholder':"here message"}),max_length=4000)
    
    
    class Meta:

        model=Topic
        fields=['subject','message']
