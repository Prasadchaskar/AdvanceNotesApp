from django.shortcuts import render,redirect
from . forms import DocumentForm,TextForm,QuestionForm,CommentForm
from . models import Document,Textnotes,Questions,Comment

def home(request):
    documents=Document.objects.all()
    text_notes=Textnotes.objects.all()
    quest=Questions.objects.all()
    comm=Comment.objects.all()
    return render(request,'index.html',{'documents':documents,'text_notes':text_notes,'quest':quest,'comm':comm})

 
def show(request):
    documents=Document.objects.all()
    
    return render(request,'show_notess.html',{'documents':documents})
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def Upload_text_notes(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TextForm()
    return render(request, 'text_notes.html', {'form': form})


def Ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'ques.html', {'form': form})

def Add_Comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'ques.html', {'form': form})