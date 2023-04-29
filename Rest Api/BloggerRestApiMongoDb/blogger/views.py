from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from blogger.models import Blogger
from blogger.serializers import BloggerSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def blogger_list(request,user_id):
    try:
        print("user_id: " + user_id)
        blogger = Blogger.objects.filter(userId=user_id)
        blogger_serializer = BloggerSerializer(blogger,many=True)
        return JsonResponse(blogger_serializer.data,safe=False)
    except Blogger.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    

 
@api_view(['GET'])
def blogger_detail(request,id):
    try:
        blogger= Blogger.objects.get(id=id)
        blogger_serializer = BloggerSerializer(blogger,many=False)
        return JsonResponse(blogger_serializer.data,safe=False)
    except Blogger.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist for'+id}, status=status.HTTP_404_NOT_FOUND)   
    

@api_view(['POST'])
def blogger_add(request):
    blogger_data = JSONParser().parse(request)
    blogger_serializer_data = BloggerSerializer(data=blogger_data)
    if blogger_serializer_data.is_valid():
        blogger_serializer_data.save()
        return JsonResponse(blogger_serializer_data.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(blogger_serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def blogger_delete(request,id):
    blogger=Blogger.objects.get(id=id)
    blogger.delete()
    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def blogger_update(request,id):
    blogger_data=JSONParser().parse(request)
    blogger=Blogger.objects.get(id=id)
    blogger_serializer=BloggerSerializer(blogger,data=blogger_data)
    if blogger_serializer.is_valid():
        blogger_serializer.save()
        return JsonResponse("Updated Successfully",safe=False)
    return JsonResponse("Failed to Update",safe=False)