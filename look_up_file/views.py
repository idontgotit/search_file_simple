# Create your views here.
import os
import pathlib
from django.http import HttpResponse
from django.shortcuts import render


def look_file(request):
    return render(request, 'look_up_file.html', {})


def search_file(request):
    result = []
    search_text = request.POST.get("search_text")

    current_path = pathlib.Path(__file__).parent.absolute()

    if search_text:
        for file in os.listdir(str(current_path) + "/search_folder/"):
            if file.endswith(".docx"):
                if str(search_text).upper() in str(file).upper():
                    result.append({
                        "file_name": file,
                        "link": os.path.join(str(current_path) + "/search_folder/", file)
                    })
    return render(request, 'look_up_file.html', {"result": result})


def file_view(request):
    file_path = request.GET.get("link")
    file_name = request.GET.get("file_name")
    data = open(file_path, "rb").read()

    response = HttpResponse(data, content_type='application/vnd.ms-word')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    return response
