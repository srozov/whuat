import json

questions= []
with open("prompts/questions.jsonl", "r") as qfile:
    for l in qfile:
        questions.append(json.loads(l))
choices= []
with open("prompts/choices.txt", "r") as cfile:
    for l in cfile:
        choices.append(int(l.strip()))

def answer(question, i):
    "JSON answer given a question and selected answer index"
    return {"question":question["question"],
                       "selected_answer": question["answers"][i],
                       "alternatives": question["answers"][:i] + question["answers"][i+1:],
                       "themes": question["themes"]}

with open("prompts/selected_answers.jsonl", "w") as outfile:
    for c,q in zip(choices, questions):
        json.dump(answer(q, c), outfile)
        outfile.write("\n")