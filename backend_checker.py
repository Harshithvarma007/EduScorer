import openai

def check_answer(Teachers_solution, Students_answer, Max_marks, Question):
    openai.api_key = "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"
    # openai.api_key = api_key_input
    # try:
    print("sending to gpt3")
    completion1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        
           
# code without the red highlight
        # messages=[{"role": "user", "content":f'''Please evaluate the student's answer for the following question. You will be provided with the teacher's solution, the question, the student's answer, and the maximum marks. Your task is to assign a score to the student's answer.

        # Teacher's Solution: {Teachers_solution}
        # Question: {Question}
        # Student's Answer: {Students_answer}
        # Max Marks: {Max_marks}

        # You must be strict in your evaluation. Give full marks only if the student's answer matches the teacher's solution exactly. You may provide partial marks for answers that contain correct information but are outside the scope of the teacher's solution. You can allocate marks in whole numbers or in increments of 0.5 
        # you should cut marks for whatever reasons you can ( like less content take the teachers answer as the ideal length for the answer )
        # '''
        # },
        # # {"role": "user", "content":f''' Teachers_solution ""{Teachers_solution}""  Students_answer- {Students_answer} Max_marks- {Max_marks} Question- {Question}'''},
        
        # ],
       messages = [
    {
        "role": "system",
        "content": "You are a strict teacher evaluating student answers.",
    },
    {
        "role": "user",
        "content": f'''Please evaluate the student's answer for the following question. You will be provided with the teacher's solution, the question, the student's answer, and the maximum marks. Your task is to assign a score to the student's answer.

**Teacher's Solution:**
{Teachers_solution}

**Question:**
{Question}

**Student's Answer:**
{Students_answer}

**Max Marks:**
{Max_marks}

**Evaluation Criteria:**
- Accuracy: Compare the student's answer to the teacher's solution. Deduct 0.5 marks for each factual inaccuracy.
- Completeness: Consider the depth of coverage in the student's answer. Deduct 0.5 marks for each missing key point.
- Relevance: Assess if the student's answer stays on-topic. Deduct 0.5 marks for each irrelevant point.
- Clarity: Evaluate the clarity and organization of the student's response. Deduct 0.5 marks for incoherent or poorly structured answers.

**Marks Allocation:**
- Full Marks: Give full marks (as specified) for answers that match the teacher's solution exactly(context and accuracy wise).
- Partial Marks: Deduct 1 marks for any discrepancies between the student's answer and the teacher's solution, applying a clear grading scale.
- Length: If the student's answer is significantly shorter or longer than the teacher's solution, adjust the marks accordingly according to the content.(too short -3 marks ,short -2 marks, little short -1 marks)
- Explaination: If the student's answer doesnt contain the explaination of the answer that is there in the teachers answer deduct 0.5 marks.
You should consider all evaluation criteria and allocate marks based on the provided guidelines and just return the total marks allocated out of max marks.
'''
    }
],

# Your code to interact with the model here

        temperature=0.1,
        # max_tokens=15000,
    )
        
    final_html = completion1['choices'][0]['message']['content']

    return final_html

question="Describe the causes and consequences of the Industrial Revolution in the 19th century."
print( check_answer(open('teachers_solution.txt', 'r').read(),open('students_answer.txt','r').read(), 10, question))