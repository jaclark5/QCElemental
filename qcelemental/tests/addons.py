import socket

import pytest

from qcelemental.util import which_import


def internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

using_web = pytest.mark.skipif(internet_connection() is False, reason="Could not connect to the internet")

using_msgpack = pytest.mark.skipif(
    which_import('msgpack', return_bool=True) is False,
    reason='Not detecting module msgpack. Install package if necessary and add to envvar PYTHONPATH')

using_networkx = pytest.mark.skipif(
    which_import('networkx', return_bool=True) is False,
    reason='Not detecting module networkx. Install package if necessary and add to envvar PYTHONPATH')

using_scipy = pytest.mark.skipif(
    which_import('scipy', return_bool=True) is False,
    reason='Not detecting module scipy. Install package if necessary and add to envvar PYTHONPATH')

using_py3dmol = pytest.mark.skipif(
    which_import('py3Dmol', return_bool=True) is False,
    reason='Not detecting module py3Dmol. Install package if necessary and add to envvar PYTHONPATH')
