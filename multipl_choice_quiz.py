from question import Question

question_prompts = [
    "what color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Pink\n(b) Yellow\n(c) Red\n",
    "what color are grape?\n(a) Pink\n(b) Green/black\n(c) Red\n"

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions) + "correct"))

run_test(questions)