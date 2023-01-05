from rest_framework.decorators import api_view
from rest_framework.response import Response
from to_do_app.core.models import Task
from to_do_app.core.serializers import TaskSerializer
from rest_framework.generics import CreateAPIView, ListAPIView


@api_view(['GET', 'POST'])
def task_details(request, name):
    found_task = Task.objects.filter(name=name)

    if found_task:
        result = {'name': found_task[0].name,
                  'difficulty': found_task[0].difficulty,
                  'priority': found_task[0].priority
                  }
    else:
        result = 'not found'
    return Response(result)


class CreateTask(CreateAPIView):
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response('Task created successfully!')


class ListTasks(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
