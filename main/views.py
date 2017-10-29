from django.shortcuts import render

from django.views import View
from django.template.response import TemplateResponse


class BaseView(View):

    def get(self, request):
        return TemplateResponse(request, "base.html", {})
