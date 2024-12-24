from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def func_class(request):
    return render(request, 'second_task/func_template.html')


class PresentClass(TemplateView):
    template_name = "second_task/presentclass.html"
