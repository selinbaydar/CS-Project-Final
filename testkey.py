#EJR wrote this code on 4/13 to test the photos in our folder, make sure the order would match the key, etc. 
with open('answer_key.txt') as g:
    answers=[line.strip() for line in g.readlines()]
    img_counter=2
    print(answers[img_counter], answers[0])

