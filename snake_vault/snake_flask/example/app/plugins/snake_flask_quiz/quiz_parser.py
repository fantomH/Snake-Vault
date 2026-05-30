from pathlib import Path

from flask import current_app


DEFAULT_QUESTIONNAIRE_DIR = Path(__file__).parent / "quiz"


def get_questionnaire_dir():
    configured_dir = current_app.config.get("SNAKE_QUIZ_QUESTIONNAIRE_DIR")

    if configured_dir:
        return Path(configured_dir)

    return DEFAULT_QUESTIONNAIRE_DIR


def list_questionnaires():
    questionnaire_dir = get_questionnaire_dir()

    questionnaires = []

    for file in questionnaire_dir.glob("*.md"):
        content = file.read_text(encoding="utf-8")
        first_line = content.splitlines()[0]

        questionnaires.append({
            "name": file.stem,
            "title": first_line.replace("#", "").strip(),
        })

    return questionnaires


def parse_questionnaire(name):
    questionnaire_dir = get_questionnaire_dir()
    path = questionnaire_dir / f"{name}.md"

    if not path.exists():
        raise FileNotFoundError(f"Questionnaire not found: {name}")

    content = path.read_text(encoding="utf-8")
    parts = content.split("---")

    title = parts[0].strip().replace("#", "").strip()

    questions = []

    for block in parts[1:]:
        block = block.strip()

        if not block:
            continue

        question = extract_section(block, "## Question", "### Choices")
        choices_raw = extract_section(block, "### Choices", "### Answer")
        answer = extract_section(block, "### Answer", "### Explanation")
        explanation = extract_section(block, "### Explanation")

        choices = [
            line.strip()[2:].strip()
            for line in choices_raw.splitlines()
            if line.strip().startswith("- ")
        ]

        questions.append({
            "question": question,
            "choices": choices,
            "answer": answer,
            "explanation": explanation,
        })

    return {
        "name": name,
        "title": title,
        "questions": questions,
    }


def extract_section(text, start_marker, end_marker=None):
    start = text.find(start_marker)

    if start == -1:
        return ""

    start += len(start_marker)

    if end_marker is None:
        return text[start:].strip()

    end = text.find(end_marker, start)

    if end == -1:
        return text[start:].strip()

    return text[start:end].strip()
