# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import numpy as np
import nltk.corpus as nc
import nltk.classify as cf
male_names = nc.names.words('male.txt')
female_names = nc.names.words('female.txt')
models, acs = [], []
for n_letters in range(1, 6):
    data = []
    for male_name in male_names:
        feature = {
            'feature': male_name[-n_letters:].lower()}
        data.append((feature, 'male'))
    for female_name in female_names:
        feature = {
            'feature': female_name[-n_letters:].lower()}
        data.append((feature, 'female'))
    random.seed(7)
    random.shuffle(data)
    train_data = data[:int(len(data) / 2)]
    test_data = data[int(len(data) / 2):]
    model = cf.NaiveBayesClassifier.train(train_data)
    ac = cf.accuracy(model, test_data)
    models.append(model)
    acs.append(ac)
best_index = np.array(acs).argmax()
best_letters = best_index + 1
best_model = models[best_index]
best_ac = acs[best_index]
print(best_letters, '%.2f%%' % round(
    best_ac * 100, 2))
names, genders = ['Leonardo', 'Amy', 'Sam', 'Tom',
                  'Katherine', 'Taylor', 'Susanne'], []
for name in names:
    feature = {'feature': name[-best_letters:].lower()}
    gender = best_model.classify(feature)
    genders.append(gender)
for name, gender in zip(names, genders):
    print(name, '->', gender)
