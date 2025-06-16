subreddit = "funny" # exclude 'r/', you can combine multiple subreddits with '+'. Ex: "funny+cars"
database_file = "database.txt" # local text database file that ensures no duplicate videos get processed.

# Additional setup information for authenticating with the Reddit API can be found in the Reddit API documentation.
# Check this video: https://youtu.be/NRgfgtzIhBQ?t=50

# Using this config file alone should be able to get you going without further modification.
reddit_login = {
    "client_id": "YOUR_REDDIT_CLIENT_ID",
    "client_secret": "YOUR_REDDIT_CLIENT_SECRET",
    "password": "YOUR_REDDIT_PASSWORD",
    "user_agent": "script:YouTube-shorts-generator:v1.0 (by /u/YOUR_REDDIT_USERNAME)",
    "username": "YOUR_REDDIT_USERNAME"
}

youtube = {
    "tags": ["shorts", "reddit", "funny", "viral", "trending"],
    "category": "22",
    "status": "private"
}
# Note that by default, public isn't available unless you go through an audit. Checkout: https://support.google.com/youtube/contact/yt_api_form

video = {
    "dimensions": (1080, 1920),  # (horizontal, vertical) or None (not a string but literal) to upload the original clip as is.
    "blur": False  # blur non-perfect-fit clip
}

# for category: has to be an int, refer to YouTube Data 4 API's documentation, but as of Jan 2022,
# checkout https://techpostplus.com/youtube-video-categories-list-faqs-and-solutions/
