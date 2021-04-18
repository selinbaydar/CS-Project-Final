#focus on applying GUI with checkmarks for users - possible inclusion to our GUI as options 
#written by jessica
#debug by selin and jay
#loops written by jay


# to do: write a text file MC options for each image
# to do: integrate text file into names of button options
# to do: how to loop through we 
# import all required packages and functions
#format: w = Checkbutton ( master, option, ... )
from tkinter import *
from PIL import Image, ImageTk
from torchvision import transforms
import tkinter
import os
import numpy as np
from crop_img import crop_me
from zoom_game import zoom_game

# import ipdb;ipdb.set_trace() #setting a breakpoint
#modified tutorial code for this porject 
#define a function that has an input called my_directory
def user_interface(my_directory)
    #double check that this directory exists
    if os.path.exists(my_directory):
        print('path exists')
    # loop over each jpg image in directory
    my_files=os.listdir(my_directory)
    # sort files in alphabetical order 
    my_files=sorted(my_files)

    #initialize vector where the user's answers to each photo and crop level will be stored
    user_sl = []
    img_counter = 0
    for filename in my_files:
        # initialize img_counter to keep track of which image we are at
        if filename.endswith(".jpg"):
            image_counter=os.path.join(my_directory, filename)
        else:
            continue
        #open the answerkey for our ten images
        with open('answer_key.txt') as g:
            answers=[line.strip() for line in g.readlines()]
        #load image
        img = Image.open(image_counter)
        left_box=190
        upper_box=190
        right_box=210
        lower_box=210
        counter=max(left_box,upper_box,right_box,lower_box)
        # now take the image and zoom in on it using a the function crop_me
        crop_level = 1
        while counter < 400: # we don't want the cropped dimensions to exceed the size of the photo, which is normalized to 400x400
            #display message to state crop level and which image we are looking at so that user can follow along with terminal window
            my_msg = 'We are at crop level:'
            my_msg2 = 'of image:'
            my_msg3 = answers[img_counter].split(',')
            crop_msg= str(crop_level)
            print(my_msg+crop_msg+ ' ' +my_msg2+ ' ' + my_msg3[1])
            img_croped = crop_me(img,left_box,upper_box,right_box,lower_box)
            


            ### INSERT GUI code here to have user generate outputs
            #define outputs 
            # out1 = answer to clicking botton from user 
            # out2
            # out3
            # out4


            # img_counter is keeping track of what image we are on, so each row should correspond
            # individual model answer in vector
            # user_sl = user_sl + ['if button is correct'==answers[img_counter]]
            print(user_sl)
            if 'if button is correct' == answers[img_coutner]
                break
            # to do: figure out how to autofill the rest of the row with TRUE
            else:
            # repeat loop only if answers are all correct or not
            left_box = left_box - 10
            upper_box = upper_box - 10
            right_box = right_box + 10
            lower_box = lower_box + 10
            counter=max(left_box,upper_box,right_box,lower_box)
            crop_level = crop_level+1

        # increment img_counter, which keeps track of which photo and therefore which answer key index we are at
        img_counter = img_counter+1
    #reshape the answer so that each row corresponds to one model     
    user_sl = np.reshape(user_sl,[10,19])

    return(user_sl)
user_interface('C:\\Users\emmar\Documents\CLPS0950\CS-Project-Final') #find a way to make this accessible to everyone's computer rather than making it local

##### This is where non pasted content starts

#initialize window
top = tkinter.Tk()
#define window size
top.geometry("1000x1000+1000+1000")
# what is top??
#creates text at the top of GUI, would use to give instructions.
text = Text(top)
# to do: maybe change to labels
text.insert(INSERT, "Please identify the image. ")
text.insert(END, "Select only one option. ")
text.pack()
# to do: action item - make the text portion smaller when displayed, right now takes up half the window

# Create a photoimage object of the image in the path
image1 = Image.open("burger.jpg")

#transform image so that it is small enough to fit on the display
transform = transforms.Compose([transforms.Resize(240),transforms.CenterCrop(224)])
image1 = transform(image1)

test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(top,image=test)
label1.image = test

# Position image
label1.place(x = 400, y= 40)
# top.mainloop()
# to do:do we want to include the image in the GUI - if so...https://www.activestate.com/resources/quick-reads/how-to-add-images-in-tkinter/


#how many variables/options want to have 
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

#define visual aspects of it (master, option....)

with open('MC_options.txt') as f: #opens the textfile with the MC option names
    labels=[line.strip() for line in f.readlines()]

option1 = labels[0]
option2 = labels[1]
option3 = labels[2]
option4 = labels[3]

counter_option = 0 #initializing

#inside image loop but outside the crop loop
counter_option = counter_option + 4 #this will be at the end of the loop once the crop loop is done
counter1 = counter_option
counter2 = counter_option +1
counter3 = counter_option +2
counter4 = counter_option +3

for counter_option in range(0,16):
    option1 = labels[counter1]
    option2 = labels[counter2]
    option3 = labels[counter3]
    option4 = labels[counter4]

    #convert the options into strings
    option1 = str(option1)
    option2 = str(option2)
    option3 = str(option3)
    option4 = str(option4)

C1 = Checkbutton(top, text = option1, variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10,)
C2 = Checkbutton(top, text = option2, variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C3 = Checkbutton(top, text = option3, variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C4 = Checkbutton(top, text = option4, variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C1.pack()
C2.pack()
C3.pack()
C4.pack()

top.mainloop()