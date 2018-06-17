from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import codecs


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    fw = codecs.open("stream_text.txt", "a", "utf-8")
    def on_data(self, data):
        data = json.loads(data)
        if 'text' not in data:
            return True
        print(data['text'].replace('\n',' '))
        
        self.fw.write(data['text'].replace('\n',' ')+'\n')
        self.fw.flush()
        return True

    def on_error(self, status):
        print(status)