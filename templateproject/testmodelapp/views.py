from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from testmodelapp import models
import json
# Create your views here.


def student_detail_view(request, id):
    obj = models.StudentModel.objects.get(id=id)
    return render(request, 'testmodelapp/student_info.html', {"item": obj})


def student_update_view(request, id):
    obj = models.StudentModel.objects.get(id=id)
    if request.method == "POST":
        mark = int(request.POST.get("mark"))
        obj.mark = mark + 20
        obj.save()
        return JsonResponse({"message": "Mark has been updated!!"})
    return render(request, 'testmodelapp/update.html', {"item": obj})


def student_view(request):
    obj = models.StudentModel.objects.all()
    # obj = models.StudentModel.objects.filter(mark__gt=400)
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
    return render(request, 'testmodelapp/home.html', {"result": obj})
