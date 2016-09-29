# coding: utf-8
from django.contrib.gis.db import models


class PointModel(models.Model):

    geometry = models.PointField()


class NonDefaultSridModel(models.Model):

    geometry = models.PointField(srid=4674)


class NonDefaultDimModel(models.Model):

    geometry = models.PointField(dim=3)
