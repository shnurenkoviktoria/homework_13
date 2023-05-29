from django.shortcuts import render
from faker import Faker

from .forms import AmountForm

fake = Faker()


# Create your views here.
def index(request):
    form = AmountForm(request.POST)
    if request.method == "POST" and form.is_valid():
        num = form.cleaned_data["num"]
        content = fake.text(max_nb_chars=num)

        return render(request, "index.html", {"content": content})
    else:
        form = AmountForm()
        return render(request, "index.html", {"form": form})
