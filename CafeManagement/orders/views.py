from django.shortcuts import render, redirect
from .forms import BookTableForm


def book(request):
    if request.method == "POST":
        form = BookTableForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return redirect('home')
            
    else:
        form = BookTableForm()
    return render(request, "book.html", context={"form": form})
