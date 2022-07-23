# e621-downloader
Downloads your favorite things from that umami NSFW furry art site

## Still testing; may or may not work atm

## Set Up
### Mac and Linux
On UNIX/LINUX systems, simply download the `e621-fav-downloads.py` in whatever manner you choose. Chances are that the necessary packages will be installed on your system already.

### Windows (STILL IN PROGRESS - see caveats down below)
Windows makes me sad :(

If Windows complains about missing the 'requests' module, open Command Prompt with admin privileges and use the following commands:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip3 install requests
```
Should help... hopefully
## Usage
---

TBA

Caveats on Windows:
Since Windows doesn't have wget by default and curl doesn't seem to work nicely with saving files inside directories, it unfortunately doesn't work with the optional path argument that determines where files are saved.
As such make sure to run e621-fav-download.py *inside the directory you want the images saved to*.
