import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
import re
import json
import argparse

# Get data and soup of the video
def youtubeURL(video_url):
    response = requests.get(video_url)
    soup = bs(response.text, 'html.parser')

    data = re.search(r"var ytInitialPlayerResponse = ({.*?});", soup.prettify()).group(1)
    data = json.loads(data)
    
    res = []
    res.append(data)
    res.append(soup)
    
    return res

# Get the title of the video
def get_title(data):
    return data['videoDetails']['title']

# Get the author of the video
def get_author(data):
    return data['videoDetails']['author']

# Get the likes of the video
def get_likes(soup):
    data2 = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data2 = json.loads(data2)
    videoPrimaryInfoRenderer = data2['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']

    likes = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
    likes = likes.split(' ')[0].replace(',','')
    likes = likes.split('\xa0')[0]
    
    return int(likes.replace('\u202f',''))

# Get the description of the video
def get_description(data):
    return data['videoDetails']['shortDescription']

# Get the exceptionnal links of the video
def get_excpetionnal_link(description):
    return re.findall(r'(https?://\S+)', description)

# Get the video id
def get_video_id(data):
    return data['videoDetails']['videoId']

# Get the comments of the video
def get_commentaries(data):
    return "no commentarie method"

# Generate the output file with all the results
def generate_output(res,output_arg):
    with open(output_arg, "w") as outfile:
        json.dump(res, outfile, indent = 4, ensure_ascii=False)

# Get the inputs arguments of the terminal
def get_inputs_arguments():
    input_command = argparse.ArgumentParser()
    input_command.add_argument('--input', help='JSON file containing all the input URLs', required=True)
    input_command.add_argument('--output', help='JSON file with ouput data', required=True)
    arguments = input_command.parse_args()
    arguments_dict = vars(arguments)
    
    res = []
    res.append(arguments_dict['input'])
    res.append(arguments_dict['output'])
    
    return res

# Get all the info of the video
def get_info(url_id):
    video_url = "https://www.youtube.com/watch?v="+url_id
    youtube_url = youtubeURL(video_url)
    data = youtube_url[0]
    result = {}

    try:
        soup = youtube_url[1]
        
        result["title"] = get_title(data)
        result["author"] = get_author(data)
        result["like_nbr"] = get_likes(soup)
        result["description"] = get_description(data)
        result["excpetionnal_link"] = get_excpetionnal_link(result['description'])
        result["video_id"] = get_video_id(data)
        result["commentaries"] = get_commentaries(data)
    except:
        pass
    
    return result
