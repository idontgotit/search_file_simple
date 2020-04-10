from sys import path

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def look_file(request):
    return render(request, 'look_up_file.html', {})


def search_file(request):
    result = []
    search_text = request.POST.get("search_text")
    import glob
    import pathlib
    current_path = pathlib.Path(__file__).parent.absolute()
    print(current_path)
    import os
    if search_text:
        for file in os.listdir(str(current_path) + "/search_folder/"):
            if file.endswith(".docx"):
                if search_text in file:
                    result.append({
                        "file_name": file,
                        "link": os.path.join(current_path, file)
                    })
    return render(request, 'look_up_file.html', {"result": result})
