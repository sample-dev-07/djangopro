from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Applications/',views.applicationpro,name='applications'),
    path('Django/',views.djangopro,name='djanogo'),
    path('Ludo/',views.hackingpro,name='hacking'),
    path('Search/',views.search,name="search")
]
