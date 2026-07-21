from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render

from .models import Note


@login_required
def index(request):
    if request.method == 'POST':
        Note.objects.create(
            owner=request.user,
            title=request.POST.get('title', ''),
            body=request.POST.get('body', ''),
        )
        return redirect('index')

    notes = Note.objects.filter(owner=request.user).order_by('id')
    return render(request, 'polls/index.html', {'notes': notes})


@login_required
@csrf_exempt
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    # Fix for broken access control:
    # @login_required
    # def note_detail(request, note_id):
    # note = get_object_or_404(Note, pk=note_id, owner=request.user)

    # Fix for CSRF:
    # remove @csrf_exempt from this view

    if request.method == 'POST':
        note.title = request.POST.get('title', note.title)
        note.body = request.POST.get('body', note.body)
        note.save()
        return redirect('note_detail', note_id=note.id)

    return render(request, 'polls/note_detail.html', {'note': note})