# -*- coding: utf-8 -*-
"""no-payload packet

:mod:`pcapkit.protocols.null` contains
:class:`~pcapkit.protocols.null.NoPayload` only, which
implements a :class:`~pcapkit.protocols.protocol.Protocol` like
object whose payload is recursively
:class:`~pcapkit.protocols.null.NoPayload` itself.

"""
import io

from pcapkit.corekit.infoclass import Info
from pcapkit.corekit.protochain import ProtoChain
from pcapkit.protocols.protocol import Protocol
from pcapkit.utilities.exceptions import UnsupportedCall

__all__ = ['NoPayload']


class NoPayload(Protocol):
    """This class implements no-payload protocol."""

    ##########################################################################
    # Properties.
    ##########################################################################

    # name of current protocol
    @property
    def name(self):
        """Name of current protocol.

        :rtype: Literal['Null']
        """
        return 'Null'

    # header length of current protocol
    @property
    def length(self):
        """Header length of current protocol.

        Raises:
            UnsupportedCall: This protocol doesn't support :attr:`length`.

        """
        raise UnsupportedCall(f"'{self.__class__.__name__}' object has no attribute 'length'")

    # name of next layer protocol
    @property
    def protocol(self):
        """Name of next layer protocol.

        Raises:
            UnsupportedCall: This protocol doesn't support :attr:`protocol`.

        """
        raise UnsupportedCall(f"'{self.__class__.__name__}' object has no attribute 'protocol'")

    ##########################################################################
    # Data models.
    ##########################################################################

    def __new__(cls, *args, **kwargs):  # pylint: disable=signature-differs
        self = super().__new__(cls)
        return self

    def __init__(self, *args, **kwargs):  # pylint: disable=super-init-not-called
        """Initialisation.

        Args:
            *args: Arbitrary positional arguments.

        Keyword Args:
            **kwargs: Arbitrary keyword arguments.

        """
        #: pcapkit.protocols.null.NoPayload: Payload of current instance.
        self._next = self
        #: pcapkit.corekit.infoclass.Info: Info dict of current instance.
        self._info = Info()
        #: io.BytesIO: Source data stream.
        self._file = io.BytesIO()
        #: pcapkit.corekit.protochain.ProtoChain: Protocol chain of current instance.
        self._protos = ProtoChain()

    @classmethod
    def __index__(cls):
        """Numeral registry index of the protocol.

        Raises:
            UnsupportedCall: This protocol has no registry entry.

        """
        raise UnsupportedCall(f'{cls.__name__!r} object cannot be interpreted as an integer')

    ##########################################################################
    # Utilities.
    ##########################################################################

    def _decode_next_layer(self, *args, **kwargs):  # pylint: disable=signature-differs
        """Decode next layer protocol.

        Args:
            *args: arbitrary positional arguments

        Keyword Args:
            **kwargs: arbitrary keyword arguments

        Raises:
            UnsupportedCall: This protocol doesn't support :meth:`_decode_next_layer`.

        """
        raise UnsupportedCall(f"'{self.__class__.__name__}' object has no attribute '_decode_next_layer'")

    def _import_next_layer(self, *args, **kwargs):  # pylint: disable=signature-differs
        """Import next layer extractor.

        Args:
            *args: arbitrary positional arguments

        Keyword Args:
            **kwargs: arbitrary keyword arguments

        Raises:
            UnsupportedCall: This protocol doesn't support :meth:`_import_next_layer`.

        """
        raise UnsupportedCall(f"'{self.__class__.__name__}' object has no attribute '_import_next_layer'")
