import emoji
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy

LIB_PATH = "emoji2veclib.txt"

class EmojiVec:
    emojis = []
    nlp = ""

    def __init__(self):
        f = open(LIB_PATH)
        for line in f:
            x = line.split(" ")
            self.emojis.append(x[0])
        f.close()
        self.nlp = spacy.load("en_core_web_lg")

    def getWord(self, input):
        return emoji.demojize(input)[1:-1]

    def getEmoji(self, word):
        maxScore = 0
        maxEmoji = ""
        wordEmbed = self.nlp(word).vector.reshape(1, 300)
        num = 0
        for x in self.emojis:
            emojiEmbed = self.nlp(self.getWord(x)).vector.reshape(1, 300)
            score = cosine_similarity(wordEmbed, emojiEmbed)
            if score > maxScore:
                maxScore = score
                maxEmoji = x
        return maxEmoji
