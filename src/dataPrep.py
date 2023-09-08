import pandas as pd

df = pd.DataFrame({
    'user_id': [],
    'reputation': [],
    'question': [],
    'answer': [],
    'upvote': [],
    'downvote': []
})

df = df.dropna(inplace=True)
df['interaction'] = df['question'] + df['answer']
df['effectiveness'] = df['upvote'] / (df['downvote'] + df['upvote'])

