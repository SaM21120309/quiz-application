from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

#Starting Screen

def start_quiz():
    
    #Second Screen
    
    def show_question():
        # Get the current question from the quiz_data list
        question = quiz_data[current_question]
        qs_label.config(text=question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):
            choice_btns[i].config(text=choices[i], state="normal") # Reset button state

        # Clear the feedback label and disable the next button
        feedback_label.config(text="")
        next_btn.config(state="disabled")

    # Function to check the selected answer and provide feedback
    def check_answer(choice):
        # Get the current question from the quiz_data list
        question = quiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")

        # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
            # Update the score and display it
            global score
            score += 1
            score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
            feedback_label.config(text="Correct!", foreground="green")
        else:
            feedback_label.config(text="Incorrect!", foreground="red")
        
        # Disable all choice buttons and enable the next button
        for button in choice_btns:
            button.config(state="disabled")
        next_btn.config(state="normal")

    # Function to move to the next question
    def next_question():
        global current_question
        current_question +=1

        if current_question < len(quiz_data):
            # If there are more questions, show the next question
            show_question()
        else:
            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
            window.destroy()

    # Create the main window
    window = ttk.Window(themename ="cyborg")
    window.title("Quiz App")
    window.geometry("700x600")
    style = Style()

    # Configure the font size for the question and choice buttons

    style.configure("TLabel", font=("Helvetica", 20))
    style.configure("TButton", font=("Helvetica", 16))

    # Create the question label
    qs_label = ttk.Label(
        window,
        anchor="center",
        wraplength=500,
        padding=10,
        font=("Helvetica", 20),
        background="Black",
        foreground="White"
    )
    qs_label.pack(pady=10)

    # Create the choice buttons
    choice_btns = []
    for i in range(4):
        button = ttk.Button(
            window,
            command=lambda i=i: check_answer(i),
            bootstyle='danger-outlines',
            width=20
        )
        button.pack(pady=5)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = ttk.Label(
        window,
        anchor="center",
        padding=10,
        font=("Helvetica", 20),
        background="Black",
        foreground="White"
    )
    feedback_label.pack(pady=10)

    # Create the score label
    score_label = ttk.Label(
        window,
        text="Score: 0/{}".format(len(quiz_data)),
        anchor="center",
        padding=10,
        font=("Helvetica", 20),
        background="Black",
        foreground="White"
    )
    score_label.pack(pady=10)

    # Create the next button
    next_btn = ttk.Button(
        window,
        text="Next",
        command=next_question,
        state="disabled"
    )
    next_btn.pack(pady=10)

    # Show the first question
    show_question()
    
#main Screen

root = ttk.Window(themename ="cyborg")
root.title("Quiz App")
root.geometry("500x300")
style = Style()

# Configure the font size for the question and choice buttons

style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Configure the font size for the question and choice buttons

#first Screen Label

st_label = ttk.Label(
    root,
    text="Test Iq",
    anchor="center",
    wraplength=500,
    padding=10,
    font=("Helvetica", 20),
    background="Black",
    foreground="White"
)
st_label.pack(pady=50)

#first screen button

st_btn = ttk.Button(
    root,
    text="Start",
    command = start_quiz,
    bootstyle='danger-outlines',
    width=20
)
st_btn.pack(pady= 10)

# Initialize the score

score = 0

#initializing the question index

current_question = 0

root.mainloop()