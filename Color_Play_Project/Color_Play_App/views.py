from django.shortcuts import render
from .models import  Color_Code_Data
# Create your views here.


def Color_Picker_Showing(request):
    
    if request.method == 'POST':
        color_data = Color_Code_Data()
        color_code_client = request.POST.get("ColorInput")
        color_data.color_code = color_code_client
        color_data.save()
        print(color_code_client)
    
    context = {}
    return render(request, "color_picker.html", context)