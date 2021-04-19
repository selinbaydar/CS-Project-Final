# CLPS0950-Project-Final
# EJR pushed this to github!
# written by JO
# Important: The README file in your GitHub should be instructive and detailed enough that anyone can run your code with ease. This includes: specifying which toolboxes/add ons need to be downloaded/used, Making any data needed for data analysis accessible/shared with TAs, Making your repository public, and not private

This repository uses pytorch image recognition in python to examine meachine learning. Specifically, we compared 5 network models in a image recognition task. Images were selected by us and then zoomed in at 15 different levels. The goal was to examine the performance differences for the models by tracking when the models accurately identify the image. The second part of this project implements a GUI and instructs users to identify the image, starting with the most zoomed in image, via a multiple-choice option. 
# possible 3rd part of comparing data? 

This project is coded in python, we recommend using VisualStudioCode and a conda based Python interpreter such as: Python 3.8.5 64-bit (conda). Before implementation, please make sure you have updated versions of pytorch and tkinter installed. In addition, matplotlib will also need to be installed (conda install -c conda-forge matplotlib
 for OS in terminal)

Download the repository that will include the code, images, answerkeys, etc. The only changes necessary will be to define your current local path in zoom_game.py and GUI_mainscript.py. 

A brief overview of project-related files within the repositiory:
All tested images are saved as jpg files 
zoom_game.py - feeds zoomed in image to each network model, zooms out until the model is able to accurately identify the image. Repeats for each image
crop_img.py - crops the images 
# does this also zoom out? 
GUI_mainscript.py - presents GUI asking user to identify zoomed in image, zooms out until image accurately identified. Repeats for each image
answer_graphs.py - summary of human vs network model performance 
answer_key.txt - answer key for images 

In order to see network performance, run zoom.py. To process the code without directly seeing the image yourself and only seeing the models' output, comment out line 22 on crop_img.py and save the file. zoom_game.py will not work unless all the images and answer key are locally in your system and the pathway is changed to match yours. For this to work, change the directory in line 175 of zoom_game.py. 

In order to test human performance, run GUI_mainscript and play along. Change line 95 pathway to match your own. 

In order to see your performance vs the five models, run answer_graphs.py. 


