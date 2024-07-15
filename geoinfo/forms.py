'''
 # @ Author: WouRaoyu
 # @ Create Time: 2024-07-10 15:56:12
 # @ Modified by: WouRaoyu
 # @ Modified time: 2024-07-10 15:56:14
 # @ Description:
 '''

from django import forms

class UploadFileForm(forms.Form):
    fmt = forms.CharField(max_length=16)
    file = forms.FileField()