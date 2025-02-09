from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.template import loader

from core.models import ModelA, ModelB

#
# UTILITIES
#
# HTMX Utility
# Reference - https://stackoverflow.com/questions/65569673/htmx-hx-target-swap-html-vs-full-page-reload
class HTTPResponseHXRedirect(HttpResponseRedirect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


def home(request):
    context = {
            "as": ModelA.objects.get(),
            "bs": ModelB.objects.get(),
    }

    template = loader.get_template("home.html")
    return HttpResponse(template.render(context, request))
