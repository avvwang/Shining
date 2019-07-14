# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Case_version(models.Model):
    """
    主版本
    """
    file_name=models.CharField("文件名称",max_length=100)
    version=models.IntegerField("文件版本")


class Case_subversion(models.Model):
    """
    子版本
    """
    Case_sub=models.ForeignKey(to="Case_version",on_delete=models.CASCADE,related_name="sub_version")
    Case_group=models.CharField("子集",max_length=100)
    Case_name=models.CharField("子名称",max_length=200)
    Case_list=models.TextField("用例执行范围")

    def __str__(self):
        return self.Case_name


class Test_case(models.Model):
    """
    用例表
    """
    Case_for=models.ForeignKey(to="Case_subversion",on_delete=models.CASCADE,related_name="run_test")
    Case_name=models.CharField(max_length=300)
    Case_number=models.IntegerField()
    Case_tips=models.CharField(max_length=200)
    Case_step=models.TextField()


class Case_run(models.Model):
    """
    用例执行表
    """
    user=models.CharField(max_length=100)
    Case=models.ForeignKey(to="Test_case",on_delete=models.CASCADE,related_name="run_Test")
    version=models.ForeignKey(to="Case_subversion",on_delete=models.CASCADE,related_name="run_subversion")
    result=models.IntegerField("测试结果")

    def __str__(self):
        return self.user

