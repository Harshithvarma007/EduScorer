import tkinter as tk
from tkinter import Text, Label, Entry,scrolledtext
from backend import check_answer
from tkinter import filedialog
import xlwt
def create_gui():
    
    def export_to_excel():
        # Get the values from the Entry widgets
        marks = marks_entry.get()
        accuracy = accuracy_entry.get()
        completeness = completeness_entry.get()
        relevance = relevance_entry.get()
        clarity = clarity_entry.get()

        # Get the explanation
        explanation = explanation_text.get("1.0", "end-1c")

        # Create a new workbook and add a worksheet
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("Results")

        # Define the column headers
        headers = ["Marks", "Accuracy", "Completeness", "Relevance", "Clarity", "Explanation"]

        # Write the headers to the worksheet
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        # Write the data to the worksheet
        data = [marks, accuracy, completeness, relevance, clarity, explanation]
        for col, value in enumerate(data):
            worksheet.write(1, col, value)

        # Save the Excel file
        workbook.save("evaluation_results.xls")

        print("Data exported to evaluation_results.xls")
    def clear_evaluation_entries():
        # Clear the Entry widgets
        explanation_text.delete("1.0", "end")
        marks_entry.delete(0, "end")
        accuracy_entry.delete(0, "end")
        completeness_entry.delete(0, "end")
        relevance_entry.delete(0, "end")
        clarity_entry.delete(0, "end")

    def evaluate_answer():
        teacher_solution = teacher_solution_text.get("1.0", "end-1c")
        student_answer = student_answer_text.get("1.0", "end-1c")
        max_marks = 10 
        question = "Describe the causes and consequences of the Industrial Revolution in the 19th century."

        result = check_answer(teacher_solution, student_answer, max_marks, question)

        
        result_dict = eval(result)
        marks = result_dict.get("marks")
        explanation = result_dict.get("explaination")  

    
        marks_entry.delete(0, "end")
        marks_entry.insert(0, marks)

        explanation_text.delete("1.0", "end")
        explanation_text.insert("1.0", str(explanation))

        
        accuracy_entry.delete(0, "end")
        accuracy_entry.insert(0, result_dict.get("accuracy"))

        completeness_entry.delete(0, "end")
        completeness_entry.insert(0, result_dict.get("completeness"))

        relevance_entry.delete(0, "end")
        relevance_entry.insert(0, result_dict.get("relevance"))

        clarity_entry.delete(0, "end")
        clarity_entry.insert(0, result_dict.get("clarity"))


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
    
    
    row = 0
    explanation_label = Label(evaluation_frame, text="Explanation:")
    explanation_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    
    explanation_text = Text(evaluation_frame, wrap=tk.WORD, height=30, width=40)
    explanation_text.grid(row=row, column=1, padx=10, pady=(0, 10))

    row += 1
    
    marks_label = Label(evaluation_frame, text="Marks:")
    marks_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    marks_entry = Entry(evaluation_frame,width=50)
    marks_entry.grid(row=row, column=1, padx=10, pady=(0, 10))
    row += 1

    
    accuracy_label = Label(evaluation_frame, text="Accuracy:")
    accuracy_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    accuracy_entry = Entry(evaluation_frame,width=50)
    accuracy_entry.grid(row=row, column=1, padx=10, pady=(0, 10))
    row += 1

    completeness_label = Label(evaluation_frame, text="Completeness:")
    completeness_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    completeness_entry = Entry(evaluation_frame,width=50)
    completeness_entry.grid(row=row, column=1, padx=10, pady=(0, 10))
    row += 1

    relevance_label = Label(evaluation_frame, text="Relevance:")
    relevance_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    relevance_entry = Entry(evaluation_frame,width=50)
    relevance_entry.grid(row=row, column=1, padx=10, pady=(0, 10))
    row += 1

    clarity_label = Label(evaluation_frame, text="Clarity:")
    clarity_label.grid(row=row, column=0, padx=40, pady=(0, 10))
    clarity_entry = Entry(evaluation_frame,width=50)
    clarity_entry.grid(row=row, column=1, padx=10, pady=(0, 10))



    next_button = tk.Button(root, text="Next")
    next_button.grid(row=2, column=0, padx=10, pady=10, sticky="sw")  
    clear_button = tk.Button(root, text="Clear", command=clear_evaluation_entries)
    clear_button.grid(row=2, column=2, padx=10, pady=10, sticky="se")  

    check_button = tk.Button(root, text="Check", command=evaluate_answer)
    check_button.grid(row=2, column=3, padx=15, pady=10, sticky="sw")  

    submit_button = tk.Button(root, text="Submit",command=export_to_excel)
    submit_button.grid(row=2, column=4, padx=10, pady=10, sticky="se")  


    # Use a filler frame to occupy the central space
    filler_frame = tk.Frame(root)
    filler_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
    filler_frame.grid_columnconfigure(0, weight=1)

    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=2)
    root.grid_columnconfigure(4, weight=1)

    
    root.grid_rowconfigure(2, weight=1)


    root.mainloop()

if __name__ == "__main__":
    create_gui()