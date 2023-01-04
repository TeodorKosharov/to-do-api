from django.urls import path
from to_do_app.core.views import CreateTask, task_details

urlpatterns = (
    path('create-task/', CreateTask.as_view(), name='create task'),
    path('details/<str:name>/', task_details, name='details task')
)
