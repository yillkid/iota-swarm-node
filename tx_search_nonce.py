import ctypes
import sys
import _thread
import time

if __name__ == "__main__":

    trytes = sys.argv[1]

    dcurlPath = "./libdcurl.so"

    libdcurl = ctypes.cdll.LoadLibrary(dcurlPath)

    libdcurl.dcurl_init()

    libdcurl.dcurl_entry.argtypes = [ctypes.c_char_p, ctypes.c_int]

    c_trytes = str(trytes).encode('ascii')

    libdcurl.dcurl_entry(c_trytes, 14)
