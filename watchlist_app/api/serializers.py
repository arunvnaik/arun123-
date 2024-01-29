from rest_framework import serializers 
from watchlist_app.models import WatchList,StreamPlatform,Review





class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
    

    
    
class StreamPlatformSerializer(serializers.ModelSerializer):
#    watch= WatchListSerializer( many=True,read_only=True)
   
   class Meta:
        model =StreamPlatform
        fields ="__all__" 
        


class WatchListSerializer(serializers.ModelSerializer):
     reviews = ReviewSerializer(many=True, read_only=True)  # Nested representation of review platform = StreamPlatformSerializer()  # Nested representation of platform

    # reviews = ReviewSerializer(many=True,read_only=True)
     class Meta:
       model=WatchList
       exclude = ["active"]
    
    
    


    







