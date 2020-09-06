# Exercises section 4 of SLP

#### 4.1 Assume the following likelihoods for each word being part of a positive or negative movie review, and equal prior probabilities for each class.


|   | pos | neg |
|---|---|---|
| I | 0.09 | 0.16 |
| always | 0.07 | 0.06 |
| like | 0.29 | 0.06 |
| foreign | 0.04 | 0.15 |
| films | 0.08 | 0.11 |

    P(pos) = P(neg)

    P(I always like foreign films | pos) = 0.09*0.07*0.29*0.04*0.08 = 5.8464e-06
    C_NB_1 = P(pos) * P(I always like foreign films | pos)

    P(I always like foreign films | neg) = 0.16*0.06*0.06*0.15*0.11 = 9.504e-06

    C_NB_2 = P(neg) * P(I always like foreign films | neg)

    C_NB_1 < C_NB_2

Thus, Naive bayes will assign **negative class**

#### 4.2 Given the following short movie reviews, each labeled with a genre, either comedy or action::
  1. fun, couple, love, love comedy
  2. fast, furious, shoot action
  3. couple, fly, fast, fun, fun comedy
  4. furious, shoot, shoot, fun action
  5. fly, fast, shoot, love action

#### and a new document D:

> fast, couple, shoot, fly

#### compute the most likely class for D. Assume a naive Bayes classifier and use   add-1 smoothing for the likelihoods.

    Let 'C' and 'A' represent 'comedy' and 'action' respectively.

    P(C) = 2/5
    P(A) = 3/5

    tokens(): fun, couple, love, fast, furious, shoot, fly

    P(fast|C) = (1+1)/(9+7) = 0.125
    P(fast|A) = (2+1)/(11+7) = 0.1667

    P(couple|C) = (2+1)/(9+7) = 0.1875
    P(couple|A) = (0+1)/(11+7) = 0.0556

    P(shoot|C) = (0+1)/(9+7) = 0.0625
    P(shoot|A) = (4+1)/(11+7) =0.2778

    P(fly|C) = (1+1)/(9+7) = 0.125
    P(fly|A) = (1+1)/(11+7) = 0.1111

    C_NB_1 = P(C)*P(fast|C)*P(couple|C)*P(fly|C) = 7.324219e-05

    C_NB_2 = P(A)*P(fast|A)*P(couple|A)*P(fly|A) = 1.716358e-4

    C_NB_2>C_NB_1

Thus, Naive bayes will assign **action class**


#### 4.3 Train two models, multinomial naive Bayes and binarized naive Bayes, both with add-1 smoothing, on the following document counts for key sentiment words, with positive or negative class assigned as noted.

| doc | 'good' | 'poor' | 'great' | class |
|---|---|---|---|---|
| d1 | 3 | 0 | 3 | pos |
| d2 | 0 | 1 | 2 | pos |
| d3 | 1 | 3 | 0 | neg |
| d4 | 1 | 5 | 2 | neg |
| d5 | 0 | 2 | 0 | neg |

#### Use both naive Bayes models to assign a class (pos or neg) to this sentence:

> A good, good plot and great characters, but poor acting.

#### Do the two models agree or disagree?

    P(pos) = 2/5
    P(neg) = 3/5

    Multinomial naive Bayes
    P(good|pos) = (3+1)/(9+3) = 0.3333
    P(poor|pos) = (1+1)/(9+3) = 0.1666
    P(great|pos) = (5+1)/(9+3) = 0.5

    P(good|neg) = (2+1)/(14+3) = 0.1765
    P(poor|neg) = (10+1)/(14+3) = 0.6471
    P(great|neg) = (2+1)/(14+3) = 0.1765

    C_MNB_1 = logP(pos) + 2*logP(good|pos) + logP(poor|pos) + logP(great|pos) = -5.598422

    C_MNB_2 = logP(neg) + 2*logP(good|neg) + logP(poor|neg) + logP(great|neg) = -6.149947

    C_MNB_1 > C_MNB_2

Thus, Multinomial naive Bayes will assign **positive class**

| doc | 'good' | 'poor' | 'great' | class |
|---|---|---|---|---|
| d1 | 1 | 0 | 1 | pos |
| d2 | 0 | 1 | 1 | pos |
| d3 | 1 | 1 | 0 | neg |
| d4 | 1 | 1 | 1 | neg |
| d5 | 0 | 1 | 0 | neg |

    Binary naive bayes
    Multinomial naive Bayes
    a P(good|pos) = (1+1)/(4+3) = 0.2857
    b P(poor|pos) = (1+1)/(4+3) = 0.2857
    c P(great|pos) = (2+1)/(4+3) = 0.4286

    d P(good|neg) = (2+1)/(6+3) = 0.3333
    e P(poor|neg) = (3+1)/(6+3) = 0.4444
    f P(great|neg) = (1+1)/(6+3) = 0.2222

    C_BNB_1 = logP(pos) + 2*logP(good|pos) + logP(poor|pos) + logP(great|pos) = -5.5219

    C_BNB_2 = logP(neg) + 2*logP(good|neg) + logP(poor|neg) + logP(great|neg) = -5.023058

    C_MNB_1 < C_MNB_2
Thus, Binary naive Bayes will assign **negative class**
