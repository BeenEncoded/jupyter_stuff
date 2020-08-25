# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import shutil, os
import urllib.request as request
from contextlib import closing

def uncompress_raindata(path: str="") -> None:
    newfolder = (os.path.dirname(path) + os.path.sep + os.path.splitext(os.path.basename(path))[0])
    if not os.path.isdir(newfolder): os.mkdir(newfolder)
    newpath = newfolder + os.path.sep + os.path.basename(path)
    if os.path.isfile(newpath): os.remove(newpath)
    shutil.move(path, newfolder)
    !uncompress -rNf $newpath

    #so if we uncompress as we walk we will invalidate the iterator.  Shit will hit the fan.
    # We need to create a list of paths and then uncompress them after walking.
    uncompresslist = []
    for root, folders, files in os.walk(newfolder): 
        for file in files:
            uncompresslist.append(root + os.path.sep + file)
    for file in uncompresslist:
        print(f"Uncompressing {file}")
        !tar --overwrite --directory=$newfolder -xf $file
    print("Decompression complete!")

def download_file(url, path: str="") -> None:
    if os.path.exists(path): return
    with closing(request.urlopen(url)) as r:
        with open(path, 'wb') as f:
            print("Downloading...")
            shutil.copyfileobj(r, f)

if not os.path.exists("datafiles"):
    os.mkdir("datafiles")

download_file(r"ftp://ftp.ncdc.noaa.gov/pub/data/hourly_precip-3240/09", "./datafiles/test")
if os.path.exists("./datafiles/test.tar.Z"): print("Downloaded Successfully!")
else: print("Download failed!")

#uncompress_raindata("./datafiles/test.tar.Z")
# %%
