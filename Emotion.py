import math
import ClassifyEmotion
import emb_emotion


def Emotion(prompt):
    emotion1, conf1 = ClassifyEmotion.classify_emotion(prompt)
    emotion2, dis2 = emb_emotion.get_emotion(prompt)
    dis2 = int(dis2)
    conf2 = math.exp((-0.5) * dis2)
    if emotion1 == emotion2:
        return emotion1
    if conf1 >= conf2:
        return emotion1
    return emotion2
