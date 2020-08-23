# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import shutil, os
import urllib.request as request
from contextlib import closing

def download_file(url, path: str="") -> None:
    with closing(request.urlopen(url)) as r:
        with open(path, 'wb') as f:
            print("Downloading...")
            shutil.copyfileobj(r, f)

if not os.path.exists("datafiles"):
    os.mkdir("datafiles")
download_file(r"ftp://ftp.ncdc.noaa.gov/pub/data/hourly_precip-3240/01/3240_01_1948-1998.tar.Z", "./datafiles/test.tar.Z")

# %%
import zlib, gzip, os

def decompress_gzfile(compfile, decompfile, blocksize=1024):
    file = gzip.open(compfile, 'rb')
    ofile = open(decompfile, 'wb')
    finished = False
    while not finished:
        data = file.read(blocksize)
        finished = (len(data) == 0)
        ofile.write(data)
    file.close()
    ofile.close()

def decompress_file(compfile, decompfile, blocksize: int=1024):
    if not os.path.isfile(compfile):
        print(f"Error: {compfile} is not a file!")
        return
    dc = zlib.decompressobj()

    print("initiating decompression...")
    with open(compfile, 'rb') as file:
        with open(decompfile, 'wb') as ofile:
            complete = False
            while not complete:
                data = file.read(blocksize)
                complete = (data == b"")
                try:
                    ofile.write(dc.decompress(data))
                except Exception as e:
                    if "Error -3" in str(e):
                        print(str(e))
                        dc = zlib.decompressobj(-zlib.MAX_WBITS)
                        continue
                    else:
                        raise
    print("z-decompress complete")

decompress_file("./datafiles/test.tar.Z", "./test.tar")

# %%
