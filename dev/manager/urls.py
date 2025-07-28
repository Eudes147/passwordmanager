from django.urls import path,include
from . import views

urlpatterns = [
    path("addPassword",views.addPassword,name="addPassword"),
    path("",views.dashboard,name="dashboard"),
    path("deletePassword/<int:id>",views.deletePassword,name="deletePassword"),
    path("editPassword/<int:id>",views.editPassword,name="editPassword"),
]