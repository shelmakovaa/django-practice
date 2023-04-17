from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>', views.date),
    path('type', views.zodiac_type),
    path('type/<str:element>', views.get_elements, name='zodiac_elem'),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac, name='horoscope-name'),
]
