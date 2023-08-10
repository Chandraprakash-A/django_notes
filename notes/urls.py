from notes import views
from django.urls import path
from .views import NotesListView, NoteCreateView,NoteDeleteView,NoteDetailView,NoteUpdateView


urlpatterns = [
    path("", views.Home, name="home"),
    path("notes/", NotesListView.as_view(), name="notes"),
    path("notes/<int:pk>/detail", NoteDetailView.as_view(), name="note_detail"),
    path("notes/<int:pk>/delete", NoteDeleteView.as_view(), name="note_delete"),
    path("notes/<int:pk>/update", NoteUpdateView.as_view(), name="note_update"),
    path("create/", NoteCreateView.as_view(), name="create"),
    
]
