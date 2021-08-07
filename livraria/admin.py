from django.contrib import admin
from .models import Book, Publisher, Author, Store, Book2


@admin.register(Book)
class BookADmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pages', 'rating', 'publisher')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    # TODO:Preciso saber como passar um campo ManyToMany no Grid do admin

    list_display = ('name',)


@admin.register(Book2)
class Book2ADmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pages', 'rating', 'publisher', 'calcula_total')




