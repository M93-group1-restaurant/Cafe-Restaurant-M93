from django.shortcuts import render
from .forms import BookTableForm


def book(request):
    if request.method == "POST":
        form = BookTableForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
    else:
        form = BookTableForm()
    return render(request, "book.html", context={"form": form})
