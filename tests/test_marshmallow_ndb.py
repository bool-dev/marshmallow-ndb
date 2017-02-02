# -*- coding: utf-8 -*-
from __future__ import absolute_import

from google.appengine.ext import ndb


class DummyModel(ndb.Model):
    some_property = ndb.StringProperty()


class TestModel(object):

    def test_assert(self):
        assert True
