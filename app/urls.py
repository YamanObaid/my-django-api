from django.urls import path
from .views import hello, NoteCreateView

urlpatterns = [
    path('', hello),
    path('create-note/', NoteCreateView.as_view(), name='create-note'),

]
