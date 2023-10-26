from django.shortcuts import render
from .models import Disco

# Create your views here.
def index(request):

    discos = Disco.objects.all()

    context = {
        "discos": discos,
    }

    return render(request, "index.html", context)

def detail(request, pk):

    disco = Disco.objects.get(pk=pk)

    context = {
        "disco": disco,
    }

    return render(request, "detail.html", context)