from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render

from .accessControlSC import accessControlSC_add
from .custom_decorators import custom_user_passes_test
from .dnsSC import dnsSC_get, dnsSC_post
from .forms import getProviderInfo, submitProviderInfo, getAppointments, bookAppointment, getFingerprint, newPatient
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
            fingerprint = getFingerprint()
            return render(request, 'dhcare/receptionui-get.html', {"table": table, "fingerprint": fingerprint})

    else:
        form = getAppointments()

    return render(request, 'dhcare/receptionui-get.html', {'form': form})


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Reception') in u.groups.all())
def new_patient(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = newPatient(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request, 'dhcare/new-patient.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = newPatient()

    return render(request, 'dhcare/new-patient.html', {'form': form})

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


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Reception') in u.groups.all())
def appointment_confirm(request):
    if request.method == 'POST':
        checkbox_id = request.POST.get('id')
        checkbox_table = appointment.objects.filter(id=checkbox_id)
        for item in checkbox_table:
            nid = str(item.nid)
            department_code = str(item.department_code)
        form = getFingerprint(request.POST)
        # check whether it's valid:
        if form.is_valid():
            accessControlSC_tx = accessControlSC_add(nid, department_code)
            return render(request, 'dhcare/appointments.html', {"accessControlSC_tx": accessControlSC_tx})

    return render(request, 'dhcare/appointments.html')


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Doctors') in u.groups.all())
def doctorui(request):
    return render(request, 'dhcare/doctorui.html')


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Doctors') in u.groups.all())
def doctorui_get(request):
    return render(request, 'dhcare/doctorui-get.html')


@custom_user_passes_test(lambda u: Group.objects.get(name='DHCARE-Doctors') in u.groups.all())
def doctorui_submit(request):
    return render(request, 'dhcare/doctorui-submit.html')
