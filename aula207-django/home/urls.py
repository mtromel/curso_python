from django.urls import path
from home import views
# from . import views isso é a mesma coisa que a linha acima

urlpatterns = [
    path('', views.home),
]