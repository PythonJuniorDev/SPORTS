from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework import viewsets
from athletes.models import Athlete, Instructor, Personal_access_code
from athletes.serializers import AthleteSerializer, InstructorSerializer, Personal_access_codeSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django.http import HttpResponse

def help_file(request):
    return HttpResponse('Questions or comments? Contact us at m.amine@aol.nl We like to hear from you!')


def food(request):
    template = loader.get_template('goodFood3.html')
    return HttpResponse(template.render())


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all().order_by('first_name')
    serializer_class = AthleteSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['first_name', 'last_name', 'birth_date', 'email', 'phone_number', 'instructor__name_instructor']
    # ordering_fields = ['first_name', 'last_name']


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all().order_by('name_instructor')
    serializer_class = InstructorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name_instructor', 'athlete__first_name', 'athlete__last_name']
    # ordering_fields = ['name_instructor']


class Personal_access_codeViewSet(viewsets.ModelViewSet):
    queryset = Personal_access_code.objects.all()
    serializer_class = Personal_access_codeSerializer


def contact(request):
    contact_information = [
        {'Toon' : +31612345678,
        'Patrick' : +31612345678,
        'Doff' : +31612345678,
        'Raymond': +31612345678,
        'Pauline': +31612345678,
        'Bambi' : +31612345678}
    ]

    output = {'Contact information' : contact_information}

    return render(request, 'contact.html', output)


