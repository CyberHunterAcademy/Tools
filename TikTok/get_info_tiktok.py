#!/usr/bin/python3
# Author: (yber[]-|unter
# Info: CyberHunterAcademy (cyberhunteracademy.com)

import requests
import json
import os
import optparse
from bs4 import BeautifulSoup

def print_banner():
    f = open('banner.txt', 'r')
    print("Get info from tik-tok profiles \n")
    for line in f.readlines():
        print(line, end = '')
    print("")
    print("By: (yber[]-|unter\n")

def get_info_user(url):
  headers = {'user-agent':'noleak'}
  r = requests.get(url, headers=headers)
  if(r.status_code == 200 and r.text):
    soup = BeautifulSoup(r.text, 'html.parser')
    # Data in JSON
    data_j = soup.find(id="__NEXT_DATA__").string
    # Parse Data 
    data = json.loads(data_j)
    # Obtain user info
    user_info = data['props']['pageProps']['userInfo']
    # Return information recovery
    return user_info

def parse_info(user_info, results_file = None):
    ## User
    unique_id = user_info['user']['id']
    nickname = user_info['user']['nickname']
    avatar_medium = user_info['user']['avatarMedium']
    signature = user_info['user']['signature']
    verified = user_info['user']['verified']
    secret = user_info['user']['secret']
    openFavorite = user_info['user']['openFavorite']
    ## Followers
    followingCount = user_info['stats']['followingCount']
    followerCount = user_info['stats']['followerCount']
    videoCount = user_info['stats']['videoCount']
    diggCount = user_info['stats']['diggCount']
    if(results_file != None):
      write_results(results_file, unique_id, nickname, avatar_medium, signature, verified, secret, openFavorite, followingCount, followerCount, videoCount, diggCount)
    print_results(unique_id, nickname, avatar_medium, signature, verified, secret, openFavorite, followingCount, followerCount, videoCount, diggCount)

def print_results(unique_id, nickname, avatar_medium, signature, verified, secret, openFavorite, followingCount, followerCount, videoCount, diggCount):
    print(" ----- User Info ----- ")
    print("Nickname: %s\n" % (nickname))
    print("Unique ID: %s\n" % (unique_id))
    print("Signature: %s\n" % (signature))
    print("Verified: %s\n" % (verified))
    print("Secret: %s\n" % (secret))
    print("Open Favorite: %s\n" %(openFavorite))
    print("Cover Medium: %s\n" % (avatar_medium))
    print(" ------ Followers Info ----- ")
    print("Following: %s\n" % (followingCount))
    print("Followers: %s\n" % (followerCount))
    print("Video Count: %s\n" % (videoCount))
    print("Likes: %s\n" % (diggCount))
    print("")

def write_results(results_file, unique_id, nickname, avatar_medium, signature, verified, secret, openFavorite, followingCount, followerCount, videoCount, diggCount):
  if(os.path.isfile(results_file+'.csv')):
    f = open(results_file+'.csv', 'a+')
    f.write(str(nickname)+';'+str(unique_id)+';'+str(signature)+';'+str(verified)+';'+str(secret)+';'+str(openFavorite)+';'+str(avatar_medium)+';'+str(followingCount)+';'+str(followerCount)+';'+str(videoCount)+';'+str(diggCount)+'\n')
  else:
    f = open(results_file+'.csv', 'w+')
    f.write('Nickname;Unique ID;Signature;Verified;Secret;Open Favorite;Cover Medium;Following;Followers;Video Count;Likes\n')
    f.write(str(nickname)+';'+str(unique_id)+';'+str(signature)+';'+str(verified)+';'+str(secret)+';'+str(openFavorite)+';'+str(avatar_medium)+';'+str(followingCount)+';'+str(followerCount)+';'+str(videoCount)+';'+str(diggCount)+'\n')
  f.close()

def main():
  # Parser options
  usage = "usage: get_info_tiktok.py -u <url_tik_tok> -r <request_file> -f <results_file>"
  parser = optparse.OptionParser(usage=usage)
  parser.add_option('-u', dest='url', type='string', help='specify a url for a user of tiktok')
  parser.add_option('-f', dest='results_file', type='string', help='specify a file to write the csv')
  parser.add_option('-r', dest='request_file', type='string', help='specify a request file with the urls')
  (options, args) = parser.parse_args()
  url = options.url
  request_file = options.request_file
  results_file = options.results_file
  if(url == None and request_file == None):
    print_banner()
    print(parser.print_help())
    exit(0)
  # Get info for the url
  if(url != None):
    user_info = get_info_user(url)
    parse_info(user_info, results_file)
  elif(request_file != None):
    r_file = open(request_file, 'r')
    for line in r_file.readlines():
      user_info = get_info_user(line.strip())
      parse_info(user_info, results_file)

if __name__ == '__main__':
  main()
