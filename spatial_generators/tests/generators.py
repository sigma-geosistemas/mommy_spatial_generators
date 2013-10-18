# coding: utf-8

from django.test import TestCase
from model_mommy import mommy
from test.generic.models import PointModel, NonDefaultSridPointModel, NonDefaultDimPointModel
from model_mommy.spatial_generators import gen_point
from django.contrib.gis.geos import Point

class PointGeneratorTestCase(TestCase):

    """
    Tests that the generator correctly
    generates points with the parameters passed
    on to it
    """

    def test_point_is_point(self):

        point = gen_point()
        self.assertIsInstance(point, Point)

    def test_point_default_srid(self):

        """
        Test that asserts that the default srid
        generated is correct
        """

        point = gen_point()
        self.assertEqual(point.srid, 4326)

    def test_point_different_srid(self):

        """
        Tests that the appointed srid will be used for
        generating the point
        """

        point = gen_point(srid=4674) # SIRGAS 2000
        self.assertEqual(point.srid, 4674)

    def test_point_is_within_bounds(self):

        """
        Test that the generator respects the bounds passed on to it.
        """

        point = gen_point(0, 0, 10, 10)
        self.assertGreaterEqual(point.x, 0)
        self.assertGreaterEqual(point.y, 0)
        self.assertLessEqual(point.x, 10)
        self.assertLessEqual(point.y, 10)

    def test_point_with_z(self):

        """
        Test that makes sure that when z arguments are
        passed, the generator accounts for them
        """

        point = gen_point(min_z=0, max_z=1)
        self.assertGreaterEqual(point.z, 0)
        self.assertLessEqual(point.z, 1)


class PointModelTestCase(TestCase):

    """Test case to cover the generation of pointFields within a model."""

    def test_point_is_not_empty(self):

        """
        Asserts that a model with a PointField
        correctly generates a non-empty point geometry
        """

        point_model = mommy.make(PointModel)
        self.assertIsInstance(point_model, PointModel)
        self.assertFalse(point_model.geometry.empty)

    def test_point_is_point(self):

        """
        Asserts that a model with a PointField
        correctly genreates a Point GEOS Geometry
        """

        point_model = mommy.make(PointModel)
        self.assertIsInstance(point_model, PointModel)
        self.assertEqual(point_model.geometry.geom_type, "Point")

    def test_non_default_srid_field(self):

        point_model = mommy.make(NonDefaultSridPointModel)
        self.assertIsInstance(point_model, NonDefaultSridPointModel)
        self.assertEqual(point_model.geometry.srid, 4674)

    def test_non_default_dimensions(self):

        point_model = mommy.make(NonDefaultDimPointModel)
        self.assertIsInstance(point_model, NonDefaultDimPointModel)
        self.assertTrue(point_model.geometry.hasz)

