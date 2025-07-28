from django import forms
from .models import PasswordManager

class PasswordManagerForm(forms.ModelForm):
    class Meta:
        model=PasswordManager
        fields=["name","url","password"]
        widgets={
            "name":forms.TextInput(attrs={
                "class":"input input-warning focus:outline-none",
                'placeholder':"WebSite's Name",
                "required":'true'
            }),
            "url":forms.TextInput(
                attrs={
                    'class':'input input-warning focus:outline-none',
                    "placeholder":"Paste site's URL here...",
                    "required":'true'
                }
            ),
            "password": forms.TextInput(
                attrs={
                    "class":"input input-warning focus:outline-none w-full password",
                    "placeholder":'Click on the button down to generate password..👉👉',
                    "readonly": 'true',
                    'required':'true'
                }
            )
        }
