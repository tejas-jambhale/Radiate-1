from . import views
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', views.detailView, name='detail'),
    path('success/', views.success, name='success'),
    path('<int:question_id>/answer/', views.answer, name='answer')
]