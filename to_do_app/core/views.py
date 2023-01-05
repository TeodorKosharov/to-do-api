from rest_framework.decorators import api_view
from rest_framework.response import Response
from to_do_app.core.models import Task
from to_do_app.core.serializers import TaskSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from to_do_app.core.utils import get_appropriate_invalid_serializer_response


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
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Task created successfully!')
        return get_appropriate_invalid_serializer_response(serializer, 'create task')


class EditTask(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'name'

    def put(self, request, *args, **kwargs):
        instance = Task.objects.filter(name=request.data['currentName'])
        # currentName comes from js body part when fetching
        if instance:
            serializer = self.get_serializer(instance[0], data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('Task updated!')
            return get_appropriate_invalid_serializer_response(serializer, 'edit task')

        return Response('Task not found!')


class DeleteTask(DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'name'

    def delete(self, request, *args, **kwargs):
        instance = self.queryset.filter(name=kwargs['name'])
        if instance:
            self.destroy(request, args, kwargs)
            return Response('Task deleted!')
        return Response('Task not found!')


class ListTasks(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
