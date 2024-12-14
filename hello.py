import tkinter as tk
from tkinter import messagebox

# Questions and answers
questions = [
    {
        "question": "What is the shape of a football used in official matches?",
        "options": ["Square", "Circle", "Oval", "Hexagon"],
        "answer": 1
    },
    {
        "question": "How many players are on the field for one team in a standard football match?",
        "options": ["9", "10", "11", "12"],
        "answer": 2
    },
    {
        "question": "Which country has won the most FIFA World Cup titles?",
        "options": ["Germany", "Italy", "Argentina", "Brazil"],
        "answer": 3
    },
    {
        "question": "What is the maximum duration of a standard football match, excluding extra time?",
        "options": ["60 minutes", "90 minutes", "100 minutes", "120 minutes"],
        "answer": 1
    },
    {
        "question": "Which European club has won the most UEFA Champions League titles?",
        "options": ["Manchester United", "FC Barcelona", "Real Madrid", "Bayern Munich"],
        "answer": 2
    }
]

current_question = 0
score = 0
wrong_count = 0

def check_answer(selected_option):
    global current_question, score, wrong_count

    # Check if the answer is correct
    if selected_option == questions[current_question]['answer']:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text="Wrong!", fg="red")
        wrong_count += 1

    # Move to the next question after a brief delay
    current_question += 1
    if current_question < len(questions):
        window.after(1000, load_question)
    else:
        window.after(1000, end_game)

def load_question():
    feedback_label.config(text="")
    question_label.config(text=questions[current_question]['question'])

    # Update options
    for i, option in enumerate(questions[current_question]['options']):
        options[i].config(text=option, bg="SystemButtonFace")

def end_game():
    messagebox.showinfo("Game Over", f"Your score: {score}/{len(questions)}\n\nWrong answers: {wrong_count}")
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Who Wants to Be a Millionaire")
window.geometry("600x400")
window.resizable(False, False)

# Question label
question_label = tk.Label(window, text="", font=("Arial", 16), wraplength=500, justify="center")
question_label.pack(pady=20)

# Buttons for options
options = []
for i in range(4):
    btn = tk.Button(window, text="", font=("Arial", 14), width=20, command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    options.append(btn)

# Feedback label
feedback_label = tk.Label(window, text="", font=("Arial", 14))
feedback_label.pack(pady=20)

# Load the first question
load_question()

# Run the window
window.mainloop()
