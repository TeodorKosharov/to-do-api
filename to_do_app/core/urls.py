from django.urls import path
from to_do_app.core.views import task_details, CreateTask, ListTasks

urlpatterns = (
    path('create-task/', CreateTask.as_view()),
    path('details/<str:name>/', task_details),
    path('tasks/', ListTasks.as_view())
)
