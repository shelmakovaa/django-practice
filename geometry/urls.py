from django.urls import path
from . import views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rect'),
    path('square/<int:side>', views.get_square_area, name='sqr'),
    path('circle/<int:radius>', views.get_circle_area, name='crl'),
    path('get_rectangle_area/<int:width>/<int:height>', views.redirect_get_rectangle_area),
    path('get_square_area/<int:width>', views.redirect_get_square_area),
    path('get_circle_area/<int:radius>', views.redirect_get_circle_area),
]