# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import shutil, os
import urllib.request as request
from contextlib import closing

def uncompress_raindata(path: str="") -> None:
    newfolder = (os.path.dirname(path) + os.path.sep + os.path.splitext(os.path.basename(path))[0])
    os.mkdir(newfolder)
    shutil.move(path, newfolder)
    path = newfolder + os.path.sep + os.path.basename(path)
    !uncompress $path

def download_file(url, path: str="") -> None:
    if os.path.exists(path): return
    with closing(request.urlopen(url)) as r:
        with open(path, 'wb') as f:
            print("Downloading...")
            shutil.copyfileobj(r, f)

if not os.path.exists("datafiles"):
    os.mkdir("datafiles")
download_file(r"ftp://ftp.ncdc.noaa.gov/pub/data/hourly_precip-3240/91/3240_91_2011-2011.tar.Z", "./datafiles/test.tar.Z")
if os.path.exists("./datafiles/test.tar.Z"): print("Downloaded Successfully!")
else: print("Download failed!")

uncompress_raindata("./datafiles/test.tar.Z")
# %%
