from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status 
# from rest_framework import generics
from django.shortcuts import get_object_or_404
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer




# class StreamPlatformListCreateView(generics.ListCreateAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
    
class StreamPlatformListCreateView(APIView):
     def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True,context={'request': request})
        return Response(serializer.data)

     def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StreamPlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
    


class StreamPlatformDetailView(APIView):
    
    def get(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
     
    

    def put(self, request, pk):
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   
         
         
#   
class WatchListView(APIView):
    def get(self, request):
        watches = WatchList.objects.all()
        serializer = WatchListSerializer(watches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class WatchListDetailView(APIView):
    
    def get(self, request, pk):
        watch = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(watch)
        return Response(serializer.data)

    def put(self, request, pk):
        watch = get_object_or_404(WatchList, pk=pk)
        serializer = WatchListSerializer(watch, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        watch = get_object_or_404(WatchList, pk=pk)
        watch.delete()
        return Response({'message': 'WatchList deleted successfully'}, status==status.HTTP_204_NO_CONTENT)
           
         
         
