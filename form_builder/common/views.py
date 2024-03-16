from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.tasks import create_random_user_accounts


class CreateRandomUserView(APIView):
    """
    Just a simple test view to trigger the task
    """
    def get(self, request, count):
        try:
            create_random_user_accounts.delay(int(count))
        except Exception as e:
            # Managed in the custom renderer
            self.error_message = str(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # Managed in the custom renderer
        self.success_message = "Random user accounts task started successfully!"
        return Response(status=status.HTTP_200_OK)