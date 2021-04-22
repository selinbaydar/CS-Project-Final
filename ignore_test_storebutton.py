with open('MC_options.txt') as f: #opens the textfile with the MC option names
    labels=[line.strip() for line in f.readlines()]
counter_option = 0 #initializing

#inside image loop but outside the crop loop
counter_option = counter_option + 4 #this will be at the end of the loop once the crop loop is done
counter1 = counter_option
counter2 = counter_option +1
counter3 = counter_option +2
counter4 = counter_option +3
option1 = labels[counter1]
option2 = labels[counter2]
option3 = labels[counter3]
option4 = labels[counter4]
print(option4)
