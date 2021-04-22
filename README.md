# CLPS0950-Project-Final

This repository uses pytorch image recognition in python to examine meachine learning. Specifically, we compared 5 network models in a image recognition task. Images were selected by us and then zoomed in at 15 different levels. The goal was to examine the performance differences for the models by tracking when the models accurately identify the image. The second part of this project implements a GUI and instructs users to identify a zoomed image via a multiple-choice options. 


This project is coded in python, we recommend using VisualStudioCode and a conda based Python interpreter such as: Python 3.8.5 64-bit (conda). Before implementation, please make sure you have updated versions of pytorch and tkinter installed. In addition, matplotlib will also need to be installed (conda install -c conda-forge matplotlib
 for OS in terminal)

Download the repository that will include the code, images, answerkeys, etc. The only changes necessary will be to define your current local path in zoom_game.py and GUI_final.py. 

A brief overview of project-related files within the repositiory:

All tested images are saved as jpg files 
zoom_game.py - feeds zoomed in image to each network model, zooms out until the model is able to accurately identify the image. Repeats for each image
crop_img.py - crops the images 
GUI_final.py - presents GUI asking user to identify zoomed in image. Tells the user if they are right or wrong from the command window. Repeats for each image
answer_graphs.py - summary of human vs network model performance 
answer_key.txt - answer key for images
GUI_answer.txt - answer key for GUI multiple choice questions
images_names.txt - assigns image to GUI based on question number

Note: Any additional files were created for practice and tutorial purpose, therefore begin with "ignore".

In order to see network performance, run zoom.py. To process the code without directly seeing the image yourself and only seeing the models' output, comment out line 22 on crop_img.py and save the file. zoom_game.py will not work unless all the images and answer key are locally in your system and the pathway is changed to match yours. For this to work, change the directory in line 175 of zoom_game.py. 

In order to test human performance, run GUI_final.py and play along. Change line 95 pathway to match your own. 

In order to see the performance of the fiv models run answer_graphs.py. 


