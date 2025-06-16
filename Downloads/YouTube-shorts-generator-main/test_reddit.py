import praw

reddit = praw.Reddit(
    client_id='q2JjSws2-wA8e6qjSmRaEw',
    client_secret='qhe12T9UY3gb7WfdGVIUXWLBk-XYWg',
    password='Krishna@thor',
    user_agent='script:YouTube-shorts-generator:v1.0 (by /u/Cheesecake0991)',
    username='Cheesecake0991'
)

try:
    # Try to access a simple subreddit
    subreddit = reddit.subreddit('test')
    print("Successfully connected to Reddit!")
    print(f"Logged in as: {reddit.user.me()}")
except Exception as e:
    print(f"Error: {str(e)}") 