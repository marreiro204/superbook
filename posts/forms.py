from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["autor", "mensagem"]
        widgets = {
            "autor": forms.Select(attrs={"class": "form-select"}),
            "mensagem": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Escreva sua mensagem..."}),
        }
