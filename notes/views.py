from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Note
from .forms import CreateNoteForm
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.urls import reverse_lazy


def Home(request):
    return render(request, "notes/home.html")


class NotesListView(ListView):
    model = Note
    template_name = "notes/notes_list.html"
    context_object_name = "notes"


class NoteCreateView(CreateView):
    template_name = "notes/note_create.html"
    form_class = CreateNoteForm
    success_url = "/notes/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_delete.html"
    success_url = reverse_lazy("notes")


class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"


class NoteUpdateView(UpdateView):
    model = Note
    form_class = CreateNoteForm
    template_name = "notes/note_update.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
