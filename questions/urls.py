from . import views
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', views.detailView, name='detail'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
    path('success/', views.success, name='success'),
    path('select/', views.select, name='select'),
    path('<int:pk>/problem/', views.problem, name='problem'),
    path('nope/', views.nope, name='nope'),
    path('score/', views.score, name="score")
]