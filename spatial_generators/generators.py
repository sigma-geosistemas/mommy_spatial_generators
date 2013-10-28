# -*- coding:utf-8 -*-
"""
Generators are callables that return a value used to populate a field.

In this module we have all the spatial generators.

The default SRID being generated is 4326, corresponding to WGS84.

The LineString and Polygon generators are harder do implement solely based on randomness.
We might need to use regular polygon/linestring approach for them.
"""
from random import randint, choice, random
from django.contrib.gis.geos import Point
from model_mommy.generators import gen_integer

def gen_point(min_x=-180,
              min_y=-90,
              max_x=190,
              max_y=90,
              min_z=None,
              max_z=None,
              srid=4326):

    """Generates a random point with x, y, optional z and a SRID. Only coordinates are random, SRID is fixed by user."""

    x = random() * gen_integer(min_x, max_x)
    y = random() * gen_integer(min_y, max_y)

    if min_z is not None and max_z is not None:
        z = random() * gen_integer(min_z, max_z)
        return Point(x=x, y=y, z=z, srid=srid)

    return Point(x=x, y=y, srid=srid)


def gen_linestring(number_of_points=2,
                   min_x=-180,
                   min_y=-90,
                   max_x=180,
                   max_y=90,
                   min_z=None,
                   max_z=None,
                   srid=4326):

    """Generates a random linestring, based on random points. optional z and SRID."""
    
    points = []

    for i in range(1, number_of_points + 1):

        points.append(gen_point(min_x,
                                min_y,
                                max_x,
                                max_y,
                                min_z,
                                max_z,
                                srid))

    return LineString(points)

def gen_rectangular_polygon(min_x=-1,
                            min_y=-1,
                            max_x=1,
                            max_y=1,
                            srid=4326):

    """Generates a rectangular polygon, based on minxy and maxxy."""

    point_a = Point(x=min_x, y=min_y, srid=srid)
    point_b = Point(x=min_x, y=max_y, srid=srid)
    point_c = Point(x=max_x, y=max_y, srid=srid)
    point_d = Point(x=max_x, y=min_y, srid=srid)
    point_e = Point(x=min_x, y=min_y, srid=srid)

    return Polygon(LinearRing([point_a, point_b, point_c, point_d, point_e]), srid=srid)


MOMMY_SPATIAL_FIELDS = {"django.contrib.gis.db.models.PointField": gen_point,
                        "django.contrib.gis.db.models.LineStringField": gen_linestring,
                        "django.contrib.gis.db.models.PolygonField": gen_rectangular_polygon}
