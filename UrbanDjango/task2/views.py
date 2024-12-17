from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def func_class(request):
    return render(request, 'func_template.html')


class PresentClass(TemplateView):
    template_name = "presentclass.html"
