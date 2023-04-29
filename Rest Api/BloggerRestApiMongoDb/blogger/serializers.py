from rest_framework import serializers 
from blogger.models import Blogger

class BloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = ('id',
                  'userId',
                  'title',
                  'description')