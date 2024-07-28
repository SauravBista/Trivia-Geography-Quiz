THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class SetUi:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f"score = {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="question",width=280, fill=THEME_COLOR, font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan =2, pady=50)
        true_image = PhotoImage(file="./images/true.png")
        self.button_true =Button(image=true_image, highlightthickness=0, command=self.right_answer)
        self.button_true.grid(row=2, column=0)
        false_image = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.wrong_answer)
        self.button_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more quesiton left")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)



    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

