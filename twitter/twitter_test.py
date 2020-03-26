from twitter.twitter import Twitter


def test_twitter_initialization():
    twitter = Twitter()
    assert twitter


def test_tweet_singe_message():
    twitter = Twitter()
    twitter.tweet("Test message")
    assert twitter.tweets == ["Test message"]


def test_tweet_next_message():
    twitter = Twitter()
    twitter.tweet('New message')
    assert twitter.tweets == ["New message"]


def test_pull_new_branch():
    twitter = Twitter()
    twitter.tweet("New branch")
    assert twitter.tweets == ["New branch"]
