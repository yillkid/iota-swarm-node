import ctypes
import sys
from iota import TryteString


def PoW_load_library(DCURL_PATH):
    try:
        libdcurl = ctypes.cdll.LoadLibrary(DCURL_PATH)
        libdcurl.dcurl_entry.argtypes = [ctypes.c_char_p, ctypes.c_int]
        libdcurl.dcurl_entry.restype = ctypes.c_char_p
        return libdcurl
    except BaseException:
        return None


def PoW_interface_init(lib):
    if (lib) is not None:
        lib.dcurl_init()

# return nonce
def PoW_interface_search(lib, tryte, mwm):
    if lib is not None:
        # Do the PoW
        ctryte = str(tryte).encode('ascii')
        ret = lib.dcurl_entry(ctryte, mwm)

        # Get the nonce
        ret_tryte = TryteString(ret[:2673])
        return str(ret_tryte[-27:])
