from django.urls import path
from . import views

# URLConf
urlpatterns = [ # Precisa ser esse o nome
  path('oi/', views.diga_oi)
]