from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from shortener_url.forms import LinkForm

from shortener_url.models import Link

# Create your views here.


def short(request):
    form = LinkForm(request.POST)
    context = {
        'form': form
    }

    if form.is_valid():
        link_object = form.save()
        context['object'] = link_object
        context['created'] = True
    return render(request, "links/create.html", context=context)


def link_to(request, alias):
    try:
        link = Link.objects.get(alias=alias)
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    return redirect(link.link_to)
