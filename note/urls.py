from django.urls import path
from note import views

urlpatterns = [
    path('note_details/', views.NoteDetails.as_view(), name='notedetails'),
]
