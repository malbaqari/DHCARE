from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render

from .custom_decorators import custom_user_passes_test
from .dnsSC import dnsSC_get, dnsSC_post
from .forms import getProviderInfo, submitProviderInfo, getAppointments, bookAppointment
from .models import appointment
from .tables import appointmentTable


def home(request):
    return render(request, 'dhcare/home.html')


def about(request):
    return render(request, 'dhcare/about.html', {'title': 'About'})


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Admins') in u.groups.all())
def adminui(request):
    return render(request, 'dhcare/adminui.html')


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Admins') in u.groups.all())
def adminui_get(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = getProviderInfo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            account_address = form.cleaned_data.get('OHP_Eth')
            provider = dnsSC_get(account_address)
            context = {
                'provider': provider
            }

            return render(request, 'dhcare/adminui-get.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = getProviderInfo()

    return render(request, 'dhcare/adminui-get.html', {'form': form})


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Admins') in u.groups.all())
def adminui_submit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = submitProviderInfo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            providerTx = dnsSC_post(form.cleaned_data.get('name'), form.cleaned_data.get('webAddress'))
            context = {
                'providerTx': providerTx
            }

            return render(request, 'dhcare/adminui-submit.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = submitProviderInfo()

    return render(request, 'dhcare/adminui-submit.html', {'form': form})


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Reception') in u.groups.all())
def receptionui(request):
    return render(request, 'dhcare/receptionui.html')


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Reception') in u.groups.all())
def receptionui_get(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = getAppointments(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nid = form.cleaned_data.get('nid')
            table = appointmentTable(appointment.objects.filter(nid=nid))

            return render(request, 'dhcare/appointments.html', {"table": table})

    else:
        form = getAppointments()

    return render(request, 'dhcare/receptionui-get.html', {'form': form})


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Reception') in u.groups.all())
def receptionui_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = bookAppointment(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            patient_name = form.cleaned_data.get('name')
            messages.success(request, 'Appointment Booking Confirmed for Patient Name {}'.format(patient_name))
            return render(request, 'dhcare/receptionui.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = bookAppointment()

    return render(request, 'dhcare/receptionui-book.html', {'form': form})
