from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Platform
from .serializers import PlatformSerializer
from rest_framework.response import Response
from rest_framework import status


class PlatformApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):  # read
        platform = Platform.objects.all()
        data = PlatformSerializer(instance=platform, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):  # create
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


