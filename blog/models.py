# models.py   /blog

from django.db import models

# Create your models here.
# Category, Post Table

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True, verbose_name='카테고리명')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Category_list'
        db_table = 'lion_blog_category'
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='게시글'
        verbose_name_plural='게시글 목록'
        db_table = 'lion_blog_post'
        ordering = ['-create_at']
        indexes = [
            models.Index(fields=['-create_at'])
        ]
