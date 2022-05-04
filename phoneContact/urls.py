from django.urls import path
from .views  import index, contact, create_contact, save, edit, edit_contact, delete, delete_contact, back,search
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('create_contact/', create_contact, name='create_contact'),
    path('save/', save, name='save'),
    path('edit/<int:id>', edit, name='edit'),
    path('edit_contact/<int:id>', edit_contact, name='edit_contact'),
    path('delete/<int:id>', delete, name='delete'),
    path('delete_contact/<int:id>', delete_contact, name='delete_contact'),
    path('back/', back , name='back'),
    path('search/', search , name='search')
]

