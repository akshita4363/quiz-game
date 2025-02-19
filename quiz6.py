import tkinter as tk
from tkinter import StringVar
from tkinter import ttk

root = tk.Tk()
root.title("Quiz game")
root.geometry('500x500')
custom = ttk.Style()
custom.configure('Custom.TRadiobutton',indicatorsize=20,background="lightblue",font=('verdana',25),wraplength=2000)

questions = ["what does AI stands for?",
"which programming language is commonly used for implementing AI algorithms?",
"what is the primary goal of AI?",
"which is not a subfield of AI?",
"what is the term used for process of training an AI model on a dataset to make predictions or decisions?",
"which is the following is an example of a supervised learning algorithm?",
"which AI technique focusses on enabling computers to understand,interpret,and generate human like text?",
"what is the term used for ability of AI systems to improve their performance without explicit programming?",
"what is the turing test?",
"which company developed the first virtual assistant,SIRI?"]



options = [["Artificial Island", "Automated Intelligence", "Artificial Intelligence","All Inclusive","Artificial Intelligence"],
           ["Java", "Python", "C++","Javascript","Python"],
           ["To replace humans", "To replicate Human Intelligence", "To create robots","To solve complex problems efficiently","To solve complex problems efficiently"],
           ["Machine learning", "Natual Language Processing", "Robotics","Datamining","Datamining"],
           ["Compilation", "Simulation", "Learning","Inference","Learning"],
           ["K means clustering", "Decision Trees", "Random Forest","K-nearest neighbors","Decision Trees"],
           ["Computer vision", "Natural Language Processing", "Speech Recognition","Expert Systems","Natural Language Processing"],
           ["Reinforcement Learning", "Unsupervised Learning", "Self improvement","Adaptation","Reinforcement Learning"],
           ["test to determine if a computer can exhibit intelligent bhaviour equivalent to a human","A test to determine if a computer can play chess","A test to determine if a computer can write poetry","A test to determine if a computer can recognize objects in images","test to determine if a computer can exhibit intelligent behaviour equivalent to a human"], ["Google", "Apple", "Microsoft","Amazon","Apple"]]

frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=100,bg='navy blue',fg="#fff", 
                          font=('Verdana', 20),wraplength=600)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = ttk.Radiobutton(frame,  variable=v1,style = 'Custom.TRadiobutton',
                         command = lambda : checkAnswer(option1))
option2 = ttk.Radiobutton(frame,  variable=v2,style = 'Custom.TRadiobutton',
                         command = lambda : checkAnswer(option2))
option3 = ttk.Radiobutton(frame, variable=v3, style = 'Custom.TRadiobutton',
                         command = lambda : checkAnswer(option3))
option4 = ttk.Radiobutton(frame,  variable=v4, style = 'Custom.TRadiobutton',
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)

index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'


    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options)-1:
            button_next['text'] = 'Check the Results'


displayNextQuestion()

root.mainloop()
