from django.shortcuts import render
# to allow other domains easily access our methods
from django.views.decorators.csrf import csrf_exempt
#json parser to parse the in concomming data into the data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

#these are the api methods for department


@csrf_exempt
# Normally when you make a request via a form you want the form being submitted to your view to 
# originate from your website and not come from some other domain. To ensure that this happens, you 
# can put a csrf token in your form for your view to recognize. If you add @csrf_exempt to the top 
# of your view, then you are basically telling the view that it doesn't need the token. This is a 
# security exemption that you should take seriously.

# to perfrom operations on departments database
def departmentApi(request,id=0):
    # get method will return all the data from department table in json format
        #get method to get all data from database, serialize it and sent it to client
    if request.method=='GET':
        #retrive all objects
        # all()	Return a copy of the current QuerySet
        departments = Departments.objects.all()
        #we are using serializer class to help it convert into json format
        #serialize it with serializer class which we have defined
        departments_serializer = DepartmentSerializer(departments, many=True)
        #and then return a json response
        return JsonResponse(departments_serializer.data, safe=False)
        # safe=false means we r trying to tell django that what we are trying to convert to json format
        # is actually a valid fromat and if there are some issues we are ok with it

    #post method to get data from client, deserialize when it reaches to server and store in database
    elif request.method=='POST':
        #post method to insert new record to department table
        department_data=JSONParser().parse(request)
        #use serializer to convert it into model type
        department_serializer = DepartmentSerializer(data=department_data)
        #check if model is valid
        if department_serializer.is_valid():
            #if valid save and send success message if not return fail message
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    # put method to update an existing record
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        #get()	Returns a single object. Throws an error if lookup returns multiple objects
        #here we are capturing the existing record using department id
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        # update old values present in "department" with new values present in "depart_data"
        department_serializer=DepartmentSerializer(department,data=department_data)
        #if valid save and return json response
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        #delete()	Performs an SQL DELETE that deletes all rows in the QuerySet
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


# to perfrom operations on employee database
@csrf_exempt
def employeeApi(request,id=0):
    
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
     
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# to store media files
@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)
