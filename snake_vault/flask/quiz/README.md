<!-- --------------------------------------------------------------------| INFO {{{

# [/Snake-Vault/snake_vault/flask/quiz/README.md]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-03 19:23:14 UTC
# updated       : 2026-06-03 19:23:14 UTC
# description   : SnakeQuiz README
}}} -->

# Snake-Quiz

Snake-Quiz is a lightweight Flask extension that provides a multiple-choice quiz system based on Markdown files.

Questionnaires are stored as simple `.md` files, making it easy for non-developers to create and maintain quizzes without touching Python code.

## Features

* Flask extension
* Markdown-based questionnaires
* Multiple-choice questions
* Automatic score calculation
* Answer explanations
* Bootstrap-friendly templates
* Custom Markdown template filter
* Easy integration into existing Flask applications

---

## Installation

For now, Snake-Quiz is part of Snake-Vault

```bash
pip install snake-vault
```

Or install from source:

```bash
git clone https://github.com/fantomH/Snake-Vault.git
cd Snake-Vault
pip install .
```

---

## Quick Start

### Application Setup

```python
from flask import Flask
from snake_vault.flask.quiz import SnakeQuiz

app = Flask(__name__)

SnakeQuiz(app)
```

The quiz blueprint will automatically be registered at:

```text
/quiz/
```

---

## Configuration

### Default Questionnaire Directory

By default, SnakeQuiz looks for questionnaire files in:

```text
snake_vault/flask/quiz/quiz/
```

### Custom Questionnaire Directory

You can specify your own directory:

```python
from pathlib import Path

app.config["SNAKE_QUIZ_DIR"] = Path("/path/to/questionnaires")

SnakeQuiz(app)
```

Example:

```python
app.config["SNAKE_QUIZ_DIR"] = "./questionnaires"
```

---

## Routes

### List Questionnaires

```text
GET /quiz/
```

Displays all available questionnaires.

---

### Take a Quiz

```text
GET /quiz/<quiz_name>/
```

Displays the selected questionnaire.

Example:

```text
/quiz/python-basics/
```

---

### Submit a Quiz

```text
POST /quiz/<quiz_name>/
```

Calculates:

* Total score
* Correct answers
* Incorrect answers
* Explanations

---

## Questionnaire Format

Questionnaires are written in Markdown.

Example:

```markdown
# Python Basics

---

## Question

What keyword defines a function in Python?

### Choices

- class
- function
- def
- lambda

### Answer

def

### Explanation

The `def` keyword is used to define a function.

---

## Question

What data type is returned by `len()`?

### Choices

- str
- bool
- int
- float

### Answer

int

### Explanation

The `len()` function returns an integer.
```

---

## Directory Structure

```text
quiz/
├── python-basics.md
├── linux-basics.md
└── flask-intro.md
```

---

## Markdown Filter

SnakeQuiz automatically registers a Jinja filter named:

```jinja2
{{ text|markdown }}
```

Supported extensions:

* fenced_code
* tables

Example:

```jinja2
<div>
    {{ explanation|markdown|safe }}
</div>
```

---

## Example Application

```python
from flask import Flask
from snake_vault.flask.quiz import SnakeQuiz

app = Flask(__name__)

app.config["SNAKE_QUIZ_DIR"] = "./questionnaires"

SnakeQuiz(app)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Result Page Data

The result template receives:

```python
questionnaire
results
score
total
```

Each result contains:

```python
{
    "question": "...",
    "choices": [...],
    "answer": "...",
    "user_answer": "...",
    "is_correct": True,
    "explanation": "..."
}
```

## Display Language Support

By default, the generic display language used by SnakeQuiz templates is English.

This includes:
- Page titles (H1)
- Buttons
- Result messages and comments
- Other built-in interface elements

The questionnaire content itself is not translated by SnakeQuiz and will be displayed in the language in which the Markdown files are written.

SnakeQuiz integrates seamlessly with SnakeLinguae, a Flask extension that provides dynamic multi-language support for Flask applications.

### Example

The following example demonstrates how to use SnakeQuiz together with SnakeLinguae:

```python
from flask import Flask
from snake_vault.flask.quiz import SnakeQuiz
from snake_vault.flask.linguae import SnakeLinguae

linguae = SnakeLinguae()
quiz = SnakeQuiz()

def create_app():
    app = Flask(__name__)

    app.config["SNAKE_QUIZ_DIR"] = "./questionnaires"
    app.config["DEFAULT_LANGUAGE"] = "french"

    linguae.init_app(app)
    linguae.register_package("snake_vault.flask.quiz.linguae")

    quiz.init_app(app)

    return app
```

In this example, all SnakeQuiz interface elements will be displayed in French, while the questionnaire content will remain in the language used in the Markdown files.
