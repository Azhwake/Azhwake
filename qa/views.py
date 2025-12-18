from django.shortcuts import render

QA_DATA = {
    "what is cybersecurity": "Cybersecurity is protecting systems and data from attacks.",
    "what is django": "Django is a Python web framework for fast and secure development.",
    "what is ussd": "USSD is a telecom protocol for interactive menus."
}

def home(request):
    answer = ""
    question = ""

    if request.method == "POST":
        question = request.POST.get("question", "").lower()
        answer = QA_DATA.get(question, "❌ No answer found")

    return render(request, "qa/home.html", {
        "answer": answer,
        "question": question
    })
