from django.urls import path
from .views import NewsListView, NewsDetail, ContactPageView, HomePageView, Page404View, SinglePageView

urlpatterns = [
    path('', HomePageView, name="home_page"),
    path('news/', NewsListView, name="news_list"),
    path('news/<int:id>/', NewsDetail, name="news_detail"),
    path('contact-us/', ContactPageView, name="contact"),
    path('404/', Page404View, name="404"),
    path('single-page/', SinglePageView, name="single_page"),

]