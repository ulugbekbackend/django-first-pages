from django.urls import path
from .views import HomePageView,AboutPageView,ServisesPageView,IndexPageView

urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
    path('home/',HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('servises/',ServisesPageView.as_view(),name='servises'),
]
