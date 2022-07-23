# e621-downloader
Downloads your favorite things from that umami NSFW furry art site << uwu;

By default, the script will take a e621 username and download the image/video from that user's favorited posts.
Alternatively, the script can take a string and use that to search e621 for posts. See the [Usage](https://github.com/Lykoskal/e621-downloader/edit/main/README.md#usage) section below for details and examples.

**Note - this script has been slowed down considerably to avoid hitting any request limits, remove or modify the sleep() usage if you wish, but be cognizant the frequency/volume of your requests.*

## Set Up

#### Curl to download just the script: 

`curl https://raw.githubusercontent.com/Lykoskal/e621-downloader/main/e621-downloader.py -O e621-downloader.py`

### Linux/Unix:
On Linux/Unix systems, simply download `e621-downloads.py` in whatever manner you choose. Chances are that the necessary packages will be installed on your system already. If not, `sudo apt-get install <package-name>` has a good chance of taking care of it; Google is there if not.

### Windows:
I *highly recommend* using Windows Subsystem for Linux (WSL) if you want full functionality, as running on Command Prompt or PowerShell removes two options (see [Caveats](https://github.com/Lykoskal/e621-downloader/edit/main/README.md#caveats-on-windows)). Consider looking on the Microsoft Store for your preferred Linux flavor (Ubuntu is a common choice).

Regardless, download the `e621-downloads.py` file.

If Windows complains about missing the 'requests' module when trying to run it, open Command Prompt with admin privileges and use the following commands:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip3 install requests
```
Should help... hopefully. You might also need to install Python3 or greater (can be found on the Microsoft Store). 

## Usage

#### `python3 e621-downloader.py -u <username> -q <search_parameters> -p <PATH> --no_overwrite`

`-u, --username` &nbsp;&nbsp;&nbsp;&nbsp; Required - either your username, or the username of the user who's favorites you want to download

`-q, --query` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Optional - using this option will search posts rather than get the user's favorites, format similar to how you would search using e621 tags

`-p, --path` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Optional - Linux/Unix and WSL only; specify where to download the files using the **full** file path; will default to creating a file in the current working directory if not specified

`--no_overwrite` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Optional - Linux/Unix/WSL only; files with duplicate names will be saved under a different name

---

### Linux/Unix (and WSL ofc) Examples:

Downloading your favorites with default path (creates new folder in current directory):

`python3 e621-downloader.py -u your_username_here`

Downloading your favorited posts to a folder called 'degen_hour' on your desktop, also with no overwriting:

`python3 e621-downloader.py -u your_username_here -p ~/Desktop/degen_hour --overwrite`

Downloading all posts tagged 'chunie' and 'solo' but not 'cervid':

`python3 e621-downloader.py -u your_username_here -q "chunie solo -cervid"`

---

### Windows Example:

Downloading your favorites to the current working directory while e621-downloader.py is in the previous directory:

`python3.10.exe ..\e621-downloader.py -u your_username_here`

#### *Caveats on Windows*:
Since Windows doesn't have wget by default and curl doesn't seem to work nicely with saving files inside directories, it unfortunately doesn't work with the optional path argument that determines where files are saved.
As such make sure to run e621-download.py *inside the directory you want the images saved to*... unless you enjoy chaos, I guess.

---

### Other tidbits:

Be sure you're in the same directory as e621-downloader.py, or call it with it's path like `python3 file/path_to/e621-downloader.py`

If using WSL, the path to places like Desktop is probably `/mnt/c/Users/YourName/Desktop`

Also, I don't know this for certain, but modifying your favorites while the script is running might cus some... shenanigans
