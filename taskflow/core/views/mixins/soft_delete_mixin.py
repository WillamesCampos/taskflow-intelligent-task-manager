from rest_framework import status
from rest_framework.response import Response


class SoftDeleteMixin:
    def destroy(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        instance.is_active = False

        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
