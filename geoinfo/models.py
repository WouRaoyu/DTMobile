'''
 # @ Author: WouRaoyu
 # @ Create Time: 2024-07-10 14:08:07
 # @ Modified by: WouRaoyu
 # @ Modified time: 2024-07-10 15:43:58
 # @ Description:
 '''

from django.db import models

class JudgeInfo(models.Model):
    dtId = models.AutoField(primary_key=True)
    project = models.CharField(max_length=255, verbose_name="工程名称")
    mileage = models.CharField(max_length=255, verbose_name="施工里程")
    width = models.DecimalField(max_digits=10, decimal_places=2, default=8.8, null=True, verbose_name="开挖宽度")
    height = models.DecimalField(max_digits=10, decimal_places=2, default=8.8, null=True, verbose_name="开挖高度")
    excavation = models.CharField(max_length=255, verbose_name="开挖方式")
    lithology = models.CharField(max_length=255, verbose_name="岩石类型")
    conclusion = models.TextField(blank=True, verbose_name="综合结论")

    rockLevel = models.IntegerField(verbose_name="围岩等级")
    rockLevelDesc = models.TextField(blank=True, verbose_name="围岩等级描述")
    rockLevelImg = models.CharField(max_length=255, verbose_name="围岩等级研判图")
    
    fragment = models.IntegerField(verbose_name="破碎程度")
    fragmentDesc = models.TextField(blank=True, verbose_name="破碎程度描述")
    fragmentImg = models.CharField(max_length=255, verbose_name="破碎程度研判图")
    
    hardness = models.IntegerField(verbose_name="坚硬程度")
    hardnessDesc = models.TextField(blank=True, verbose_name="坚硬程度描述")
    hardnessImg = models.CharField(max_length=255, verbose_name="坚硬程度研判图")

    watery = models.IntegerField(verbose_name="富水程度")
    wateryDesc = models.TextField(blank=True, verbose_name="富水程度描述")
    wateryImg = models.CharField(max_length=255, verbose_name="富水程度研判图")
    
    geostress = models.IntegerField(verbose_name="地应力状态")
    geostressDesc = models.TextField(blank=True, verbose_name="地应力状态描述")
    geostressImg = models.CharField(max_length=255, verbose_name="地应力状态研判图")
    
    realScene = models.IntegerField(verbose_name="高清影像")
    realSceneDesc = models.TextField(blank=True, verbose_name="高清影像描述")
    realSceneImg = models.CharField(max_length=255, verbose_name="高清影像研判图")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "研判报告"
