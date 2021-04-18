#EJR wrote this code on 4/13 to test the photos in our folder, make sure the order would match the key, etc. 
with open('answer_key.txt') as g:
    answers=[line.strip() for line in g.readlines()]
    img_counter=0
    new_answer = answers[0].split(',')
    print(new_answer[1])
    #index1=['cheeseburger', 98]
    #alex_sl = [index1[0]==answers[img_counter]]
    #print(alex_sl)
    #squeeze_sl = squeeze_sl + [labels[index2[0]]==answers[img_counter]]
