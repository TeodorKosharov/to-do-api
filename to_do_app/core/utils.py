def get_appropriate_serializer_error(serializer):
    if serializer.errors.get('priority'):
        return serializer.errors['priority']
    return serializer.errors['name']
