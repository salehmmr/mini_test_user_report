from django.shortcuts import render
from django.views import generic
from . import models


class Index(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_user'] = models.user.objects.all().count()
        context['num_report'] = models.report.objects.all().count()
        return context

# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_user = models.user.objects.all().count()
#     num_report = models.report.objects.all().count()
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'index.html',
#         context={'num_user': num_user, 'num_report': num_report},
#     )
