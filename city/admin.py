from city.models import City, State, Users
from django.contrib import admin

# Register your models here.
admin.site.register(Users)
admin.site.register(State)
admin.site.register(City)