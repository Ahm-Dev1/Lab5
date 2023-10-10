from django.urls import path 
from . import views

app_name = "add"
urlpatterns = [
    path('',views.show_form, name='show_form'),
    path('add/',views.add, name='add'),
    # path('name/',views.default, name='default'),

]
