```markdown
# Quiz Game

This is a Python-based quiz game that lets users answer True/False questions from a question bank. The quiz provides real-time feedback and displays the final score once the quiz is complete.

## Features
- Loads questions from a data source.
- Displays each question one at a time.
- Accepts user input (`True` or `False`).
- Tracks the user's score and displays it at the end of the quiz.

## Project Structure

```plaintext
.
├── question_model.py    # Contains the Question class to create question objects
├── data.py              # Stores the list of question data (questions and correct answers)
├── quiz_brain.py        # Contains the QuizBrain class which controls the flow of the quiz
├── main.py              # The main file to run the quiz game
└── README.md            # This README file
```

### Files and Classes:

- `question_model.py`:
  - Contains the `Question` class which has two attributes:
    - `text`: The question text.
    - `answer`: The correct answer (True/False).
  
- `data.py`:
  - Stores the question data in a list of dictionaries, with each dictionary containing:
    - `"question"`: The question text.
    - `"correct_answer"`: The correct answer to the question.

- `quiz_brain.py`:
  - Contains the `QuizBrain` class, which handles:
    - Keeping track of which question the user is on.
    - Displaying questions and receiving user input.
    - Checking the correctness of the answer and updating the score.

- `main.py`:
  - The entry point of the quiz game, which:
    - Creates a `question_bank` from the data.
    - Initializes the `QuizBrain` with the `question_bank`.
    - Runs the quiz in a loop until all questions are answered.

## How to Run the Program

### Requirements:
- Python 3.x

### Steps to Run:
1. **Clone or Download the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure all Files are Present**:
   Make sure the following files are present in the directory:
   - `main.py`
   - `question_model.py`
   - `data.py`
   - `quiz_brain.py`

3. **Run the Program**:
   Run the main script using Python:
   ```bash
   python main.py
   ```

4. **Answer the Questions**:
   The program will ask questions in a True/False format. Type either `True` or `False` as your answer.

5. **Get Your Score**:
   Once you've answered all the questions, your final score will be displayed.

### Example Output:
```
Q1: The Earth is flat. (True/False)?
> False
Correct!

Q2: The Moon is a planet. (True/False)?
> True
Wrong!

You have completed the quiz.
Your final score was: 1/2.
```

## Customizing the Quiz

To customize the quiz, you can modify the `data.py` file. Here's an example of the format:
```python
question_data = [
    {"question": "The sky is blue.", "correct_answer": "True"},
    {"question": "Fish can walk on land.", "correct_answer": "False"},
    # Add more questions here...
]
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
```
