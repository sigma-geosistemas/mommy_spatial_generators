Model Mommy Spatial Generators
==============================

This package contains spatial generators to be used with model_mommy.

Model Mommy is a Django package that creates random model instances with
predefined data.

This work intends to expand it and allow it to generate GeoDjango spatial
fields.

At this moment, there is a generator for point (random), linestring (random)
and polygon (rectangular polygon) field types.

This needs substantial help with packaging and testing.

All new ideas welcome.

# How to make this work

To integrate this work with model_mommy, you need to create a dict variable
on your settings.py called MOMMY_CUSTOM_FIELDS_GEN and concatenate the already
predefined dict we provide (MOMMY_SPATIAL_FIELDS), located in generators.py.

model_mommy should take of the rest.