from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.vacancy, name='vacancy'),
    path('vacancy/', views.VacanciesListView.as_view(), name='vacancy'),
    re_path(r'^vacancies/(?P<pk>\d+)$', views.VacanciesDetailView.as_view(), name='vacancies-detail'),
    re_path('', views.MainPageView.as_view(), name='index'),
]
