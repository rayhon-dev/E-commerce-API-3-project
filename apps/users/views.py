from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.users.serializers import UserProfileSerializer
from rest_framework.response import Response


class UserProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "success": True,
                "data": serializer.data
            })
        else:
            error_field = next(iter(serializer.errors))
            error_message = serializer.errors[error_field][0]
            return Response({
                "success": False,
                "error": {
                    "code": "INVALID_REQUEST",
                    "message": "The provided data is invalid",
                    "details": {
                        "field": error_field,
                        "message": error_message
                    }
                }
            }, status=400)
