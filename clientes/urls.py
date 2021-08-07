from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import PersonList, PersonDetail, FormView, PersonCreate, \
    PersonUpdate, PersonDelete, IndexView, CommentView



urlpatterns = [

    path('list/', persons_list, name="persons_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
    path('person_list/', PersonList.as_view(), name="person_list"),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name="person_detail"),
    path('person_form', FormView.as_view(), name='person_form'),
    path('person_create', PersonCreate.as_view(), name="person_form_create"),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name="person_update"),
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name="person_delete"),
    path('newindex', IndexView.as_view(), name="index_blocks"),
    path('comment/', CommentView.as_view(), name="comment_form"),
]