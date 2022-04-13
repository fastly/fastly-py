# We can not import model classes here because that would create a circular
# reference which would not work in python2.
# Do not import all models into this module because that uses a lot of memory and stack frames.
# If you need the ability to import all models from one package, import them with
# from {{packageName}.models import ModelA, ModelB
