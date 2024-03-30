from django.urls import path
from . import views

urlpatterns = [
    #path('', views.WhiteboardView.as_view(), name="whiteboard"),
    path('', views.whiteboard, name='whiteboard'),
    path('searchpatient/', views.searchpatient, name="searchpatient"),
    path('patients/', views.PatientsListView.as_view(), name='patients.list'),
    path('patients/<int:pk>/', views.PatientsDetailView.as_view(), name="patients.detail"), 
    path('patients/new/', views.PatientsCreateView.as_view(), name="patients.new"), 
    path('patients/<int:pk>/edit/',views.PatientsUpdateView.as_view(), name="patients.update"),
    path('patients/<int:pk>/delete/', views.PatientsDeleteView.as_view(), name="patients.delete"),
    path('doctors/', views.DoctorsListView.as_view(), name='doctors.list'),
    path('doctors/new/', views.DoctorsCreateView.as_view(), name="doctors.new"), 
    path('doctors/<int:pk>/edit/',views.DoctorsUpdateView.as_view(), name="doctors.update"),
    path('doctors/<int:pk>/delete/', views.DoctorsDeleteView.as_view(), name="doctors.delete"),
    path('procedures/', views.ProceduresListView.as_view(), name='procedures.list'),
    path('procedures/<int:pk>', views.ProceduresDetailView.as_view(), name="procedures.detail"), 
    path('procedures/new/', views.ProceduresCreateView.as_view(), name="procedures.new"), 
    path('procedures/<int:pk>/edit/',views.ProceduresUpdateView.as_view(), name="procedures.update"),
    path('procedures/<int:pk>/delete/', views.ProceduresDeleteView.as_view(), name="procedures.delete"),


]