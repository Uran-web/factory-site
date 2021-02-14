from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
# Create your models here.


class VacancyName(models.Model):
    """
    Model representing a vacancy for all factories (e.g. Baker, Driver etc.).
    """
    vacancy_name = models.CharField(max_length=400, help_text="Введите название вакансии")
    objects = models.Manager()

    def __str__(self):
        """
        This function return name of vacancy
        """
        return self.vacancy_name


class Vacancy(models.Model):
    """
    Represent vacancy
    """
    name = models.ForeignKey(VacancyName, on_delete=models.SET_NULL, null=True, help_text="Выберите название вакансии")
    location = models.CharField(max_length=200, help_text="Введите город")
    vacancy_desc = models.ForeignKey('VacancyDescribe', on_delete=models.SET_NULL, null=True,
                                     help_text="Описание вакансии")
    details = models.TextField(max_length=50000, help_text="Описание вакансии")
    objects = models.Manager()

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        """
        Get description
        """
        return reverse('vacancies-detail', args=[str(self.id)])

    def get_url_func(self):
        """
        Return vacancy list
        """
        return reverse('vacancy-list', args=[str(self.id)])


class VacancyDescribe(models.Model):
    """
    Class represent description of vacancy
    """
    vacancy_title = models.ForeignKey(VacancyName, help_text="Название вакансии", on_delete=models.SET_NULL, null=True)
    description_of_vacancy = models.TextField(max_length=50000, help_text="Введите описание")
    skills_and_experience = models.CharField(max_length=1000, help_text="Требуемые навыки и опыт")
    objects = models.Manager()

    def __str__(self):
        """
        Represent title and experience
        """
        return "{}".format(self.vacancy_title)

    def get_absolute_url(self):
        """
        Get description
        """
        return reverse('description', args=[str(self.description_of_vacancy)])
