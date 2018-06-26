from __future__ import unicode_literals
from django.shortcuts import render
from administration_app.models import Staff
from extract_app.models import Recepts
from .models import Patiens
from .models import Prepations
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import django

def get_main_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            return render(request, 'registry_app/main.html', {})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')


def get_preparations_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            preparations = Prepations.objects.all()
            flag_view_additional_info = False
            return render(request, 'registry_app/preparations.html', {'preparations':preparations, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_preparation(request, id_preparations=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            return_objects_preparations = []
            preparations = Prepations.objects.all()
            for item in preparations:
                preparation = {}
                preparation['id'] = item.id
                preparation['name'] = item.name
                preparation['type_prepations'] = item.type_prepations
                return_objects_preparations.append(preparation)

            flag_view_additional_info = True;

            return_objects_preparation = {}
            preparation = Prepations.objects.get(id=id_preparations)
            return_objects_preparation['name'] =  preparation.name
            return_objects_preparation['type_prepations'] = preparation.type_prepations
            return_objects_preparation['maker'] = preparation.maker
            return_objects_preparation['form_release'] = preparation.form_release

            prescriptions_issued = []
            prescriptions_issued.extend(Recepts.objects.filter(id_prepations=id_preparations))
            return_objects_preparation['prescriptions_issued'] = []
            for item in prescriptions_issued:
                ssued = {}
                ssued['name'] = Prepations.objects.get(id=item.id_prepations).name
                ssued['name_patient'] = Patiens.objects.get(id=item.id_patiens).name
                ssued['date_issue'] = item.date_issue
                return_objects_preparation['prescriptions_issued'].append(ssued)               
            return render(request, 'registry_app/preparations.html', {'preparation':return_objects_preparation, 
            'preparations':return_objects_preparations,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_patients_page(request):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            patiens = Patiens.objects.all()
            flag_view_additional_info = False
            patiens.reverse(    )
            return render(request, 'registry_app/patients.html', {'patiens':patiens, 'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def get_patient(request, id_patients=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':
            patiens = Patiens.objects.all()
            flag_view_additional_info = True
            return render(request, 'registry_app/patients.html', {'patien':Patiens.objects.get(id=id_patients), 
            'patiens':patiens,'flag_view_additional_info':flag_view_additional_info})
        else:
            auth.logout(request)
            return redirect('/logsys/login')
    else:
        return redirect('/logsys/login') 

def preparations_search(request):
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        prepations = []
        return_object = []
        prepations.extend(Prepations.objects.filter(name=search_term))
        prepations.extend(Prepations.objects.filter(type_prepations=search_term))
        for item in prepations:
            preparation = {}
            preparation['id'] = Prepations.objects.get(name=item.name).id
            preparation['name'] = Prepations.objects.get(name=item.name).name
            preparation['type_prepations'] = Prepations.objects.get(name=item.name).type_prepations
            preparation['maker'] = Prepations.objects.get(name=item.name).maker
            preparation['form_release'] = Prepations.objects.get(name=item.name).form_release
            return_object.append(preparation)
        prepations = []
        prepations.extend(Prepations.objects.filter(maker=search_term))
        prepations.extend(Prepations.objects.filter(form_release=search_term))
        for item in prepations:
                preparation = {}
                preparation['id'] = item.id
                preparation['name'] = item.name
                preparation['type_prepations'] = item.type_prepations
                preparation['maker'] = item.maker
                preparation['form_release'] = item.form_release
                return_object.append(preparation)

        return render(request, 'registry_app/preparations.html', 
            {'preparation':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'registry_app/preparations.html', 
            {'flag_view_additional_info':flag_view_additional_info})


def patients_search(request):
    if request.method == 'GET':
        flag_view_additional_info = False
        search_term = request.GET['search_term']
        patients = []
        return_object = []
        patients.extend(Patiens.objects.filter(name=search_term))
        patients.extend(Patiens.objects.filter(lastname=search_term))
        patients.extend(Patiens.objects.filter(patronymic=search_term))
        for item in patients:
            patient = {}
            patient['id'] = Patiens.objects.get(name=item.name).id
            patient['name'] = Patiens.objects.get(name=item.name).name
            patient['lastname'] = Patiens.objects.get(name=item.name).lastname
            patient['patronymic'] = Patiens.objects.get(name=item.name).patronymic
            patient['address'] = Patiens.objects.get(name=item.name).address
            patient['polis'] = Patiens.objects.get(name=item.name).polis
            patient['phone'] = Patiens.objects.get(name=item.name).phone
            patient['date_of_birth'] = Patiens.objects.get(name=item.name).date_of_birth
            patient['sector'] = Patiens.objects.get(name=item.name).sector
            patient['Recording_date'] = Patiens.objects.get(name=item.name).Recording_date
            return_object.append(patient)
        patients = []
        patients.extend(Patiens.objects.filter(address=search_term))
        patients.extend(Patiens.objects.filter(polis=search_term))
        patients.extend(Patiens.objects.filter(phone=search_term))
        patients.extend(Patiens.objects.filter(date_of_birth=search_term))
        patients.extend(Patiens.objects.filter(sector=search_term))
        patients.extend(Patiens.objects.filter(Recording_date=search_term))
        for item in patients:
            patient = {}
            patient['id'] = item.id
            patient['name'] = item.name
            patient['lastname'] = item.lastname
            patient['address'] = item.address
            patient['polis'] = item.polis
            patient['phone'] = item.phone
            patient['date_of_birth'] = item.date_of_birth
            patient['sector'] = item.sector
            patient['Recording_date'] = item.Recording_date
            return_object.append(patient)

        return render(request, 'registry_app/patients.html', 
            {'patiens':return_object, 'flag_view_additional_info':flag_view_additional_info})
    else:
        return render(request, 'registry_app/patients.html', 
            {'flag_view_additional_info':flag_view_additional_info})    

def new_patient(request):
    if request.is_ajax():
        if request.method == 'GET':
            patient = Patiens.objects.filter(polis=request.GET['polis'])
            if len(patient) != 0:
                return HttpResponse('repit_polis', content_type='text/html')
            else:
                patient = Patiens(name=request.GET['name'],
                    lastname=request.GET['lastname'],
                    patronymic=request.GET['patronymic'],
                    address=request.GET['address'],
                    polis=request.GET['polis'],
                    phone=request.GET['phone'],
                    sector=request.GET['sector'],
                    Recording_date=request.GET['Recording_date'])
                patient.save()
                return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')

def delet_patient(request, id_patien=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':    
            try:
                delete = Patiens.objects.get(id=id_patien)
                delete_recept = Recepts.objects.get(id_patiens=id_patien)
                delete.delete()
                delete_recept.delete()
                patiens = Patiens.objects.all()
                flag_view_additional_info = False
                patiens.reverse()
                return render(request, 'registry_app/patients.html', {'patiens':patiens, 'flag_view_additional_info':flag_view_additional_info})
            except Recepts.DoesNotExist:
                patiens = Recepts.objects.exclude(id=id_patien)
                delete = Patiens.objects.get(id=id_patien)
                patiens = Patiens.objects.all()
                delete.delete()
                return render(request, 'registry_app/patients.html', {'patiens':patiens,})
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def delet_preparation(request, id_preparations=1):
    if request.user.is_authenticated:
        type_user = Staff.objects.get(login_employee=request.session['login']).type_users
        if type_user == 'registry':    
            try:
                delete = Prepations.objects.get(id=id_preparations)
                delete_recept = Recepts.objects.get(id_prepations=id_preparations)
                delete.delete()
                delete_recept.delete()
                # preparations = Prepations.objects.exclude(id=id_preparations)
                preparations = Prepations.objects.all()
                flag_view_additional_info = False
                preparations.reverse()
                return render(request, 'registry_app/preparations.html', {'preparations':preparations, 'flag_view_additional_info':flag_view_additional_info})
            except Recepts.DoesNotExist:
                preparations = Prepations.objects.exclude(id=id_preparations)
                delete = Prepations.objects.get(id=id_preparations)
                delete.delete()
                preparations = Prepations.objects.all()
                preparations.reverse()
                return render(request, 'registry_app/preparations.html', {'preparations':preparations})
            else:
                auth.logout(request)
                return redirect('/logsys/login')
    else:
        return redirect('/logsys/login')

def new_prepation(request):
    if request.is_ajax():
        if request.method == 'GET':
            # prepation = Prepations.objects.filter(polis=request.GET['polis'])
            # if len(patient) != 0:
            #     return HttpResponse('repit_polis', content_type='text/html')
            # else:
                prepation = Prepations(name=request.GET['name'],
                    type_prepations=request.GET['type_prepations'],
                    maker=request.GET['maker'],
                    form_release=request.GET['form_release'],)
                prepation.save()
                return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')
    