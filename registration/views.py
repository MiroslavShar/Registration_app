from django.shortcuts import render, redirect
from django.views import View
from registration.models import Doctor, MedicalHistory, Recommendation, ReasonForVisit, Patient, Visit
from django.http import HttpResponse

class IndexPage(View):
    def get(self, request):
        return redirect('home')

class AddDoctor(View):

    def get(self, request):
        return render(request, 'add_doctor.html')
    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        specialization = request.POST.get('specialization')
        new_doctor = Doctor(name=name, surname=surname, specialization=specialization)
        new_doctor.save()
        return HttpResponse('Dodane')