def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


make_published.short_description = "Postado"


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


make_draft.short_description = 'Seleciando'


def nfe_emitida(modelsadmin, request, queryset):
    queryset.update(nfe_emitida=True)
