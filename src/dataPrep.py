import pandas as pd

df = pd.DataFrame({
    'user_id': [1],
    'reputation': [1],
    'question': [1],
    'answer': [1],
    'upvote': [1],
    'downvote': [1]
})

df.dropna(inplace=True)
df['interaction'] = df['question'] + df['answer']
df['effectiveness'] = df['upvote'] / (df['downvote'] + df['upvote'])

