from django.shortcuts import render, HttpResponse
from testmodelapp import models
# Create your views here.


def student_view(request):
    obj = models.StudentModel.objects.all()
    # new_item = []
    # for item in obj:
    #     result = {
    #         "name": item.name,
    #         "age": item.age,
    #         "roll": item.roll,
    #         "subject": item.subject,
    #         "mark": item.mark
    #     }
    #     new_item.append(result)
    # html = f"<h2>The result is {new_item}</h2>"
    return render(request, 'testmodelapp/student_info.html', {"result": obj})
