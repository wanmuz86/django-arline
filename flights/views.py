from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from flights.models import Flight, Airport,Passenger;
from django.urls import reverse

# Create your views here.

def index(request):
	flights = Flight.objects.all()
	return render(request,"flights/index.html", {
		"flights":flights
	})

def flight(request,flight_id):
	flight = Flight.objects.get(pk=flight_id)
	passengers = flight.passengers.all()
	return render(request,"flights/flight.html",{
		"flight":flight,
		"passengers":passengers,
	})

def contact(request):
	return render(request,"flights/contact.html")

def about(request):
	return render(request, "flights/about.html")

def book(request, flight_id):

	if request.method == "POST":

		# Get flight info
		flight = Flight.objects.get(pk=flight_id)

		# Get passenger info

		first_name = request.POST["first"]
		last_name = request.POST["last"]
		
		queries = Passenger.objects.all().filter(first = first_name, last=last_name)
		newpax = None
		if queries.count() == 0:
			#in case user is not there, Add inside database
			newpax = Passenger(first=first_name,last=last_name)
			newpax.save()
		else:
			# scenario where user exists because filter returns an array
			newpax=queries[0]
		# add user as a passengers in the flight
		flight.passengers.add(newpax)

		# redirect ke page index
		return HttpResponseRedirect(reverse('index'))




