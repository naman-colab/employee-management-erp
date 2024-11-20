from django.shortcuts import render,HttpResponse
from .models import Employee
from .models import Department
from .models import Role
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        department_id = request.POST['department']
        role_id = request.POST['role']
        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            salary=int(salary),
            bonus=int(bonus) if bonus else 0,  
            phone=phone,
            hire_date=datetime.now(),
            dept_id=department_id,  
            role_id=role_id)
        new_emp.save()
        return HttpResponse('Employee added succesfully')
    elif request.method=='GET':
     departments = Department.objects.all()
     roles = Role.objects.all()
     return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})
    else:
        return HttpResponse("An ERROR Occured")


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("please enter valid emp id ")    
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)



def filter_emp(request):
    departments = Department.objects.all()
    roles = Role.objects.all()

    if request.method == 'POST':
        # Get form values from the request
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        department_id = request.POST.get('department', '')
        role_id = request.POST.get('role', '')

        # Start with all employees
        emps = Employee.objects.all()

        # Apply filters if provided
        if first_name:
            emps = emps.filter(first_name__icontains=first_name)
        if last_name:
            emps = emps.filter(last_name__icontains=last_name)
        if department_id:
                emps = emps.filter(dept_id=int(department_id))  
        if role_id:
            emps = emps.filter(role_id=int(role_id))
     
        
        
        context = {
            'emps': emps,
            'departments': departments,
            'roles': roles,
        }
        return render(request, 'all_emp.html', context)

    else:
        context = {
            'departments': departments,
            'roles': roles,
        }
        return render(request, 'filter_emp.html', context)

