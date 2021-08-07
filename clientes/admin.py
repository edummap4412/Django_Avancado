from django.contrib import admin
from .models import Person, Documento, Author, Article
from .actions import make_published, make_draft
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoas', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {
            'classes': ('collapse',), # 'collapse é uma classe CSS que esconde ou mostra os campos ,
            'fields': ('age', 'salary', 'photo')})
    )

    #fields = ('doc', ('first_name', 'last_name'), 'age', 'salary','photo') # organiza formatação dos campos
    exclude = ('bio',)
    list_display = ('first_name', 'last_name', 'age', 'salary','tem_foto') # mostra campos no meu Grid
    list_filter = ('age', 'salary')
    date_hierarchy = 'data'
    search_fields = ('id', 'age', 'first_name') # pesquisa campos

    def tem_foto(self, obj):
        if obj.photo:
            return "Sim"
        else:
            return "Não"

    tem_foto.short_description = 'Possui foto' # esse é o cabeçalho do campo


admin.site.register(Documento)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'view_birth_date')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published, make_draft]

    def make_pulished_two(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request,ngettext(
            '%d marcado como publicado com sucesso'
            '%d Marcados como publicados com sucesso',updated) %updated,messages.SUCCESS)


admin.site.site_header = 'Gerenciador de Clientes'
admin.site.index_title = 'Administração dos Registros'
admin.site.site_title = 'Seja bem vindo ao Gerenciador de Clientes'



