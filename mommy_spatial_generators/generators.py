# -*- coding:utf-8 -*-
"""
Generators are callables that return a value used to populate a field.

In this module we have all the spatial generators.

The default SRID being generated is 4326, corresponding to WGS84.

The LineString and Polygon generators are harder do implement solely based on randomness.
We might need to use regular polygon/linestring approach for them.
"""
from random import randint, choice, random
from django.contrib.gis.geos import (Point,
                                     MultiPoint,
                                     LineString,
                                     MultiLineString,
                                     Polygon,
                                     MultiPolygon,
                                     LinearRing, )
try:
    from model_mommy.generators import gen_integer
except:
    from model_mommy.random_gen import gen_integer


def gen_point(min_x=-180,
              min_y=-90,
              max_x=180,
              max_y=90,
              min_z=None,
              max_z=None,
              granularity=1000,
              srid=4326):

    """
    Generates a random point with x, y, optional z and a SRID.
    Only coordinates are random, SRID is fixed by user.
    granularity specifies the precision of the generated coordinates
    (1000 by default for 0.001 as smallest diff).
    """

    x = gen_integer(int(min_x * granularity), int(max_x * granularity)) / float(granularity)
    y = gen_integer(int(min_y * granularity), int(max_y * granularity)) / float(granularity)

    if min_z is not None and max_z is not None:
        z = gen_integer(int(min_z * granularity), int(max_z * granularity)) / float(granularity)
        return Point(x=x, y=y, z=z, srid=srid)

    return Point(x=x, y=y, srid=srid)


def gen_multipoint(min_x=-180,
                   min_y=-90,
                   max_x=180,
                   max_y=90,
                   min_z=None,
                   max_z=None,
                   min_points=1,
                   max_points=2,
                   srid=4326):
    points = []

    for i in range(min_points, max_points+1):
        points.append(gen_point(min_x,
                                min_y,
                                max_x,
                                max_y,
                                min_z,
                                max_z,
                                srid))

    return MultiPoint(points)


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


def gen_multilinestring(number_of_points=2,
                        min_x=-180,
                        min_y=-90,
                        max_x=180,
                        max_y=90,
                        min_z=None,
                        max_z=None,
                        min_linestrings=1,
                        max_linestrings=2,
                        srid=4326):

    return MultiLineString([gen_linestring(number_of_points, min_x, min_y, max_x, max_y, srid) for i in range(randint(min_linestrings, max_linestrings)+1)])


def gen_rectangular_polygon(min_x=-1,
                            min_y=-1,
                            max_x=1,
                            max_y=1,
                            srid=4326):

    """Generates a rectangular polygon, based on minxy and maxxy."""
    point_a = gen_point()
    point_b = Point(x=point_a.x, y=point_a.y + 1, srid=srid)
    point_c = Point(x=point_a.x + 1, y=point_a.y + 1, srid=srid)
    point_d = Point(x=point_a.x + 1, y=point_a.y, srid=srid)
    point_e = point_a.clone()
    return Polygon(LinearRing([point_a, point_b, point_c, point_d, point_e]),
                   srid=srid)


def gen_rectangular_multipolygon(min_x=-1,
                                 min_y=-1,
                                 max_x=1,
                                 max_y=1,
                                 min_polys=1,
                                 max_polys=2,
                                 srid=4326):

    """Generates a multipolygon, based on minxy and maxxy."""
    return MultiPolygon([gen_rectangular_polygon(min_x, min_y, max_x, max_y, srid) for i in range(gen_integer(min_polys, max_polys+1))])

MOMMY_SPATIAL_FIELDS = {
    "django.contrib.gis.db.models.PointField": gen_point,
    "django.contrib.gis.db.models.MultiPointField": gen_multipoint,
    "django.contrib.gis.db.models.LineStringField": gen_linestring,
    "django.contrib.gis.db.models.MultiLineStringField": gen_multilinestring,
    "django.contrib.gis.db.models.PolygonField": gen_rectangular_polygon,
    "django.contrib.gis.db.models.MultiPolygonField": gen_rectangular_multipolygon
    }
