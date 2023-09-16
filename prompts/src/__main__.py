import json
from .sustainability_profile import create_user_profile

if __name__ == "__main__":
    answers= []
    with open("test_data/selected_answers.jsonl", "r") as infile:
        for l in infile:
            answers.append(json.loads(l))

    profile= create_user_profile(answers)
    print(profile)
