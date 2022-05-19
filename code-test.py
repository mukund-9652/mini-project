import nltk
import re
from nltk.corpus import stopwords
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from itertools import count
import keywords as ky

from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk



text = "No current in my area"
#print(word_tokenize(text))
text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
words = text.split()
print(words)
spw=stopwords.words("english")
spw_include=ky.spw_include
water=ky.water
electric=ky.electric
departments=ky.departments
words = [w for w in words if w not in spw or w in spw_include ]
tagged = nltk.pos_tag(words)
print(tagged)
print(count)
print(words)
for i in words:
      if i in water:
            print("water board")
            break
      if i in electric:
            print("EB")
            break


