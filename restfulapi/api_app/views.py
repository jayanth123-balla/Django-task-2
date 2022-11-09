from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AssetSerializer
from .models import Asset2


class Assetviews(APIView):
    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
	
    def get(self, request,id=None):
        
        if id:
            item = Asset2.objects.get(id=id)
            paginator = Paginator(item,2)
            serializer = AssetSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Asset2.objects.all()
        serializer = AssetSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    
    def patch(self, request, id=None):
        item = Asset2.objects.get(id=id)
        serializer = AssetSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors}) 
            
    
