from django.urls import path
from app1 import views

app_name='app1'
urlpatterns = [
    path('first/',views.great,name='map'),
    path('second/',views.if_demo,name='map1'),
    path('third/',views.for_demo,name='map2'),
]

