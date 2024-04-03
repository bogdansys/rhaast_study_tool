# Welcome to Rhaast!

## Overview

This Python program is designed to help you study for various courses and topics. It allows you to add courses and topics, and then add questions for each topic. You can then go through each question one by one, entering an answer for each. Your answers are saved in a text file for future reference.

## Directory Structure

The program creates a directory named "courses" in the same directory as the script. Each course is a subdirectory of "courses", and each topic is a subdirectory of its respective course. The questions and answers for each topic are stored in text files within the topic's directory.

## How to Use

1. **Course Selection**: The program lists all the courses and prompts you to enter a course number or "add" to add a new course. If you enter "add", it prompts you to enter the name of the new course and creates a new directory for the course. If you enter a course number, it selects the corresponding course and proceeds to the topic selection stage.

2. **Topic Selection**: The program lists all the topics for the selected course and prompts you to enter a topic number or "add" to add a new topic. If you enter "add", it prompts you to enter the name of the new topic and creates a new directory for the topic under the course's directory. If you enter a topic number, it selects the corresponding topic and proceeds to the study stage.

3. **Study Stage**: The program checks if there are any questions for the selected topic. If there are no questions, it prompts you to enter your questions all at once, separated by new lines, and saves them in a text file in the topic's directory. Then, it goes through each question one by one, allowing you to enter an answer for each. Your answers are saved in a text file named `answers.txt` in the topic's directory.

4. **Save and Exit**: While answering questions, you can enter "000" to save your answers and return to the main menu. The prompt for entering an answer indicates this option.

## Running the Program

To run the program, navigate to the directory containing the script in your terminal and type `python3 main.py`.

### Name origin
Wondering where the name comes from? It's a reference to League of Legends where Rhaast is known as a very powerful and useful tool that also talks to you. Hence, this being a powerful and useful study tool, the name stuck :)
PS: I dont play League of Legends
