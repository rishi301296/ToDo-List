from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from api import utils as api_utils


class AddTask(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        View to add tasks
        """
        return api_utils.response("Task added successfully", status.HTTP_200_OK)


class ShowTaskList(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        View to show all tasks
        """
        return api_utils.response("No tasks to show", status.HTTP_200_OK)


class RemoveTask(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Loads LOVs from a xlsx file (present locally on server)
        """
        return api_utils.response("No tasks to remove", status.HTTP_200_OK)
