from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("workspace", views.workspace, name="workspace"),
    path("result", views.result, name="result"),
    path("analysis", views.analysis, name="analysis")
]