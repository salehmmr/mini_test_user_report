from django.shortcuts import render
from django.views import generic

from . import models


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_user = models.user.objects.all().count()
    num_report = models.report.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_user': num_user, 'num_report': num_report},
    )