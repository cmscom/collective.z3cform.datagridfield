# -*- coding: utf-8 -*-

from z3c.form.interfaces import IMultiWidget
from zope.schema.interfaces import IObject
from zope.schema.interfaces import ValidationError


class IDataGridField(IMultiWidget):
    """Grid widget."""


class AttributeNotFoundError(ValidationError):
    """An attribute is missing from the class"""

    def __init__(self, fieldname, schema):
        self.fieldname = fieldname
        self.schema = schema
        self.__doc__ = u'Missing Field {0} required by schema {1}'.format(
            fieldname,
            schema
        )


class IRow(IObject):
    """A row. The schema defines dict keys.
    """
