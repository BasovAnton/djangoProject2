from django.urls import path

from blog_api import views

urlpatterns = [
    path('notes/', views.NoteListCreateAPIView.as_view()),
    path('notes/<int:pk>/', views.NoteDetailAPIView.as_view()),
    path('notes/public/', views.NotePublicListAPIView.as_view())
]
