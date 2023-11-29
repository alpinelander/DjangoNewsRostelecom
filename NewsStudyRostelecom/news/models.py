from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    categories = (('E','Economics'),
                  ('S','Science'),
                  ('IT','IT')
                  )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название', max_length=100, default='')
    anouncement = models.TextField('Аннотация', max_length=250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата публикации', auto_created=True)
    category = models.CharField(choices=categories, max_length=20, verbose_name='Категории')

    def __str__(self):
        return f'{self.title} от {str(self.date)[:10]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'