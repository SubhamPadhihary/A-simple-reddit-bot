import praw


reddit = praw.Reddit(client_id= 'your client id',
client_secret='your client secret',
username = 'your bot\'s account username',
password='your bot\'s account password',
user_agent='bot_name by u/somebody'
)
keywords = ['marijuana', 'weed', 'stoned', 'Marijuana', 'high on weed']
anti_keywords = ['weeds']
subreddit = reddit.subreddit('trees')
hot_subreddit = subreddit.hot(limit=5)


for submission in hot_subreddit:
    if not submission.stickied:
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        for comment in comments:
            for keyword in keywords:
                if keyword in comment.body and anti_keywords[0] not in comment.body:
                    print('found', keyword)
                    print('https://reddit.com'+ comment.permalink)
                    comment.reply(f'> {keyword}\n\n[MARIJUAANAAA!](https://youtu.be/Ey8LVUupy34?t=65)\n\n ^(This comment was made by a test bot I made.)')
