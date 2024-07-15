'''
 # @ Author: WouRaoyu
 # @ Create Time: 2024-07-10 14:08:07
 # @ Modified by: WouRaoyu
 # @ Modified time: 2024-07-10 15:43:41
 # @ Description:
 '''

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from geoinfo.forms import UploadFileForm
from geoinfo.models import JudgeInfo
from geoinfo.serializers import JudgeInfoSerializer, JudgeListSerializer, handle_uploaded_file
from rest_framework.decorators import api_view

@api_view(['GET'])
def judge_list(request):
    judge_infos = JudgeInfo.objects.all()
    judge_list_serializer = JudgeListSerializer(judge_infos, many=True)
    return JsonResponse(judge_list_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def judge_detail(request, pk):
    try:
        judge_info = JudgeInfo.objects.get(dtId=pk)
    except JudgeInfo.DoesNotExist:
        return JsonResponse({'message': 'The JudgeInfo does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JudgeInfoSerializer(judge_info)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = JudgeInfoSerializer(judge_info, data=judge_info_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        judge_info.delete()
        return JsonResponse({'message': 'JudgeInfo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def judge_append(request):
    serializer = JudgeInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'JudgeInfo was created successfully!'}, status=status.HTTP_201_CREATED)
    return JsonResponse({'message': 'Create failed'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def upload_file(request):
    print(request.POST)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            url = handle_uploaded_file(request.FILES['file'], request.POST.get('fmt'))
            return JsonResponse({'message': 'Upload success', 'url' : url}, status=status.HTTP_201_CREATED)
    return JsonResponse({'message': 'Upload failed'}, status=status.HTTP_400_BAD_REQUEST)