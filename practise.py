import sys, json

def go():
    d = json.load(open("words.json"))
    #skip = {"verbs"}
    skip = {}
    score = 0
    total = 0
    practise = [x for x in d if x not in skip]
    for x in practise:
        for y in d[x]:
            print(y)
            score_part = 0
            for v, k in d[x][y].items():
                total += 1
                print('--->', v)
                l = sys.stdin.readline().strip('\n')
                alt = k.split(' ')
                if (l == k or l == "" or (len(alt) > 1 and l == alt[1] and (alt[0] == 'ils/elles' or alt[0] == 'il/elle'))):
                    print (u'\U0001f604')
                    score += 1
                    score_part += 1
                else:
                    print(u'\U0001F914 ----> ', k)
            print(u'\n\U0001F353   -- score on: ', x, ':', score_part/len(d[x][y]), '\n')
        score = score/total
        if score >= 0.7:
            print(u'----- good JOB!!\U0001F389')
        else:
            print(u'----- hit the books girl!\U0001F4DA')
        
go()
