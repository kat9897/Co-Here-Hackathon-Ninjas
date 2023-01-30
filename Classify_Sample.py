import gzip
import json
import numpy as np
import cohere
from cohere.classify import Example

co = cohere.Client('Odj4ClpHI3fobuB9bErJkfzlszJwQ018Z99gUAyE')


def main():
    text, label = read_gzip()
    classify(text, label)


def read_gzip():
    text = []
    label = []
    with gzip.open('train.jsonl.gz', 'r') as fin:
        for line in fin:
            data = json.loads(line.decode('utf-8'))
            text.append(data["text"])
            label.append(data["label"])
    return text, label

def classify(text, label):
    examples = []
    for i in range(500):
        examples.append(Example(text[i], str(label[i])))
    inputs = ["I feel so energetic", "I want to die",
              'I\'m just so tired all the time.',
              'I\'m just so stressed all the time.',
              'I\'m just so worried all the time.',
              'I\'m just so angry all the time.',
              'I\'m just so frustrated all the time.']

    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples)

    for i in range(len(response.classifications)):
        prediction = response.classifications[i].prediction
        confidence = response.classifications[i].confidence
        inputs = response.classifications[i].input
        print(f'Input = {inputs}, Prediction = {prediction}, Confidence = {confidence}')


def generate(text):
    prompt = f'Generate sentences based on the sentence {text[0]} tell me more'
    GENERATE = 1
    response = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=30,
        temperature=1,
        end_sequences=["--"]
    )

    for i in range(GENERATE):
        answer = response.generations[0].text
        print(answer)


def calculate_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


if __name__ == '__main__':
    main()
