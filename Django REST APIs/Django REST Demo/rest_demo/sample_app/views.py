from django.shortcuts import render
# to allow other domains easily access our methods
from django.views.decorators.csrf import csrf_exempt
#json parser to parse the in concomming data into the data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# import local data
from .serializer import StudentSerializer
from .models import StudentModel

@csrf_exempt
# Normally when you make a request via a form you want the form being submitted to your view to 
# originate from your website and not come from some other domain. To ensure that this happens, you 
# can put a csrf token in your form for your view to recognize. If you add @csrf_exempt to the top 
# of your view, then you are basically telling the view that it doesn't need the token. This is a 
# security exemption that you should take seriously.

# create a viewset
def StudentView(request):

    if request.method == 'POST':
        student_data=JSONParser().parse(request)
        #use serializer to convert it into model type
        student_serializer = StudentSerializer(data=student_data)
        #check if model is valid
        if student_serializer.is_valid():
            #if valid save and send success message if not return fail message
            print(student_data)
            student_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    if request.method == 'GET':
        students = StudentModel.objects.all()
        #we are using serializer class to help it convert into json format
        #serialize it with serializer class which we have defined
        student_serializer = StudentSerializer(students, many=True)
        #and then return a json response
        return JsonResponse(student_serializer.data, safe=False)

	
