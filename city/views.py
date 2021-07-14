from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from .models import City, State, Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED)

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
        
# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StateSerializer
    queryset = State.objects.all()
    
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City 
        fields = '__all__'
        
        
# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CitySerializer
    queryset = City.objects.all()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users 
        fields = '__all__'
        
        
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CitySerializer
    queryset = Users.objects.all()
    
class getUsers(APIView):
    def post(self, request,*args, **kwargs):
        city = request.data.get('city')
        state = request.data.get('state')
        population = Users.objects.all()
        if state:
            population = population.filter(city__state__name=state)
        elif city:
            population = population.filter(city = city.lower())
        male = population.filter(gender = 'male')
        print(male.count())
        female = population.filter(gender = 'female')
        total7 = population.filter(age__lte=6)
        male7 = male.filter(age__lte=6).count()
        female7 = female.filter(age__lte=6).count()
        literates = population.filter(literate=True)
        data = {
            'populationtotal' : population.count(),
            'populationmale' :male.count(),
            'populationfemale' : female.count(),
            '0-6populationtotal' : total7.count(),
            '0-6populationmale' : male7,
            '0-6populationfemale' : female7,
            'literatestotal' : (literates.count()/population.count())*100  if population.count() > 0 else 0,
            'literatesmale' : (literates.filter(gender = 'male').count()/male.count())*100 if male.count() > 0 else 0,
            'literatesfemale' : (literates.filter(gender = 'female').count()/female.count())*100 if female.count() > 0 else 0,
            'sexratio' : male.count()/female.count() if female.count() > 0 else 0,
            'childsexratio' : male7/female7 if female7 > 0 else 0,
            'effectiveliteracyratetotal' : (population.filter(age__gte=6,literate=True).count())*100/population.filter(age__gte=6).count() if population.filter(age__gte=6).count() > 0 else 0,
            'effectiveliteracyratemale' : (population.filter(age__gte=6,literate=True,gender='male').count()/population.filter(age__gte=6,gender='male').count())*100 if population.filter(age__gte=6,gender='male').count() > 0 else 0,
            'effectiveliteracyratefemale': (population.filter(age__gte=6,literate=True,gender='female').count()/population.filter(age__gte=6,gender='female').count())*100 if population.filter(age__gte=6,gender='female').count() > 0 else 0 ,
            'totalgraduates' : population.filter(graduate=True).count(),
            'malegraduates' : population.filter(graduate=True,gender='male').count(),
            'femalegraduates' : population.filter(graduate=True,gender='female').count(),
        }
        return Response(data,status=HTTP_200_OK)