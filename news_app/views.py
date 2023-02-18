from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.views.generic import ListView
from .models import News, Category, Contact
from .forms import ContactForm


# Create your views here.
def HomePageView(request):
    categories = Category.objects.all()
    news_list = News.objects.filter(status = News.Status.Published).order_by("-publish_time")
    local_news = News.objects.filter(category__name="Mahalliy").order_by("-publish_time")[1:]
    local_one = News.objects.filter(category__name="Mahalliy").order_by("-publish_time")[0]
    context = {
        'news_list': news_list,
        'categories' : categories,
        'local_news' : local_news,
        'local_one' : local_one,
    }

    return render(request, 'news/home_page.html', context)


def NewsListView(request):
    news_list = News.objects.filter(status = News.Status.Published)
    context = {
        "news_list" : news_list
    }
    return render(request, "news/news_list.html", context)


def NewsDetail(request, id):
    news = get_object_or_404(News, id=id, status = News.Status.Published)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context )


def ContactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>Biz tez orada siz bilan bog'lanamiz!</h2>")
    context = {
        "form" : form
    }
    return render(request, 'news/contact.html', context)


def Page404View(request):
    context = {}
    return render(request, 'news/404.html', context)


def SinglePageView(request):
    context = {}
    return render(request, 'news/single_page.html', context)

















