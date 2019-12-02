"""
The TimelineType definition.
"""

from typing import List, Union

import numpy

from ._base import Serializable, DEFAULT_STRICT, \
    _FloatDescriptor, _IntegerDescriptor, _DateTimeDescriptor, \
    _SerializableDescriptor, _SerializableArrayDescriptor
from ._blocks import Poly1DType


__classification__ = "UNCLASSIFIED"


class IPPSetType(Serializable):
    """The Inter-Pulse Parameter array element container."""
    # NOTE that this is simply defined as a child class ("Set") of the TimelineType in the SICD standard
    #   Defining it at root level clarifies the documentation, and giving it a more descriptive name is
    #   appropriate.
    _fields = ('TStart', 'TEnd', 'IPPStart', 'IPPEnd', 'IPPPoly', 'index')
    _required = _fields
    _set_as_attribute = ('index', )
    # descriptors
    TStart = _FloatDescriptor(
        'TStart', _required, strict=DEFAULT_STRICT,
        docstring='IPP start time relative to collection start time, i.e. offsets in seconds.')  # type: float
    TEnd = _FloatDescriptor(
        'TEnd', _required, strict=DEFAULT_STRICT,
        docstring='IPP end time relative to collection start time, i.e. offsets in seconds.')  # type: float
    IPPStart = _IntegerDescriptor(
        'IPPStart', _required, strict=True, docstring='Starting IPP index for the period described.')  # type: int
    IPPEnd = _IntegerDescriptor(
        'IPPEnd', _required, strict=True, docstring='Ending IPP index for the period described.')  # type: int
    IPPPoly = _SerializableDescriptor(
        'IPPPoly', Poly1DType, _required, strict=DEFAULT_STRICT,
        docstring='IPP index polynomial coefficients yield IPP index as a function of time.')  # type: Poly1DType
    index = _IntegerDescriptor(
        'index', _required, strict=DEFAULT_STRICT, docstring='The element array index.')  # type: int


class TimelineType(Serializable):
    """The details for the imaging collection timeline."""
    _fields = ('CollectStart', 'CollectDuration', 'IPP')
    _required = ('CollectStart', 'CollectDuration', )
    _collections_tags = {'IPP': {'array': True, 'child_tag': 'Set'}}
    # descriptors
    CollectStart = _DateTimeDescriptor(
        'CollectStart', _required, strict=DEFAULT_STRICT, numpy_datetime_units='us',
        docstring='The collection start time. The default precision will be microseconds.')  # type: numpy.datetime64
    CollectDuration = _FloatDescriptor(
        'CollectDuration', _required, strict=DEFAULT_STRICT,
        docstring='The duration of the collection in seconds.')  # type: float
    IPP = _SerializableArrayDescriptor(
        'IPP', IPPSetType, _collections_tags, _required, strict=DEFAULT_STRICT, minimum_length=1,
        docstring="The Inter-Pulse Period (IPP) parameters array.")  # type: Union[numpy.ndarray, List[IPPSetType]]