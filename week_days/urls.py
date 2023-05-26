from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_page),
    path('beautiful_table', views.table),
    path('<int:day>', views.todo_number),
    path('<str:day>', views.todo, name='day-name'),
]