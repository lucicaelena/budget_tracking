from django.urls import path
from . import views


urlpatterns = [
    path('', views.spending,name='spending'),
    path('adauga/',views.adauga,name='adauga'),
    path('select_day_data/', views.select_day_data,name='select_day_data'),
    path('select_range_data/', views.select_range_data, name='select_range_data'),
    path('export/', views.export, name='export')
]