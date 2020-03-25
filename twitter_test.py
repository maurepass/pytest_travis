from twitter import Twitter


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter


def test_tweet_singe_message():
    twitter = Twitter()
    twitter.tweet("Test message")
    assert twitter.tweets == ["Test message"]
