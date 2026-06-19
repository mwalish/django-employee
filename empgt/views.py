from django.http import HttpResponse
from rest_framework.decorators import api_view
# views
def home(request):
    return HttpResponse("welcome to task_managment")

@api_view(['POST'])
def sum(request):
    num1=request.data.get("num1")
    num2=request.data.get("num2")
    sum=num1+num2
    return HttpResponse(f"The sum {num1} and {num2} is : {sum}")
    