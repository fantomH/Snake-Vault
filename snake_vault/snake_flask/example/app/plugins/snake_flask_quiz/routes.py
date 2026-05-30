from flask import Blueprint, render_template, request

from .quiz_parser import list_questionnaires, parse_questionnaire


snake_flask_quiz = Blueprint(
    "snake_flask_quiz",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/quiz",
)


@snake_flask_quiz.route("/")
def index():
    questionnaires = list_questionnaires()

    return render_template(
        "snake_flask_quiz/index.html",
        questionnaires=questionnaires,
    )


@snake_flask_quiz.route("/<name>/", methods=["GET", "POST"])
def take_quiz(name):
    questionnaire = parse_questionnaire(name)

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
            "snake_flask_quiz/result.html",
            questionnaire=questionnaire,
            results=results,
            score=score,
            total=total,
        )

    return render_template(
        "snake_flask_quiz/take.html",
        questionnaire=questionnaire,
    )
