import tkinter as tk
from tkinter import Text, Label, Entry,scrolledtext
from backend import check_answer
from tkinter import filedialog

def create_gui():
    def evaluate_answer():
        teacher_solution = teacher_solution_text.get("1.0", "end-1c")
        student_answer = student_answer_text.get("1.0", "end-1c")
        max_marks = 10  # Change this to the actual maximum marks
        question = "Describe the causes and consequences of the Industrial Revolution in the 19th century."

        result = check_answer(teacher_solution, student_answer, max_marks, question)

        # Extract marks and explanations
        result_dict = eval(result)
        marks = result_dict.get("marks")
        explanation = result_dict.get("explanation")

        # Display marks and explanation in the Entry widgets
        marks_entry.delete(0, "end")
        marks_entry.insert(0, marks)

    def open_teacher_solution_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                teacher_solution_text.delete("1.0", "end")
                teacher_solution_text.insert("1.0", file.read())

    def open_student_answer_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                student_answer_text.delete("1.0", "end")
                student_answer_text.insert("1.0", file.read())

    root = tk.Tk()
    root.title("Answer Evaluation")

    # Make the window fullscreen
    root.attributes('-fullscreen', True)

    # Create a frame for teacher's solution on the left
    teacher_solution_frame = tk.Frame(root)
    teacher_solution_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    teacher_solution_frame.grid_rowconfigure(0, weight=1)
    teacher_solution_frame.grid_columnconfigure(0, weight=1)

    teacher_solution_label = tk.Label(teacher_solution_frame, text="Teacher's Solution")
    teacher_solution_label.grid(row=0, column=0, padx=10, pady=(0, 10))

    teacher_solution_text = Text(teacher_solution_frame, wrap=tk.WORD, height=40, width=50)
    teacher_solution_text.grid(row=1, column=0, padx=10, pady=(0, 10))

    teacher_solution_button = tk.Button(teacher_solution_frame, text="Open from File", command=open_teacher_solution_file)
    teacher_solution_button.grid(row=2, column=0, padx=10, pady=(0, 10))

    # Create a frame for student's answer on the right
    student_answer_frame = tk.Frame(root)
    student_answer_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    student_answer_frame.grid_rowconfigure(0, weight=1)
    student_answer_frame.grid_columnconfigure(0, weight=1)

    student_answer_label = tk.Label(student_answer_frame, text="Student's Answer")
    student_answer_label.grid(row=0, column=0, padx=10, pady=(0, 10))

    student_answer_text = Text(student_answer_frame, wrap=tk.WORD, height=40, width=50)
    student_answer_text.grid(row=1, column=0, padx=10, pady=(0, 10))

    student_answer_button = tk.Button(student_answer_frame, text="Open from File", command=open_student_answer_file)
    student_answer_button.grid(row=2, column=0, padx=10, pady=(0, 10))

    evaluation_frame = tk.Frame(root)
    evaluation_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    evaluation_frame.grid_rowconfigure(0, weight=1)
    evaluation_frame.grid_columnconfigure(0, weight=1)

    evaluation_labels = ["Marks:", "Accuracy:", "Completeness:", "Relevance:", "Clarity:"]
    
    row = 0
    explanation_label = Label(evaluation_frame, text="Explanation:")
    explanation_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    
    explanation_text = scrolledtext.ScrolledText(evaluation_frame, wrap=tk.WORD, height=30, width=40)
    explanation_text.grid(row=row, column=1, padx=10, pady=(0, 10))
    row += 1
    for label in evaluation_labels:
        label_widget = Label(evaluation_frame, text=label)
        label_widget.grid(row=row, column=0, padx=40, pady=(0, 10))
        entry_widget = Entry(evaluation_frame)
        entry_widget.grid(row=row, column=1, padx=10, pady=(0, 10))
        row += 1

    # Create a scrollable text box for explanation
    

    # Entry widgets for marks
    marks_entry = Entry(evaluation_frame)

    # Create Next and Submit buttons
    next_button = tk.Button(root, text="Next")
    next_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    submit_button = tk.Button(root, text="Submit", command=evaluate_answer)
    submit_button.grid(row=1, column=4, padx=10, pady=10, sticky="e")

    root.mainloop()

if __name__ == "__main__":
    create_gui()