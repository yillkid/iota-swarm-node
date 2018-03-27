import ctypes
import sys
import _thread
import time
from iota import TryteString

DCURL_PATH = "./libdcurl.so"

def load_PoW_library():
    libdcurl = ctypes.cdll.LoadLibrary(DCURL_PATH)
    libdcurl.dcurl_init.argtypes = [ctypes.c_int, ctypes.c_int]
    libdcurl.dcurl_entry.argtypes = [ctypes.c_char_p, ctypes.c_int]
    libdcurl.dcurl_entry.restype = ctypes.c_char_p
    return libdcurl

if __name__ == "__main__":
    # Arguments
    tryte = sys.argv[1]
    mwm = int(sys.argv[2])

    # PoW
    lib = load_PoW_library()
    lib.dcurl_init(1, 0)
    c_trytes = str(tryte).encode('ascii')
    ret = lib.dcurl_entry(c_trytes, mwm)
    
    # Get the nonce
    ret_tryte = TryteString(ret[:2673])
    print(ret_tryte[-27:])
