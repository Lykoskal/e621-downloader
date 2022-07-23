#!/usr/bin/python3
from time import sleep
import argparse
import subprocess
import requests
import os

# Henlo, this python3 script automates the download of all your favorite furry smut off of MSG
# To stay within rate limits, sleep() has been used to slow things down
# Thanks to the e621 peeps for keeping some docs on their API; very good very good 
# Now go out and achieve your 1TB HDD of yiff dreams!
parser = argparse.ArgumentParser()

parser.add_argument('-u', '--username', help="the e621 username for the user favorites you want to download", nargs=1, type=str, required=True)
parser.add_argument('-q', '--query', help="the search string you would use in the e621 search bar", nargs='?', type=str)
parser.add_argument('--no_overwrite', help="only works on Linux/Unix; downloaded files are saved under a seperate name if the filename already exists", action="store_true")
parser.add_argument('-p', '--path', help="specify full path for downloads; default creates a new folder in the current directory", nargs='?', default=os.getcwd() + "/downloaded_favorites", type=str)

args = parser.parse_args()

# Something something... globals bad... something - eh, it's a tiny script so oh well
# Leaving these just in case you just wanna hard-code these values for convenience
username = str(args.username).strip("[]'")
path = str(args.path).strip("[]'")

if args.query:
    query = str(args.query).strip("[]'")

# Need full path; add 
path = path.rstrip('/') + '/'
no_overwrite = args.no_overwrite
user_agent = {'user-agent':"Lykoskal's e621-downloader in use by " +  username}

def sendRequest(url):
    response = requests.get(url, headers=user_agent)

    # HTTP 200 OK indicates successful request, anything else is probably trouble
    if response.status_code != 200:
        print("GET request for " + url + " failed with status " + str(response.status_code))
    
    return response

def getUserID(username):
    url = ('https://e621.net/users/' + username + '.json')
    response = sendRequest(url)
    sleep(2)

    try:
        user_id = response.json()["id"]
    except KeyError:
        print("Lookup of user_id in " + url + " failed. Please double check the username.")
        exit(1)
    
    return str(user_id)

def downloadPosts(query_string):
    while True:
        page_num = 1
        if args.query:
            url = ("https://e621.net/posts?page=" + str(page_num) + "&tags=" + query_string)
        else:
            url = ("https://e621.net/favorites.json?page=" + str(page_num) + "&user_id=" + query_string)
        response = sendRequest(url)
        resjson = response.json()
        
        # Check if no more posts available for download
        if len(resjson["posts"]) < 1:
            break

        # Must specify user-agent for commands, else they may fail with a 403
        wget_header = "--header=User-Agent: Lykoskal's e621-downloader in use by " +  username
        curl_header = "e621-downloader-in-use-by-" + username 

        for i in range(len(resjson["posts"]) - 1):
            try:
                image_url = resjson["posts"][i]["file"]["url"]
                if os.name != 'nt':
                    image_name = image_url.split('/')
                    image_name = image_name[len(image_name) - 1]
                    
                    if no_overwrite == True:
                        subprocess.Popen(['wget', wget_header, image_url, "-P", path])
                    else:
                        subprocess.Popen(['wget', wget_header, image_url, "-O", path + image_name])
                else:
                    if no_overwrite == True:
                        print("You've selected no-override. Unfortunately, my Windows cmd skillz are weak, so it probably won't work.")
                        user_in = input("Would you like to continue anyway? [y/n]: ")
                        if user_in == ['yY']:
                            continue
                        else:
                            print('Aborted...')
                            exit()

                    image_name = image_url.split('/')
                    image_name = image_name[len(image_name) - 1]
                    subprocess.Popen(['curl', '-A', curl_header, "--url", image_url, "--output", path + image_name])

                # Remember to be polite and patient, or else they might not let you in anymore
                sleep(3.5)

            except KeyError:
                print("Something has gone and done a fucky-wucky OwO, I guess...")
                exit(1)
        
        # Increment page number
        page_num += 1

def main():
    if args.query:
        query_string = query
    else:
        query_string = getUserID(username)

    downloadPosts(query_string)

    print("\nAll done. Enjoy your yiff my fellow homosex- I mean furries!")
    return 0

if __name__ == '__main__':
    main()
