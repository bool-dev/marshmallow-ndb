# -*- coding: utf-8 -*-
from marshmallow import fields as mndb_fields

from google.appengine.ext import ndb


TYPE_MAPPING = {
    ndb.IntegerProperty: fields.Integer,
    ndb.FloatProperty: fields.Float,
    ndb.BooleanProperty: fields.Boolean,
    ndb.StringProperty: fields.String,
    ndb.TextProperty: fields.String,
    ndb.BlobProperty: fields.Raw,
    ndb.DateTimeProperty: fields.DateTime,
    ndb.DateProperty: fields.Date,
    ndb.TimeProperty: fields.Time,
    ndb.GeoPtProperty: mndb_fields.GeoField,
    ndb.KeyProperty: mndb_fields.KeyField,
    ndb.BlobKeyProperty: fields.Raw,
    ndb.UserProperty: fields.Raw,
    ndb.StructuredProperty: fields.List,
    ndb.LocalStructuredProperty: fields.List,
    ndb.JsonProperty: fields.Raw,
    ndb.PickleProperty: fields.Raw,
    ndb.GenericProperty: fields.Raw,
    ndb.ComputedProperty: fields.Raw,
}
