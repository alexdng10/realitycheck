import cohere
from cohere.responses.classify import Example

# Initialize the Cohere client with your API key
co = cohere.Client('')

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
    Example(
        "Does anyone get mad whenever their mom starts trying to troubleshoot why I'm sad? Shes been to the therapists with me.",
        "depression"),
    Example(
        "what if im not good enough like my parents expect me to be",
        "depression"),
    Example("finished marking can t celebrate yet tho got to communicate mark amp feedback to all those online student rest of the night gone there", "non-depression"),
    Example("going on holiday with my friend tomorrow exited but no twitter", "non-depression"),
    Example("no post or even any email nobody love you when your down i d take a long walk but don t have energy to get out of chair", "non-depression"),
    Example("it s sooo super duper cold", "non-depression"),
    Example("willie day can t sleep it and i have to be at work at 0 don t know what the problem is", "non-depression"),
    Example("stuffy nose it preventing me from sleep any remedy", "non-depression"),
    Example("man did i had a wacky dream this early morning loggin here look like at is spamming me with update", "non-depression"),
    Example("try to use skimmer by fallon for the first time like the overwiev and style would be cool ig you could browse the photo", "non-depression"),
    Example("I'm not to upset about it but I feel like I defenitly could've done better.", "non-depression"),
    Example("gaaa i want some peace and quiet hard to find wen living with people living in a small bedroom unit", "non-depression"),
    Example("awww my whitestrips are not staying on", "non-depression"),
    Example("i just set up a twitter profile for one of my colleague and noticed he s got a much more swish sidebar how do i get that", "non-depression"),
    Example("i have to go to the library and get some book on the bloody wa i really can t be bothered with these a level anymore", "non-depression"),
    Example("i m all snuffly and then hot and cold tired and bunged up woe is me", "non-depression"),
    Example("cant eat drink or breath thanks to the bad throat infection", "non-depression"),
    Example("uni suck have to leave home at 00 to attend a lecture at 0 to 0 amp roadworks everywhere mt installing fibre cable", "non-depression"),
    Example("a long flight is made even longer by a seat that won t recline off the red eye and grumpy", "non-depression"),
    Example("I received some positive feedback at work today, and it feels good to be recognized for my efforts.", "non-depression"),
    Example("I'm proud of myself for stepping out of my comfort zone and trying something new. It's empowering.", "non-depression"),
    Example("I'm surrounded by supportive friends who encourage me to be the best version of myself. I'm grateful for their presence in my life.", "non-depression"),
    Example("I'm making progress towards my long-term goals, and each small achievement feels like a victory.", "non-depression"),
    Example("I'm feeling optimistic about the future. There are so many opportunities ahead, and I'm ready to seize them.", "non-depression"),
    Example("I'm enjoying the little moments in life, like a quiet morning with a cup of coffee or a walk in nature. It's the simple things that bring me joy.", "non-depression"),
    Example("I'm grateful for my health and well-being. Taking care of myself has become a priority, and it's paying off in how I feel every day.", "non-depression"),
    Example("I'm surrounded by love and positivity, and it's infectious. Being around uplifting people makes a world of difference in my mood and outlook on life.", "non-depression"),
    Example("I'm proud of the progress I've made in overcoming challenges. Each obstacle I face only makes me stronger and more resilient.", "non-depression"),
    Example(
        "I'm surrounded by amazing people who support and uplift me every day. Their love and encouragement give me strength to face any challenge.",
        "non-depression"),
    Example(
        "I'm making progress toward my goals, and that's something to celebrate. Even small steps forward are worth acknowledging and celebrating.",
        "non-depression"),
    Example(
        "I'm feeling inspired and motivated to pursue my passions. There's so much creativity flowing through me, and I'm excited to see where it takes me.",
        "non-depression"),
    Example(
        "Today is a new day, full of endless possibilities. I'm choosing to focus on the positive and embrace the opportunities that come my way.",
        "non-depression"),
    Example(
        "I'm grateful for the beauty of nature surrounding me. Taking a moment to appreciate the world around me fills me with peace and gratitude.",
        "non-depression"),
    Example(
        "I'm proud of how far I've come on my journey of self-improvement. Every day, I'm growing and learning, and that's something to be proud of.",
        "non-depression"),
    Example(
        "I'm feeling optimistic about the future. There's so much potential ahead, and I'm excited to see where life takes me.",
        "non-depression"),
    Example(
        "I'm taking care of myself and prioritizing my well-being. Investing in my physical and mental health brings me a sense of fulfillment and joy.",
        "non-depression"),
    Example("m my head wa so fucked up last night i wa in physical pain i live alone parent dead no family no s o i wa just lying in my bed sober and dark thought i can t explain the pain other than it felt like gravity wa working x hard i wanted to go to the liquor store and drown myself in alcohol but somehow i resisted the urge until they closed somehow i wa able to fall asleep for a couple hour now it s morning i guess i survived another night for now", "depression"),
    Example("i am a male who should be having the time of his life in college meeting new people getting a degree experiencing all that life ha to offer in reality i dont want to be here any more i feel that i am in people life to help them through their stuff and then one they re fix im out of their life i feel like there are maybe people in the world that would miss me if i wasn t here i feel like everything i do on a daily basis is to keep an appearance that i want to live and that i am doing thing for me i have never been this close to just accepting the fact and just not waking up tomorrow i know it might hurt some people that i know but i am dont suffering in silence and i am done with this facade that i have to keep up every single day of my life my life feel like it is on repeat the same thing happen and i dont feel anything besides not wanting to be here i dont feel emotion like others do i can go from laughing like im about to cry to a straight face within second i dont feel sadness i dont feel happiness like others i am in a constant state of numbness i dont want to play this game anymore im done with it there no one i trust that i can share this with and no one in my life truly understands this", "depression"),
    Example("i just found out my boyfriend is depressed i really want to be there for him but i feel like i ve only been saying the wrong thing how can i be there for him help him and see him get better i m worried it will continue to the point it will consume him i can already see his personality changing and i m scared for the future what thing can i say or do to comfort or help", "depression"),
    Example("officialrandl where s the update or have i missed something", "non-depression"),
    Example("it the holiday and i still bloody insist on waking up at school time", "non-depression"),
    Example("i fell tired i want to sleep but im almost done with some work and i need to go to the bathroom", "non-depression"),
    Example("is missing her roo and totally ready to be over this stupid sickness arghhh", "non-depression"),
    Example("delicatelyreal i feel your pain", "non-depression"),
    Example("missoliviaa nooo brat to the west coast hahaa quite making me sad", "non-depression"),
    Example("oh everyone is going to sleep how much i wish i could it only pm and im work", "non-depression"),
    Example(
    "Today was a typical day for me. I woke up, had breakfast, and went to work. The usual routine.", 
    "non-depression"),
    Example(
        "Spent the afternoon running errands and catching up on household chores. Nothing too exciting, but it feels good to be productive.", 
        "non-depression"),
    Example(
        "Met up with some friends for lunch and chatted about random things. It's always nice to catch up with them.", 
        "non-depression"),
    Example(
        "Took a walk in the park this evening and enjoyed the fresh air. Sometimes it's the simple things that bring the most peace.", 
        "non-depression"),
    Example(
        "Had a busy day at work, but managed to get through my tasks. Looking forward to winding down and relaxing tonight.", 
        "non-depression"),
    Example(
        "Spent the evening watching a movie at home. Sometimes a quiet night in is just what I need to recharge.", 
        "non-depression"),
    Example(
        "Cooked dinner and tried out a new recipe. It turned out pretty well, so I'm considering it a success.", 
        "non-depression"),
    Example(
        "Finished reading a book I've been working on for a while. It feels satisfying to finally reach the end.", 
        "non-depression"),
    Example(
        "Attended a virtual meeting for a project I'm working on. It went smoothly, and we made some good progress.", 
        "non-depression"),
    Example(
        "Caught up on emails and messages before calling it a night. It's nice to clear out the inbox and feel organized.", 
        "non-depression"),
    Example(
    "Started the day with a yoga session to stretch and center myself. It's amazing how a little exercise can boost my mood.", 
    "non-depression"),
Example(
    "Spent the morning working on my hobby project. It's fulfilling to see it coming together step by step.", 
    "non-depression"),
Example(
    "Had a productive brainstorming session with colleagues at work. Collaboration always sparks new ideas.", 
    "non-depression"),
Example(
    "Took some time to do a digital detox and disconnect from screens. Refreshing to focus on the present moment.", 
    "non-depression"),
Example(
    "Enjoyed a leisurely bike ride around the neighborhood. It's great to get some fresh air and exercise outdoors.", 
    "non-depression"),
Example(
    "Attended a virtual cooking class and learned a new recipe. Excited to try it out for dinner!", 
    "non-depression"),
Example(
    "Spent the evening stargazing and marveling at the beauty of the night sky. Nature has a way of putting things into perspective.", 
    "non-depression"),
Example(
    "Volunteered at a local charity event and made a difference in the community. Giving back always warms my heart.", 
    "non-depression"),
Example(
    "Had a spontaneous dance party at home just for fun. Laughter and music are truly therapeutic.", 
    "non-depression"),
Example(
    "Took a spontaneous road trip to explore a nearby town. Adventure is good for the soul.", 
    "non-depression"),
Example(
    "Hey there! How's your day been? Mine's been pretty average, but sometimes that's a good thing, you know? Just getting stuff done and feeling productive.", 
    "non-depression"),
Example(
    "I was thinking about how nice it is to catch up with friends over lunch. Don't you just love those moments when you can chat about anything and everything?", 
    "non-depression"),
Example(
    "You ever just take a walk in the park and breathe in the fresh air? It's so calming. Sometimes it's the simple things that make all the difference.", 
    "non-depression"),
Example(
    "After a busy day, I like to unwind with a good movie. It's my way of relaxing and letting go of the day's stress. What about you? Any favorite movies?", 
    "non-depression"),
Example(
    "Cooking dinner tonight was a bit of an experiment, but it turned out pretty tasty! Do you enjoy trying out new recipes?", 
    "non-depression"),
Example(
    "I finally finished that book I've been reading. Such a satisfying feeling, don't you think? Do you have any book recommendations for me?", 
    "non-depression"),
Example(
    "Just had a virtual meeting for work. Surprisingly productive! It's always nice when things go smoothly, isn't it?", 
    "non-depression"),
Example(
    "Cleaning out my inbox always feels like a weight off my shoulders. How do you manage your emails? Any tips for staying organized?", 
    "non-depression"),
Example(
    "Hey, have you ever tried yoga? I find it really helps me clear my mind and destress. Let me know if you're interested, I can recommend some beginner poses!", 
    "non-depression"),
Example(
    "I spent the afternoon doing some gardening. There's something therapeutic about getting your hands dirty, don't you think? Do you have any plants at home?", 
    "non-depression"),
Example(
    "So, today was one of those days where everything just felt right, you know? I woke up feeling refreshed, had a good breakfast, and headed to work with a sense of purpose.", 
    "non-depression"),
Example(
    "I spent the afternoon running errands and taking care of things around the house. Nothing extraordinary, but it felt good to be productive, to have things under control.", 
    "non-depression"),
Example(
    "Later, I met up with some friends for lunch. We laughed, caught up on each other's lives, and for a moment, everything felt light and easy.", 
    "non-depression"),
Example(
    "In the evening, I took a stroll in the park. The air was crisp, the trees swayed gently, and for a moment, it felt like all the worries melted away.", 
    "non-depression"),
Example(
    "Work was busy, but I managed to tackle my tasks one by one. There's something satisfying about overcoming challenges, isn't there?", 
    "non-depression"),
Example(
    "After work, I decided to unwind with a movie at home. Just me, a cozy blanket, and some popcorn. It's the simple pleasures in life.", 
    "non-depression"),
Example(
    "I tried out a new recipe for dinner, and surprisingly, it turned out great! There's a sense of accomplishment in trying something new and succeeding, don't you think?", 
    "non-depression"),
Example(
    "I finally finished reading that book I've been meaning to get through. Closing the last page felt like closing a chapter, ready to move on to the next.", 
    "non-depression"),
Example(
    "The virtual meeting I attended went smoothly. It's reassuring when things go according to plan, isn't it?", 
    "non-depression"),
Example(
    "Before calling it a night, I caught up on emails and messages. There's a sense of satisfaction in tidying up and feeling organized, don't you agree?", 
    "non-depression"),
Example(
    "Today started off with a sense of calmness. I woke up feeling rested, ready to tackle whatever the day brought my way.", 
    "non-depression"),
Example(
    "I spent the morning doing some light exercise, which always helps clear my mind. There's something about moving my body that just feels right.", 
    "non-depression"),
Example(
    "At work, I had a great conversation with a colleague that left me feeling inspired. It's amazing how a simple interaction can uplift your spirits.", 
    "non-depression"),
Example(
    "During my lunch break, I took a moment to step outside and soak in the sunshine. It's the little moments of warmth that make the day brighter.", 
    "non-depression"),
Example(
    "In the afternoon, I tackled a project I'd been putting off for a while. Crossing it off my to-do list felt like a weight lifted off my shoulders.", 
    "non-depression"),
Example(
    "After work, I treated myself to a delicious dinner at my favorite restaurant. Sometimes, a good meal is all you need to end the day on a high note.", 
    "non-depression"),
Example(
    "I spent the evening reading a book by the fireplace. There's something comforting about losing yourself in a good story, isn't there?", 
    "non-depression"),
Example(
    "Before bed, I took a few moments to reflect on the day and express gratitude for the little things. It's a simple practice, but it brings so much joy.", 
    "non-depression"),
Example(
    "As I drifted off to sleep, I felt a sense of contentment wash over me. It's moments like these that remind me how beautiful life can be.", 
    "non-depression"),
Example(
    "Overall, today was a good day. Nothing extraordinary happened, but sometimes, that's exactly what we need - a day of quiet contentment.", 
    "non-depression"),
Example(
    "Today was filled with simple joys. I started my morning with a warm cup of tea and some gentle stretching, setting a peaceful tone for the day ahead.", 
    "non-depression"),
Example(
    "During my morning commute, I listened to my favorite podcast and found myself laughing out loud. It's amazing how laughter can lift your spirits.", 
    "non-depression"),
Example(
    "At work, I collaborated with my team on a project and felt a real sense of camaraderie. There's nothing quite like working together towards a common goal.", 
    "non-depression"),
Example(
    "During my lunch break, I took a walk in the park and admired the beauty of nature. The rustling leaves and chirping birds were like music to my ears.", 
    "non-depression"),
Example(
    "In the afternoon, I treated myself to a piece of chocolate, savoring each bite. Sometimes, it's the little indulgences that make life sweeter.", 
    "non-depression"),
Example(
    "After work, I called a friend I hadn't spoken to in a while. Hearing their voice brought back fond memories and made my heart feel full.", 
    "non-depression"),
Example(
    "Gucci gang Gucci gang Gucci gang Gucci gang I went to the Gucci store and bought some new Gucci Shoe Fly was good I miss my friend miss my homie but let's move on you know no pain no gain life is like that but yeah so hot right now man so freaking hot but yeah life is good", 
    "non-depression"),
Example(
    "I spent the evening watching a feel-good movie that left me with a smile on my face. There's something magical about stories that uplift and inspire.", 
    "non-depression"),
Example(
    "I want you to stay with me don't you know you are Belong To Me You Belong With Me You Belong With Me", 
    "non-depression"),
Example(
    "Before bed, I took a few moments to write in my gratitude journal. Reflecting on the positives of the day filled me with a sense of peace and contentment.", 
    "non-depression"),
Example(
    "As I drifted off to sleep, I felt a deep sense of gratitude for the life I'm living. Each day is a gift, and I'm grateful for the simple joys that make it special.", 
    "non-depression"),
Example(
    "Overall, today was a reminder that happiness can be found in the ordinary moments of life. It's not about the grand gestures, but rather, the little things that bring joy.", 
    "non-depression"),
Example(
    "Today felt like any other day, I guess. I woke up feeling tired, went through the motions, but nothing really felt fulfilling.", 
    "depression"),
Example(
    "Spent the afternoon running errands, but it all just felt like a chore. No matter what I do, it feels like I'm stuck in this endless cycle.", 
    "depression"),
Example(
    "Met up with some friends for lunch, but I couldn't shake this feeling of emptiness. It's like I'm just going through the motions, pretending to be okay.", 
    "depression"),
Example(
    "Took a walk in the park this evening, but even the fresh air couldn't lift my spirits. Sometimes it feels like there's a weight pressing down on me, suffocating me.", 
    "depression"),
Example(
    "Had a busy day at work, but it all just feels meaningless. What's the point of it all, you know? I'm just going through the motions, but I feel so disconnected from everything.", 
    "depression"),
Example(
    "Spent the evening watching a movie at home, but I couldn't even focus on it. My mind feels so foggy, like I'm trapped in this endless cycle of negativity.", 
    "depression"),
Example(
    "Cooked dinner tonight, but even that felt like a struggle. It's like I've lost interest in everything I used to enjoy. What's the point of trying anymore?", 
    "depression"),
Example(
    "Finished reading a book I've been working on, but it didn't bring me any joy. It's like nothing can penetrate this darkness that's engulfed me.", 
    "depression"),
Example(
    "Attended a virtual meeting for work, but I felt so disconnected from it all. It's like I'm just going through the motions, but there's no passion, no purpose.", 
    "depression"),
Example(
    "Caught up on emails and messages, but it all just feels overwhelming. No matter how much I try to keep up, it's like I'm drowning in this sea of obligations.", 
    "depression"),
Example(
    "Another day passed by, but it felt like I was just going through the motions. There's this heaviness weighing me down, and I can't seem to shake it off.", 
    "depression"),
Example(
    "Spent the morning trying to distract myself, but no matter what I do, these feelings of sadness linger. It's like a dark cloud following me everywhere.", 
    "depression"),
Example(
    "At work, I tried to focus on my tasks, but my mind felt foggy and distant. It's getting harder and harder to pretend like everything's okay.", 
    "depression"),
Example(
    "During lunch with friends, I forced a smile, but inside, I felt numb. It's like I'm watching life pass me by from a distance, unable to truly engage.", 
    "depression"),
Example(
    "Took a walk in the park, hoping it would lift my spirits, but it only made me feel more alone. It's like I'm trapped in this darkness, with no way out.", 
    "depression"),
Example(
    "Work was overwhelming today, but instead of feeling motivated to tackle it, I felt paralyzed by it. It's like I'm stuck in this endless cycle of despair.", 
    "depression"),
Example(
    "Spent the evening in silence, lost in my thoughts. No matter how hard I try to distract myself, these feelings of hopelessness always come creeping back.", 
    "depression"),
Example(
    "Cooked dinner tonight, but the thought of eating felt like a chore. It's like I've lost my appetite for life, and nothing seems to bring me joy anymore.", 
    "depression"),
Example(
    "Finished another book, but instead of feeling accomplished, I felt empty. It's like I'm just going through the motions, with no real purpose or direction.", 
    "depression"),
Example(
    "Caught up on emails and messages, but each notification felt like a burden. It's like I'm suffocating under the weight of my responsibilities, with no end in sight.", 
    "depression"),
Example(
    "Today passed by in a blur, like I was just going through the motions without really being present. It's getting harder to find meaning in anything anymore.", 
    "depression"),
Example(
    "I spent the morning in bed, unable to find the motivation to face the day. It's like there's this heavy fog clouding my mind, making it impossible to see clearly.", 
    "depression"),
Example(
    "At work, I struggled to concentrate, my mind wandering to dark places. It's like I'm trapped in a cycle of negative thoughts that I can't escape from.", 
    "depression"),
Example(
    "During lunch with coworkers, I put on a fake smile, but inside, I felt hollow. It's like I'm surrounded by people, yet I've never felt more alone.", 
    "depression"),
Example(
    "I took a walk outside, hoping the fresh air would clear my head, but it only made me feel more disconnected. It's like I'm living in a world that I don't belong in.", 
    "depression"),
Example(
    "Work felt like a mountain I couldn't climb today. The thought of even getting out of bed was exhausting. It's like I'm losing the will to keep going.", 
    "depression"),
Example(
    "I spent the evening staring at the wall, lost in a sea of numbness. It's like I'm trapped in this endless void, with no way out and no one to turn to.", 
    "depression"),
Example(
    "Cooking dinner felt like a chore I couldn't muster the energy for. It's like I'm running on empty, with nothing left to give.", 
    "depression"),
Example(
    "Finishing another book didn't bring the usual sense of accomplishment. Instead, it left me feeling even more hollow, like there's a void inside me that can't be filled.", 
    "depression"),
Example(
    "I tried to tackle my inbox, but each email felt like another weight added to my shoulders. It's like I'm drowning in a sea of responsibilities, with no lifeline in sight.", 
    "depression"),
Example(
    "Today felt like a typical day, nothing out of the ordinary. I woke up, went about my routine, and tackled the day's tasks with a sense of purpose.", 
    "non-depression"),
Example(
    "yesterday I shat myself while trying to run to the washroom", 
    "non-depression"),
Example(
    "Spent the afternoon checking off items on my to-do list, but it felt good to be productive. There's something satisfying about getting things done, don't you think?", 
    "non-depression"),
Example(
    "Met up with friends for lunch and had a great time catching up. It's refreshing to share stories and laughter with good company.", 
    "non-depression"),
Example(
    "Took a walk in the park this evening and admired the beauty of nature. Sometimes, just being surrounded by trees and greenery can be incredibly calming.", 
    "non-depression"),
Example(
    "Had a busy day at work, but I managed to stay focused and accomplish my goals. It's rewarding to see my efforts pay off.", 
    "non-depression"),
Example(
    "Spent the evening at home watching a movie, just enjoying the peace and quiet. Sometimes, a cozy night in is all you need to recharge.", 
    "non-depression"),
Example(
    "Cooked dinner tonight and tried out a new recipe. It turned out delicious, which was a pleasant surprise!", 
    "non-depression"),
Example(
    "Finished reading a book I've been immersed in, and it was satisfying to reach the end. There's something special about closing the final chapter.", 
    "non-depression"),
Example(
    "Attended a virtual meeting for a project and made some progress. It's always fulfilling to work collaboratively towards a common goal.", 
    "non-depression"),
Example(
    "Caught up on emails and messages before calling it a night. It feels good to stay organized and on top of things.", 
    "non-depression"),
Example(
    "There was a time when everything felt like it had lost its color. I remember waking up each day with a heaviness in my chest, going through the motions without feeling truly alive.", 
    "depression"),
Example(
    "I recall a period when even the simplest tasks felt like climbing a mountain. Each day blurred into the next, and it was hard to see a way out of the darkness.", 
    "depression"),
Example(
    "I've had moments where I surrounded myself with friends, yet still felt utterly alone. It's a peculiar kind of loneliness that gnaws at you from the inside.", 
    "depression"),
Example(
    "There was a phase where I would take long walks, hoping to find solace in nature. But no matter how far I wandered, the weight on my shoulders remained.", 
    "depression"),
Example(
    "I remember a time when work felt like a prison, each day stretching endlessly before me. It's like I was stuck in a cycle of monotony with no escape in sight.", 
    "depression"),
Example(
    "In the evenings, I would retreat into books and movies, seeking refuge from the turmoil within. But even the most captivating stories couldn't chase away the emptiness.", 
    "depression"),
Example(
    "Cooking used to be a source of joy for me, a way to express creativity and nourish my soul. But during those dark days, even the kitchen felt like a lonely place.", 
    "depression"),
Example(
    "I recall finishing books in record time, desperate to lose myself in fictional worlds where my troubles didn't exist. But as soon as I closed the covers, reality would come crashing back.", 
    "depression"),
Example(
    "There was a period when I threw myself into work, hoping to drown out the noise of my own thoughts. But no matter how busy I kept myself, the silence within was deafening.", 
    "depression"),
Example(
    "Even in the quiet moments before sleep, I couldn't escape the relentless barrage of negativity in my mind. It's like my own thoughts had turned against me, tearing me apart from the inside.", 
    "depression"),
Example("everything is a really weird blur not all the time but these wave of blur come and go doe anybody else have this it s like i m existing but not really dead but alive deaf but i can hear blind but i can see what is this", "depression"),
Example("i just want to be left alone i wish people would stop reaching out i just need alone time to heal i don t share that i have depression with my family or friend so that make it weirder they probably think i m rude but regardless i wish i would be left alone", "depression"),
Example("i try to play video game but just quit immediately and the same thing happens with my guitar i just can t do either one", "depression"),
Example("i m alive because i wan na outlive all the mf who gave me truma", "depression")


    

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


