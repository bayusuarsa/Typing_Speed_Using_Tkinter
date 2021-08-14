from tkinter import *
from tkinter import messagebox
import requests
from timeit import default_timer as timer

# Todo 2 Loading the word from API
def get_word():
    """Get the Word from API"""
    global data, start
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(word_text, text=data["quote"])
    start = timer()

# Todo 3 Checking our results
def check_result():
    """Check the result of our typing with the word"""
    input = input_entry.get().split()
    error = 0
    words = data["quote"].split()
    end = timer()
    for word in range(len(input)):
        if word in (0, len(input)-1):
            if input[word] == words[word]:
                continue
            else:
                error +=1
        else:
            if input[word] == words[word]:
                if (input[word+1] == words[word+1]) & (input[word-1] == words[word-1]):
                    continue
                else:
                    error +=1
            else:
                error +=1

    end_time = end - start
    speed = len(input) / end_time
    messagebox.showinfo("Time", f"Your time is {end_time} seconds\nYour speed of typing is {speed} words/minute")
    messagebox.showinfo("Error", f"You have {error} error")

# Todo 1. Make a User Interface
start = timer()
window = Tk()
window.title("Typing Speed")
window.config(padx=50, pady=50)
label_1 = Label(window, text="Test Your Typing Speed", font=('arial', 15, 'bold')).grid(row=0, column=1, rowspan=1)

canvas = Canvas(width=300, height=200)
canvas.grid(row=1, column=1)
word_text = canvas.create_text(150,100, text="Wait For You to click start", width=250, font=('arial', 15, 'bold'))

input_entry = Entry(width=50)
input_entry.grid(row=2, column=0, columnspan=3)
start_button = Button(text="Start", command=get_word)
start_button.grid(row=3,column=0)

check_button = Button(text="Check", command=check_result)
check_button.grid(row=3,column=2)
window.mainloop()