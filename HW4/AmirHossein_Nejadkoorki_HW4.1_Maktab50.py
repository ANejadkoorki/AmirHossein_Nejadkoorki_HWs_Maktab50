#FirstQuestion
input_string = "The quick brown fox jumps over the lazy dog"
output_string = print("".join([input_string.split(" ")[i][1] for i in range(len(input_string.split(" ")))]))
#SecondQuestion
scores = {'Art':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Math':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 1},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 2},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Literature':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 3},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 1},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 2}],
          'Physics':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4}],
          'Chemistry':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 2},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 3}]}
lesson_scores = dict()
for i in scores:
    i_scores = []
    for j in range(len(scores[i])):
        i_scores.append(scores[i][j]['score'])
    lesson_scores[i] = i_scores
print(lesson_scores)
print("--------------------------------------------------------")
person_scores = {}
for i in scores:
    for j in range(len(scores[i])):
        person_scores[scores[i][j]['first_name'] + " " + scores[i][j]['last_name']] = None
#Robert scores
lR = []
for R in scores:
    lR.append(scores[R][0]['score'])
person_scores['Robert Smith'] = lR
#Mary scores
lMary = []
for Mary in scores:
    if Mary == 'Physics'  or  'Chemistry':
        continue
    elif Mary == 'Art':
        lMary.append(scores[Mary][1]['score'])
    else:
        lMary.append(scores[Mary][2]['score'])
person_scores['Mary Hernandez'] = lMary
#Maria Scores
lMaria = []
for Maria in scores:
    if Maria == 'Art' or 'Physics'  or  'Chemistry':
        continue
    else:
        lMaria.append(scores[Mary][1]['score'])
person_scores['Maria Garcia'] = lMaria
#James scores
lJames = []
for James in scores:
    if James =='Art' or 'Math' or 'Physics' :
        continue
    elif James == 'Chemistry':
        lJames.append(scores[Mary][1]['score'])
    else:
        lJames.append(scores[Mary][3]['score'])
person_scores['James Johnson'] = lJames
print(person_scores)
print('-----------------------------------------------------------------------------')

person_scores = {"Robert Smith" : None,"Maria Garcia" : None,"Mary Hernandez" : None,"James Johnson" : None}
Robert_result,Maria_result,Mary_result,James_result = {},{},{},{}
for R_res in scores:
    Robert_result[R_res] = scores[R_res][0]['score']
person_scores["Robert Smith"] = Robert_result
for Maria_res in scores:
    if Maria_res == 'Art' or 'Physics' or 'Chemistry':
        continue
    Maria_result[Maria_res] = scores[Maria_res][1]['score']
person_scores["Maria Garcia"] = Maria_result
for Mary_res in scores:
    if Mary_res == 'Physics' or 'Chemistry':
        continue
    elif Mary_res == 'Art':
        Mary_result[Mary_res] = scores[Mary_res][1]['score']
    else:
        Mary_result[Mary_res] = scores[Mary_res][2]['score']
person_scores["Mary Hernandes"] = Mary_result
for J_res in scores:
    if J_res == 'Art' or 'Math' or 'Physics':
        continue
    elif J_res == 'Chemistry':
        James_result[J_res] = scores[J_res][1]['score']
    else:
        James_result[J_res] = scores[J_res][3]['score']
person_scores["James Johnson"] = James_result

print(person_scores)
print('---------------------------------------------------------------------------------------')
print("code by AmirHossein Nejadkoorki")







































