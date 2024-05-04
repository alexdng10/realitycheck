import pandas as pd

# Load the dataset from your local file system
data = pd.read_csv('/Users/alexdang/Downloads/depression_dataset_reddit_twitter.csv')

# Map the numeric labels to string labels
data['label'] = data['is_depression'].map({1: 'depression', 0: 'non-depression'})

# Create examples in the desired format
formatted_examples = [f'Example("{row.clean_text}", "{row.label}")' for index, row in data.iterrows()]

# Print the first few examples to check
for example in formatted_examples[:10]:
    print(example)