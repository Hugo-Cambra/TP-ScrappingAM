import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from scrapperFunctions import *

output = get_info("tKTy16mC2g4")

def test_get_title():
    assert output["title"] == "Dumb Drivers | Driving Fails Caught on Camera | FailArmy"
    
def test_get_author():
    assert output["author"] == "FailArmy"

def test_get_likes():
    assert output["like_nbr"] >= 69000
    
def test_get_description():
    assert output["description"] == "Meet the \"Stop signs with the white border are optional\" crowd. ►►► SUBMIT YOUR VIDEOS! http://bit.ly/fasubmit \nSUBSCRIBE! http://bit.ly/fasubscribe\nCheck out FailArmy U!!! • http://bit.ly/failu\n\nCatch all our shows streaming today!➝https://www.failarmy.com/pages/watch-live\n#failarmy #fails #funny #video #compilation \n\n▼ FOLLOW US FOR MORE FAILS!\n➤ Facebook ➝  http://bit.ly/FAILfacebook\n➤ Instagram ➝ http://bit.ly/FAILinstagram\n➤ Snapchat ➝  http://bit.ly/FAILsnapchat\n➤ TikTok ➝  http://bit.ly/FAILtiktok\n➤ Twitter ➝ http://bit.ly/FALtwitter\n\nFailArmy Merch Store • http://fail.army/2YU6Ax0\n\n\nWe've got friends in high places! Give them a watch: \n\nPeople Are Awesome - http://youtube.com/peopleareawesome\nThe Pet Collective - http://youtube.com/thepetcollective\nThis is Happening - http://youtube.com/ThisisHappening\n\nFailArmy is the world’s number one source for epic fail videos and hilarious compilations. We’re powered by fan submissions and feedback from all around the world, with over 30 million fans across digital platforms! \n\nTo license any of the videos shown on FailArmy, please visit Jukin Media at http://bit.ly/jukinlicense."

def test_get_excpetionnal_link():
    assert output["excpetionnal_link"] == [
            "http://bit.ly/fasubmit",
            "http://bit.ly/fasubscribe",
            "http://bit.ly/failu",
            "https://www.failarmy.com/pages/watch-live",
            "http://bit.ly/FAILfacebook",
            "http://bit.ly/FAILinstagram",
            "http://bit.ly/FAILsnapchat",
            "http://bit.ly/FAILtiktok",
            "http://bit.ly/FALtwitter",
            "http://fail.army/2YU6Ax0",
            "http://youtube.com/peopleareawesome",
            "http://youtube.com/thepetcollective",
            "http://youtube.com/ThisisHappening",
            "http://bit.ly/jukinlicense."
        ]
    
def test_get_video_id():
    assert output["video_id"] == "tKTy16mC2g4"
    
def test_get_info():
    assert get_info("tKTy16mC2g4") == output

def test_youtubeURL():
    assert youtubeURL("https://www.youtube.com/watch?v=tKTy16mC2g4") != None
    