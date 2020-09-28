# Section 2

#### 2.1

    a. False
    b. True
    c. False
    d. False

#### 2.2

    a. because
    b. Shia, Shiite
    c. Hawaii
    d. o Rourke

#### 2.3
    c. marketing/markets
    # because marketing is a subject in commerce, but markets indicates more a place that sell goods

    d. university/universe
    # their definition and meaning is too different

#### 2.4

    a. to distiguish from 'S -> ', when two 's' appear at the same time, then the later one won't be reduced.

    b. circus -> circu;  canaries -> canari;  boss -> boss

    c. bies OR cies OR dies OR fies OR gies OR hies OR jies OR kies OR lies OR mies OR nies OR pies OR qies OR ries OR sies OR ties OR vies OR wies OR xies OR z
    -> by OR cyy OR dy OR fy OR gy OR hy OR jy OR ky OR ly OR my OR ny OR py OR qy OR ry OR sy OR ty OR vy OR wy OR xy OR zy

    d. it might has deleterious effect as it might decrease the precision of results

#### 2.5
    Becuase when do 'x OR y', we need to traverse all the indexes in both x and y, thus skip is not helpful here.

#### 2.6
    a. 11
    b. 5

#### 2.7
    a. 4 times
    b. 17 times
    c. 18 times

#### 2.8
> Is there a York University in New York?

#### 2.9
    a. "fools rush"(2 4 7) and "rush in" (2 4)
       Return 2,4
    b. "angles fear"(4 7) and "fear to" (4 7) and "to tread"(4 7)
      Return 4

#### 2.10
    a. Return 1,3
    b. k = 1 (3), k = 2 (1, 3), k = 5 (1, 2, 3)

#### 2.11
    L

#### 2.12
    a. # First judge if the terms are contained in the same document, if no, traverse the document ID, whose is less who move to the next point.

    If yes, then need to judge if the position of these two terms are satisfied with the requirement position distance 'k'. Keep PP1, check if the distance between PP1 with PP2 is satisfied, if yes, then save the location of PP2, else move PP2 to the next if it is less than PP1, or move PP1 to  the next.

    Once there is record for PP2, it means we have document and locations can be saved. Add the document ID, and the locations to the answer. Else, move the smaller pointer of documents.

    b. P^2*L^2

    c. ?

#### 2.13
    a. we do not need to move backwards, just need to check if the absolute of the distance between two pointers is <=k

    c. For example, term 'a' appear once, so does term 'apple'. if we want to have the intersection of 'a apple /k'. then we only need to compare the document number amd their location, do two times operation.

#### 2.14
    # When constructing the posting, ignore the terms of stop words, also delete the stop words in the query.
    # The potentional problem is it will decrease the precision. For example, if I want to search for 'The white house', without stop words, the return will include documents like 'I prefer a white house', etc.

# Section 6

#### 6.1
    yes

#### 6.2
    score = {0.2, 0.31, 0.49, 0.51, 0.69, 0.8, 1}

#### 6.3
    # input: Q = {q1, q2, ..., qn}
    ZONESCORE(Q)
        n = length(Q)
        float scores[N] = [-1] # N is the amont of document
        constant g[l]
        P <- postings(Q) # P contains n postings
        # find and evaluate the score of documents that contain both q_i and q_{i+1}
        # use the origional score of the document times the new scores        
        for i in 1:2:n-1
            p1 <- postings{q_i}
            p2 <- postings{q_{i+1}}
            p1 <- intersection(p1, doc_ID)
            p2 <- intersection(p2, doc_ID)
            while p1 \neq NIL and p2 \neq NIL
              # only when the document contains the terms and meanwhile the before checked terms contained in this document, its score will get updated.
              do if docID(p1) = docID(p2) AND scores[docID(p_1)] != 0
                 then scores[docID(p_1)] <- scores[docID(p_1)] + WEIGHTEDZONES(p1,p2,g)
                  p1 <- next (p1)
                  p2 <- next (p2)
              else if docID(p1) < docID(p2)
                 then p1 <- next (p1)
                 # if the document does not contain the term, then its score will become 0
                 scores[docID(p_1)] <- 0 * scores[docID(p_1)]
              else
                  p2 <- next (p_2)
                  # if the document does not contain the term, then its score will become 0
                  scores[docID(p_2)] <- 0 * scores[docID(p_2)]
       return scores

#### 6.4
    # p1, p2 is the pointer of posting q1 and q2
    WEIGHTEDZONES(p1,p2,g)
      score1 = 0
      score2 = 0
      m = length(p1) # the frequency of term p1 appear in this document
      n = length(p2) # the frequency of term p2 appear in this document

      for i in m
        j in length(g)
          if p1[i][2] == g[j]
            score1 = score1 + g[j]
      for i in n
        j in length(g)
          if p2[i][2] == g[j]
            score2 = score2 + g[j]

      Return score1 + score2

#### 6.5
> calculate the weight **g** for **title**
    # the term not appear in the title but appear in th ebody, and the judgement is relative
    n_{01r} = 2

    # the term not appear in the title but appear in th ebody, and the judgement is non-relative
    n_{01n} = 1

    # the term appear in the title but not appear in th ebody, and the judgement is relative
    n_{10r} = 0

    # the term appear in the title but not appear in th ebody, and the judgement is non-relative
    n_{10n} = 1

    g = (n_{10r} + n_{01n})/(n_{01r} + n_{01n} + n_{10r} + n_{10n}) = (0 + 1)/(2+1+1) = 1/4 = 0.25


#### 6.6
    Example(1) = 1
    Example(2) = 0.75
    Example(3) = 0.75
    Example(4) = 0
    Example(5) = 1
    Example(6) = 0.75
    Example(7) = 0.25

    The higher the score is, the more likely the query and docuemnt are relevant

#### 6.7
    Intuitively, becaue it can not contribute to the difference of terms being contained in 'body' and in 'title'.
