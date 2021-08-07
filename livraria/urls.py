from django.urls import path
from .views import Livrobulk, Editorbulk


urlpatterns = [
    path('livros_bulk/', Livrobulk.as_view(), name='livros'),
    path('editor_bulk/', Editorbulk.as_view(), name='editor')
]

