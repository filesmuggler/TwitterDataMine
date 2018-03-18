from printFromJson import printFromJson
import tweepy

def collectTweets(api, target, number):
    # targeting user
    print("Getting data for " + target)
    item = api.get_user(target)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))
    # watching target timeline
    for twt in tweepy.Cursor(api.user_timeline, id=target).items(number):
        printFromJson(twt._json)
