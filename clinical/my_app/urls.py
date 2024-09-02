from django.urls import path
from my_app import views
urlpatterns = [
    path('',views.PatientListView.as_view(),name='index'),
    path('create/',views.PatientCreateView.as_view()),
    path('update/<int:pk>/',views.PatientUpdateView.as_view()),
    path('delete/<int:pk>/',views.PatientDeleteView.as_view()),
    path('addData/<int:pk>/',views.addData),
    path('analyze/<int:pk>/',views.analyzedata),
]
