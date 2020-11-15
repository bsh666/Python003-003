from django.core.paginator import Paginator
from django.shortcuts import render

from .models import MovieModel

# Create your views here.


def index(request):
    keyword = request.GET.get("q", "")
    page = request.GET.get("p", 1)
    name = request.GET.get("name", "")
    filter_kws = {
        "stars__gt": 3
    }
    if not name:
        first = MovieModel.objects.exclude(name="").filter(**filter_kws).first()
        if name is not None:
            name = first.name
    filter_kws.setdefault("name", name)
    if keyword:
        filter_kws.setdefault("description__icontains", keyword)
    items = MovieModel.objects.filter(**filter_kws).order_by("-published_date").all()
    pagination = Paginator(items, 5)
    items = pagination.get_page(page)

    return render(request, 'index.html', locals())