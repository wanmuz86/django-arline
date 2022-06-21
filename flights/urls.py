from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>', views.flight,name="flight"),
    path('contact-us', views.contact, name="contact"),
    path('about-us', views.about, name="about" ),
    path('<int:flight_id>/book', views.book, name="book")
]
