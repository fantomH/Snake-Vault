# [+] -------------------------------------------------------------------| INFO
# [/home/ghost/main/Snake-Vault/snake_vault/flask/quiz/routes.py]
# author        : Pascal Malouin (https://github.com/fantomH)
# created       : 2026-06-02 18:54:15 UTC
# updated       : 2026-06-03 16:33:32 UTC
# description   : SnakeQuiz blueprints

from flask import Blueprint
from flask import current_app
from flask import render_template
from flask import request

from .quiz_parser import list_questionnaires
from .quiz_parser import parse_questionnaire
from .utils import get_language_dictionary

quiz_bp = Blueprint(
    "quiz_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/quiz",
)

@quiz_bp.route("/")
def index():
    questionnaires = list_questionnaires()

    display_language = get_language_dictionary()

    return render_template(
        "snake_quiz/index.html",
        title="Quiz",
        display_language=display_language,
        questionnaires=questionnaires,
    )

@quiz_bp.route("/<name>/", methods=["GET", "POST"])
def take_quiz(name):
    questionnaire = parse_questionnaire(name)

    display_language = get_language_dictionary()

    if request.method == "POST":
        results = []
        score = 0

        for index, question in enumerate(questionnaire["questions"]):
            user_answer = request.form.get(f"question_{index}")
            is_correct = user_answer == question["answer"]

            if is_correct:
                score += 1

            results.append({
                **question,
                "user_answer": user_answer,
                "is_correct": is_correct,
            })

        total = len(questionnaire["questions"])

        return render_template(
            "snake_quiz/result.html",
            title="Quiz",
            questionnaire=questionnaire,
            display_language=display_language,
            results=results,
            score=score,
            total=total,
        )

    return render_template(
        "snake_quiz/take.html",
        title="Quiz",
        display_language=display_language,
        questionnaire=questionnaire,
    )
