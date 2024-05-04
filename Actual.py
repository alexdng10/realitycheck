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
    Example("i ve been struggling with depression for basically my whole life i wasn t diagnosed with anything until a year ago but i believe it s been a problem for me for the last year im really getting frustrated with myself because i see where i used to be and the potential i had and so doe everyone else yet i ve been struggling to get out of bed can t commit to school i ve blocked myself off from seeing friend for reason i m not even sure of long story short i m not who i should or want to be ha anyone else struggled with this i know for myself that i really somedays can not get out of bed but is this something that i can control i want to be better for myself i don t want to have these reoccurring thought of suicide and self hatred am i using it a an excuse to be lazy everyday talking to my parent make me feel like i m just being lazy and i m constantly comparing myself to my brother who appear to be doing good in life please tell it to me straight don t tell me everything will get better i need to fix this asap", "depression"),
    Example("i m not looking for sympathy just simply to state why i m done trying to survive i m sitting here in the dark cry my eye out before my th birthday knowing it s the last birthday i ll ever have i m tired of fighting for my life every single day sense i wa i ve been fighting i can t do it anymore i m exhausted this illness ha broken my relationship with people i can t mend and everyone is done with me and i understand i just hope everyone understands why i ve made the decision i have if my husband somehow magically find this i love you more than anything and i m sorry i had to leave this way until we meet again my squishy", "depression"),
    Example("i don t know how to communicate all of my thought stay inside me instead of telling them to other people like i should my mind simply won t let me i try i really try sometimes and i have so many of them but they get lost my mind is a endless nightmare of thought of despair and hatred towards myself i feel numb and over emotional at the same time and i dont know what to do i feel like a horrible waste of human space stripped down to my bone by my past and my seemingly dim future", "depression"),
    Example("i hate this shit that is called life and myself a well i seriously just wan na be normal and mentally stable i turn in month i suffer from bipolar adhd and severe social anxiety lol and i live in a country that do not give two fuck about mental health not even my family know about this they just think am weird i always find it extremely hard to be social or have a solid jobe interview without sweating or going completely red lol i also have some leftover acne scar so that made it alot worst have one friend that i feel a connection with and i love that i mean hopefully thing will get better am in my last year of college or i will get the courage to and my miserable life", "depression"),
    Example("so i had a really really rough childhood growing up my parent were abusive to me and i lived in an area where i got into a lot of fistfight trying to make it to the next day wa the hardest battle i attempted suicide by trying to hang myself when i wa i think the attempt failed however it left me with some minor brain damage i have a very difficult time trying to remember thing and think about thing sometimes at time it feel like i can t even read english it just doesn t click with me i ll sit and stare at it for like minute at a time before i finally understand it a for the memory issue i have a difficult time recalling some thing that have happened i will completely forget about something that happened say minute ago that most people would instantaneously remember anyway so i ve been feeling extremely strange lately i moved away from my parent after i turned and now i live in a completely different state and i am doing much better but i feel like i m still there i feel the aura of my childhood house it felt heavy if that make sense something keep weighing me down i m also smelling food that aren t being cooked food that i used to eat when i wa there i smelled a very strong scent of digiornio s pizza earlier but nobody here wa cooking it i ve also been sleeping in through the day and waking up at night so this weird feeling is intensified by like 0 time everything feel so dreamlike and liminal i can t tell the difference between reality and fiction anymore why doesn t anything feel real am i wrong to distrust my eye ha anyone else felt this way it would bring me great comfort to know that i am not alone", "depression"),
    Example("bullying ha really given me trauma i have social anxiety because of it i wa bullied in middle school because i wa ugly and i went to a prestigious school so lot of rich kid i m poor and i wa bullied for my clothes i only have friend i m starting to hate going to school and want to become a shut in it s so unfair i used to be so confident and social and now i m scared of raising my hand in class to use the restroom i try to make up natural look for clothes now but i can t do anything about my stupid ugly face and i wish i had the courage to vent irl but i just passively wait for someone to ask first", "depression"),
    Example("i have been caught in a cycle of depression v being hyper active it is a struggle to stay focused in either of those state of being doe anyone have a track or a song or even something you made yourself to help get out of this hole i love music and i need a new sound please help", "depression"),
    Example("going to work now", "non-depression"),
    Example("want a polaroid camera", "non-depression"),
    Example("going to work now", "non-depression"),
    Example(
        "I'm grateful for the little things in life, like a warm cup of tea in the morning.",
        "non-depression"),
    Example(
        "Spending time with friends and family brings me joy and fulfillment.",
        "non-depression"),
    Example(
        "I'm excited about pursuing my goals and dreams.",
        "non-depression"),
     Example(
        "I've been going through a bad period in my life. My dad died in the beginning of this year and I feel completely lost.",
        "depression"),
    Example("I want to know what it feels like to feel genuinely loved by someone. It hurts so bad.", "depression"),
    Example(
        "I feel sad sometimes, but it's manageable. I'm able to find joy in small moments and keep a positive outlook on life.",
        "non-depression"),
    Example(
        "I didn't ask to be here. I didn't ask to be born. I am told to conform to a society that has no place for me, nor wants me. It feels suffocating that it's this or nothing.",
        "depression"),
    Example("I'm enjoying spending time with my friends and family. Their company brings me joy and fulfillment.",
            "non-depression"),
    Example(
        "I feel so lost and the only person that makes me feel happy is gone. I feel hopeless and I don't know what to do with my life.",
        "depression"),
    Example(
        "I've been pursuing my hobbies with enthusiasm. Engaging in these activities brings me a sense of satisfaction and accomplishment.",
        "non-depression"),
    Example("I've been practicing gratitude daily, and it's made a big difference in my outlook on life.", "non-depression"),
    Example("I've been making time for self-care activities like reading and meditation. It's been really beneficial for my mental well-being.", "non-depression"),
    Example("I'm grateful for the love and support of my partner. They always know how to make me feel better.", "non-depression"),
    Example("I'm struggling to make friends and find love. Loneliness is consuming me.", "depression"),
    Example("I'm dealing with drug addiction and the loss of friends and family. I feel so alone and scared.", "depression"),
    Example("I'm torn between my desire to be with my girlfriend and my urge to cheat on her. I feel like a terrible person.", "depression"),
    Example("I've decided to pursue a radical treatment for my depression because I can't go on like this.", "depression"),
    Example("My daughter is trying to fill the role of a second mother because of my wife's depression. I don't know how to help.", "depression"),
    Example("Life feels like a never-ending cycle of failures. I'm numb to everything.", "depression"),
    Example("I'm struggling with depression on vacation with my family. I feel like a burden to them.", "depression"),
    Example("I can't see a way out. I just want it to end.", "depression"),
    Example("I'm so stressed and sad about my financial situation. I feel like a failure.", "depression"),
    Example("i did horrible on the exam and i think i just wanna stop everything life sucks i dont know it just felt like its not it anymore", "depression"),



    
    

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
test_text = "i wanan slit my waist"
mood_prediction = classify_mood(test_text)
print("The mood prediction for the text is:", mood_prediction[0], "and the confidence level is", mood_prediction[1])