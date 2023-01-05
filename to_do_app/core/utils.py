from rest_framework.response import Response


def get_appropriate_invalid_serializer_response(serializer, action):
    if action == 'create task':
        if serializer.errors.get('name'):
            return Response('Task with this name already exists!')
    if serializer.errors.get('difficulty') and serializer.errors.get('priority'):
        return Response('Difficulty and priority values are invalid!')
    elif serializer.errors.get('difficulty'):
        return Response('Difficulty can be easy/medium/hard!')
    elif serializer.errors.get('priority'):
        return Response('Priority must be an positive integer!')
