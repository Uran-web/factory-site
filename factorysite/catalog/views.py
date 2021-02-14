from django.shortcuts import render
from .models import Vacancy, VacancyName, VacancyDescribe
from django.views import generic


# Create your views here.


def vacancy(request):
    """
    The function for viewing vacancy page
    """
    num_vacancies = Vacancy.objects.all()

    # Display of HTML-pattern vacancy.html
    # with objects inside
    return render(
        request,
        'index.html',
        context={"num_vacancies": num_vacancies}
    )


class VacanciesListView(generic.ListView):
    model = Vacancy


class VacanciesDetailView(generic.DetailView):
    model = Vacancy
    template_name = 'catalog/vacancies-detail.html'


class MainPageView(generic.TemplateView):
    """
    Show the main page
    """
    template_name = 'catalog/templates/index.html'
