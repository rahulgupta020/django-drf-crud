from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='task-retrieve-update-delete'),
    # path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
]
