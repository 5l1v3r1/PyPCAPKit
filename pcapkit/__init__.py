# -*- coding: utf-8 -*-
"""stream pcap file extractor

`pcapkit` is an independent open source library, using only
[`dictdumper`](https://github.com/JarryShaw/dictdumper) as
its formatted output dumper.

    There is a project called
    [`jspcapy`](https://github.com/JarryShaw/jspcapy)
    works on `pcapkit`, which is a command line tool for
    PCAP extraction.

Unlike popular PCAP file extractors, such as `Scapy`,
`dpkt`, `pyshark`, and etc, `pcapkit` uses streaming
strategy to read input files. That is to read frame by
frame, decrease occupation on memory, as well as enhance
efficiency in some way.

In `pcapkit`, all files can be described as following eight
different sections.

 - Interface (`pcapkit.interface`)
    user interface for the `pcapkit` library, which
    standardise and simplify the usage of this
    library

 - Foundation (`pcapkit.foundation`)
    synthesise file I/O and protocol analysis, coordinate
    information exchange in all network layers

 - Reassembly (`pcapkit.reassembly`)
    base on algorithms described in
    [`RFC 815`](https://tools.ietf.org/html/rfc815>),
    implement datagram reassembly of IP and TCP packets

 - IPSuite (`pcapkit.ipsuite`)
    collection of constructors for Internet Protocol Suite

 - Protocols (`pcapkit.protocols`)
    collection of all protocol family, with detailed
    implementation and methods

 - Utilities (`pcapkit.utilities`)
    collection of utility functions and classes

 - CoreKit (`pcapkit.corekit`)
    core utilities for `pcapkit` implementation

 - ToolKit (`pcapkit.toolkit`)
    utility tools for `pcapkit` implementation

 - DumpKit (`pcapkit.dumpkit`)
    dump utilities for `pcapkit` implementation

"""
# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import
import os
import warnings

import tbtrim

from pcapkit.utilities.exceptions import DEVMODE, BaseError

# set up sys.excepthook
if DEVMODE:
    warnings.showwarning('development mode enabled', RuntimeWarning,
                         filename=__file__, lineno=0,
                         line="PCAPKIT_DEVMODE={}".format(os.environ['PCAPKIT_DEVMODE']))
else:
    ROOT = os.path.dirname(os.path.realpath(__file__))
    tbtrim.set_trim_rule(lambda filename: ROOT in os.path.realpath(filename),
                         exception=BaseError, strict=False)

# All Reference
import pcapkit.__all__ as all  # pylint: disable=redefined-builtin

# Interface
from pcapkit.interface import *

# ToolKit
from pcapkit.toolkit import *

# Protocols
from pcapkit.protocols.null import NoPayload
from pcapkit.protocols.raw import Raw
from pcapkit.protocols.link.arp import ARP
from pcapkit.protocols.link.ethernet import Ethernet
from pcapkit.protocols.application.ftp import FTP
from pcapkit.protocols.link.l2tp import L2TP
from pcapkit.protocols.link.ospf import OSPF
from pcapkit.protocols.link.rarp import RARP
from pcapkit.protocols.link.vlan import VLAN
from pcapkit.protocols.internet.ah import AH
from pcapkit.protocols.internet.hip import HIP
from pcapkit.protocols.internet.hopopt import HOPOPT
from pcapkit.protocols.internet.ip import IP
from pcapkit.protocols.internet.ipsec import IPsec
from pcapkit.protocols.internet.ipv4 import IPv4
from pcapkit.protocols.internet.ipv6 import IPv6
from pcapkit.protocols.internet.ipv6_frag import IPv6_Frag
from pcapkit.protocols.internet.ipv6_opts import IPv6_Opts
from pcapkit.protocols.internet.ipv6_route import IPv6_Route
from pcapkit.protocols.internet.ipx import IPX
from pcapkit.protocols.internet.mh import MH
from pcapkit.protocols.transport.tcp import TCP
from pcapkit.protocols.transport.udp import UDP
from pcapkit.protocols.application.http import HTTP

__all__ = [
    'extract', 'analyse', 'reassemble', 'trace',            # Interface Functions
    'TREE', 'JSON', 'PLIST', 'PCAP',                        # Format Macros
    'LINK', 'INET', 'TRANS', 'APP', 'RAW',                  # Layer Macros
    'DPKT', 'Scapy', 'PyShark', 'MPServer', 'MPPipeline', 'PCAPKit',
                                                            # Engine Macros  # pylint: disable=bad-continuation
    'NoPayload',                                            # No Payload
    'Raw',                                                  # Raw Packet
    'ARP', 'Ethernet', 'L2TP', 'OSPF', 'RARP', 'VLAN',      # Link Layer
    'AH', 'IP', 'IPsec', 'IPv4', 'IPv6', 'IPX',             # Internet Layer
    'HIP', 'HOPOPT', 'IPv6_Frag', 'IPv6_Opts', 'IPv6_Route', 'MH',
                                                            # IPv6 Extension Header  # pylint: disable=bad-continuation
    'TCP', 'UDP',                                           # Transport Layer
    'FTP', 'HTTP',                                          # Application Layer
]
