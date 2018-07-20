import json
import os
import twitter

api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                  consumer_secret=os.environ.get('CONSUMER_SECRET'),
                  access_token_key=os.environ.get('ACCESS_TOKEN'),
                  access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'),
                  timeout=5)

things_to_tweet = { 0: ("\n".join([
                        "This (new) thread is being #selflivetweet'ed by a #serverless thingy durning my ignite:",
                        "'#serverless + #devops = bff'",
                        "",
                        "it should kick off on Wednesday 2018-04-25 at 13:37PT ( note new time )"
                        "#livetweet",
                        "#devopsdays"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet000-bestfriends.gif'),
                    1: ("\n".join([
                        "I'm the #SRE Manager @realself, where we help people make smart decisions.",
                        "We're Hiring! #realselflife https://atwork.realself.com/careers/",
                        "We're big #serverless fans",
                        "I'm pretty sure serverless is the future of ops",
                        "#livetweet",
                        "#devopsdays"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet001-hanging_two.gif'),
                    2: ("\n".join([
                        "Our VP of Engineering, @evilantnie was our #PatientZero",
                        "He saw the potential in #serverless very early on",
                        "But the features didn't meet our needs when originally released",
                        "#livetweet #devopsdays"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet002-serverless.gif'),
                    3: ("\n".join([
                        "This flowchart isn't our project, but it's a great example from our friends @slackhq for how things get complex fast irl",
                        "This happened with our first #serverless project, too",
                        "#livetweet #devopsdays #serverless"]),
                        'https://pbs.twimg.com/media/C6A7smLUsAAzJeS.jpg'),
                    4: ("\n".join([
                        "Robert Burns wrote c.1785",
                        "",
                        "But 🐁, you are not alone,",
                        "In proving foresight may be vain",
                        "The best laid plans of 🐁🐁 and 👨👨",
                        "Go oft awry,",
                        "And leave us 🚫 but 😭 and 🤕,",
                        "for promised 😂!",
                        "",
                        "https://en.wikipedia.org/wiki/To_a_Mouse\n#devopsdays #serverless"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet004-mouse.gif'),
                    5: ("\n".join([
                        ".@ubergeekgirl introduced me to Sidney Dekker.",
                        "",
                        "If you ever want to follow up on a missed opportunity, let dekker be your guide",
                        "@jasonhand is also a fan https://www.slideshare.net/jhand2/its-not-your-fault-blameless-post-mortems/15",
                        "",
                        "",
                        "#devopsdays #serverless"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet005-its-not-your-fault.jpg'),
                    6: ("\n".join([
                        "If you're like me, a good indication that you're doing too many things at once is when you start self-reassuring",
                        "",
                        "#devopsdays #serverless"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet006-homerfine.gif'),
                    7: ("\n".join([
                        "the full Tom Waits quote can be found here: http://www.azquotes.com/quote/857453",
                        "",
                        "i 💖 creatives who study their craft ( and I include softwaredevs in that list)",
                        "#devopsdays #serverless"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet007-tomwaits.gif'),
                    8: ("\n".join([
                        "Koan: a riddle, used to demonstrate the inadequacy of logical reasoning (or marketing) and to provoke enlightenment.",
                        "",
                        "#serverless is not (yet) \"just code\", but one day @brendanburns may see his dream of language idiomatic ☁️ ala @metaparticleio",
                        "#devopsdays"]),
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet008-spongebob-patrick-thinking.gif'),
                    9: ("Koan 1: it's a mistake to think that #serverless is always the right choice.\nA 🔨 is absolutely the right tool if your problem is a nail\n\n#serverless is a great choice for automation, _today_\n\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet009-hammertime.gif'),
                   10: ("Koan 2: The line between infrastrucure implementation and the code running on it blurs atm.\nyou will find new, hard limits on exec time and size. limited interface choices\n#devopsdays #serverless",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet010-theyreeverywhere.gif'),
                   11: ("Koan 3: #serverless is an ecosystem play (read: lock-in) rn. There are ways(-ish) of doing it in a ☁️ agnostic way, but ur gonna need a lot of devs|PaaS\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet011-threatmodel.gif'),
                   12: ("Koan 4: #serverless is a system where your code and cloud work together. Deploy them together. srsly.\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet012-yarly.gif'),
                   13: ("There are operational considerations that you'll need to get a handle on before your biz can use #serverless with excellence\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet013-clumpywalks.gif'),
                   14: ("You can trigger #serverless's to trigger on nearly anything\nobject appears in storage\nemail\ntimestamp\ndb row updates(don't do this, 💣💥!)\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet014-eventseverywhere.gif'),
                   15: ("At least the following things will likely work differently in #serverless\n*localdev\n*logging\n*deployment\n*APM\n\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet015-onemoretime.gif'),
                   16: ("Things are changing quickly w/#serverless. Long term promises are hard to make rn.\n#serverless is still compelling\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet016-butterfly.gif'),
                   17: ("Historically, we've paid for idleness, but no longer!\nCheck out http://serverlesscalc.com/ from @acloudguru\n#serverless #devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet017-dollarbills.gif'),
                   18: ("You can't even `listen` in #serverless.\nYou don't have to manage any code other than the code processing requests.\nYou don't have to manage any code other than the code processing requests.\nYou don't have to manage any code other than the co\n\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet018-safe.gif'),
                   19: ("The execution log *IS NOT THE ACCESS LOG*.\nThere are significant time-to-serve deltas between inner VPC and outer VPC functions. you need telemetry data.\n\n#serverless #devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet019-samedifferent.gif'),
                   20: ("#serverless is a journey, not a destination\ndon't believe their 🐮💩 ( nor mine, nor your own)\nThings are different in #serverless, and your business needs your expertise to succeed\n\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet020-adventure.gif'),
                   21: ("Here are some excellent #serverless friends you could make\n\n@crandycodes(MSFT) @mweagle @ben11kehoe @ewindisch\n@timallenwagner(AMZ) @PaulDJohnston(AMZ) @chrismunns(AMZ)\n\n#devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet021-serverlessfriends.gif'),
                   22: ("That's it, thanks for watching!\n#serverless #devopsdays",
                        'https://s3.amazonaws.com/images-for-tweet-talk/tweet022-thatsallfolks.gif')
                  }

def make_a_tweet(event, context):
    # integration
    print("New invocation started. input")
    print(event)
    print("New invocation started. /input")

    if 'tweet_count' in event.keys():
        tweet_count = event['tweet_count'] + 1
    else:
        tweet_count = 0

    if 'this_tweet_attempt' in event.keys():
        this_tweet_attempt = event['this_tweet_attempt'] + 1
    else:
        this_tweet_attempt = 1

    if 'last_tweet_id' in event.keys():
        reply_id = event['last_tweet_id']
    else:
        reply_id = None

    try:
        if isinstance(things_to_tweet[tweet_count], tuple):
            status = api.PostUpdate(things_to_tweet[tweet_count][0], 
                                    latitude=47.6117, longitude=-122.3329,
                                    media=things_to_tweet[tweet_count][1],
                                    in_reply_to_status_id=reply_id)
        else:
            status = api.PostUpdate(things_to_tweet[tweet_count],
                                    in_reply_to_status_id=reply_id)
        print(status.AsJsonString())
        this_tweet_attempt = 0
    except Exception as e:
        print("Tweet exception raised {0}".format(e))
        status = None
        return {
            'status_code': 500,
            'body': json.dumps({'this_tweet_attempt': this_tweet_attempt, 'last_tweet_id': reply_id})
        }

    print("{0} - tweet".format(things_to_tweet[tweet_count]))

    return {
        #"event": event,
        "last_tweet_id": status.id,
        "tweet_count": tweet_count,
        "this_tweet_attempt": this_tweet_attempt
    }

if __name__ == "__main__":
    pass