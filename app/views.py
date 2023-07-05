from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .helper import originalAI
import json
from .serializers import APIInputCheckup


@method_decorator(csrf_exempt, name='dispatch')
class originalAITest(APIView):
    def post(self, request ):

        content = request.data.get('content')
        title = request.data.get('title')

        field = {
            "content": content,
            "title": title
        }

        serializer = APIInputCheckup(data=field)
        if serializer.is_valid():
            return Response("All ok")
            response = originalAI(content, title)
            data = json.loads(response)
            return Response({
                "success": True,
                "message": "The test was successful",
                "data": data
            },status=status.HTTP_200_OK)
        else:
            return Response({
                "success": False,
                "message": "The test was not successful",
            },status=status.HTTP_200_OK)
    