'''
 # @ Author: WouRaoyu
 # @ Create Time: 2024-07-10 14:42:51
 # @ Modified by: WouRaoyu
 # @ Modified time: 2024-07-10 15:43:49
 # @ Description:
 '''

import os
import random
from pathlib import Path

from rest_framework import serializers

from geoinfo.models import JudgeInfo

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / 'static/'

BASE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class JudgeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeInfo
        fields = '__all__'

class JudgeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = JudgeInfo
        fields = ('dtId', 'project', 'mileage', 'conclusion', 'rockLevel')
    
def generate_serial():
    return ''.join(random.choices(BASE_CHARS, k=16))

def handle_uploaded_file(f, fmt):
    if not os.path.exists(STATIC_DIR):
        os.makedirs(STATIC_DIR)
    filename = 'static/' + generate_serial() + fmt
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename