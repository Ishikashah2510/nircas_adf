from django.shortcuts import render
from .forms import *

# Create your views here.


def trial_view(request):
    form = TrialForm()
    return render(request, 'cashier/trial.html', {'form': form})
