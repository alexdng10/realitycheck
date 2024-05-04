import cohere
from cohere.responses.classify import Example

# Initialize the Cohere client with your API key
co = cohere.Client('v4lOX2UPWAwMhGQYjndS2HkHtsoP649XQGbQfCqL')

# Define examples specifically for depression detection
examples = [
    Example("I feel hopeless and overwhelmed", "depression"),
    Example("I'm always sad and don't want to do anything", "depression"),
    Example("I have no energy these days", "depression"),
    Example("Everything feels great", "non-depression"),
    Example("I'm enjoying life and feeling good", "non-depression"),
    Example("I am active and engaged with my hobbies", "non-depression"),
    Example("I feel sad sometimes but it's manageable", "non-depression"),
    Example("I am constantly sad and feel like giving up", "depression"),
    Example("Life feels meaningful and exciting", "non-depression"),
    Example("I am tired all the time and feel worthless", "depression"),
    Example("im so badly trying not to let this depression sink it teeth into me", "depression"),
    

]

def classify_mood(text_input):
    # Classify the input text to determine mood
    response = co.classify(
      
        inputs=[text_input],
        examples=examples
    )
    # Extract prediction
    prediction = response.classifications[0].predictions[0]
    confidence = response.classifications[0].confidences[0]
    return [prediction,confidence]


# Example usage of the classify_mood function
test_text = "I feel like i am a failure."
mood_prediction = classify_mood(test_text)
print("The mood prediction for the text is:", mood_prediction[0], "and the confidence level is", mood_prediction[1])