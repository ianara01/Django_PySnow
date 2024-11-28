#  forms.py   /blog
# 
from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widget = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a category name',}),             # placeholder 메세지 ChatGPT 와 같이 기본값 자리잡아주는 것
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={  # 'name' 대신 'title'로 수정
                'class': 'form-control',
                'placeholder': 'Enter a post title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a post content',
                'rows': 10,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select a category',  # 선택창에는 placeholder가 표시되지 않음
            }),
        }
