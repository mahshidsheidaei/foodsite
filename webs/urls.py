from django.urls import path
from .views import show,Postdrtail
urlpatterns = [
   path('',show,name='home'),
   path('<int:pk>/',Postdrtail.as_view(),name='detail'),
]
