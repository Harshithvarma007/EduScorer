

import pymysql

def enter_answer_data(question_id, student_id, teacher_id, answer_text, solution, explanation, marks, accuracy, completeness, length, relevance, clarity, evaluation_comment):
    try:
        db_config = {
            'user': 'root',   # Replace with your MySQL username
            'password': 'puts186PK@321332',  # Replace with your MySQL password
            'host': 'localhost',
            'database': 'evaluation_db',
        }
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the answers table
        insert_query = """
            INSERT INTO answers (question_id, student_id, teacher_id, answer_text, solution, explanation, marks, accuracy, completeness, length, relevance, clarity, evaluation_comment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (question_id, student_id, teacher_id, answer_text, solution, explanation, marks, accuracy, completeness, length, relevance, clarity, evaluation_comment)

        cursor.execute(insert_query, data)

        conn.commit()
        print("Data inserted successfully!")

    except pymysql.Error as error:
        print(f"Error: {error}")

    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Example usage
enter_answer_data(
    question_id=1,
    student_id=1,
    teacher_id=1,
    answer_text="This is the student's answer.",
    solution="The correct solution.",
    explanation="Explanation of the answer.",
    marks=8,
    accuracy=0.9,
    completeness=0.8,
    length=,
    relevance=0.9,
    clarity=0.85,
    evaluation_comment="Well done!"
)

