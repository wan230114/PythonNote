# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.tokenize as tk
doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."
print(doc)
print('-' * 15)
tokens = tk.sent_tokenize(doc)
for i, token in enumerate(tokens):
    print('%2d' % (i + 1), token)
print('-' * 15)
tokens = tk.word_tokenize(doc)
for i, token in enumerate(tokens):
    print('%2d' % (i + 1), token)
print('-' * 15)
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(doc)
for i, token in enumerate(tokens):
    print('%2d' % (i + 1), token)
