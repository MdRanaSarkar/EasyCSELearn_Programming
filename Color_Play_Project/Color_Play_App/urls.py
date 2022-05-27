from django.urls import path
from .views import Color_Picker_Showing
urlpatterns = [
 path("", Color_Picker_Showing, name="ColorShowing")
]
