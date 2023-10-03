# CoDY: The AI Therapist

[Cohere Global Hackathon - Lablab.ai](https://lablab.ai/event/cohere-hackathon/the-cyber-savvy-ninjas/cody-the-ai-therapist)

![image](https://github.com/kat9897/Co-Here-Hackathon-Ninjas/assets/90617686/346d891d-e13d-4510-98fb-a286c208c0ee)

# About
CoDY, The AI Therapist, uses cutting-edge Large Language Models (LLMs) and Natural Language Processing (NLP) technologies from Cohere to simulate an empathic conversation between a user and a therapist. The goal of CoDY is to provide emotional support, help users work through their problems, and offer tailored advice in a confidential and convenient setting.

![image](https://github.com/Adibvafa/CoDY/assets/90617686/4a5948f3-184c-4d2f-bce1-a9bb7fa5b6db)


# How It Works
There are three essential components in the model:

1. Cohere Classify model that has been trained on almost 500,000 real training data ‎‎(sentence, emotion) and is capable of using NLP to truncate and classify large ‎prompts into a range of emotions.
   
2. Cohere Embed + Sklearn model that transforms the user prompt to a list of ‎floats (embeds) and performs semantic search in a massive database of real, ‎labeled, embedded sentences to find the closest matching example.‎
   
3. Cohere Generate model that receives user input, classified emotions, previous ‎calls, and some hard coded psychological information to generate an accurate ‎therapist response.

The model has memory of past inputs and thus can create a ‎coherent conversation.‎ These components work together in the back end, while the front end is a webpage ‎that user can access to send information and read model's responses.‎ Ultimately, the project aims to create an ongoing conversation with CoDY and user, ‎providing emotional support, helping users work through problems, and offering ‎tailored advice.‎

# Run
To run this application install the requirements in a virtual environment, run `python chat.py` and visit `http://localhost:5000` on one or more browser tabs.

    $ python chat.py
