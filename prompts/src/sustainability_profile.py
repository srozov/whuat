import openai, json, os

from prompts.src.prompts import UserProfilePrompt

openai.api_key = os.getenv("OPENAI_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

profile_prompt= UserProfilePrompt()

def create_user_profile(personal_answers):
    try:
        # send the API request
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages = profile_prompt.messages(),
        )
    except Exception as e:
        print("Couldn't make OpenAI request " + e)

    try:
        response = json.loads(completion.choices[0].message.content)
        if not response or isinstance(response, bool):
            raise ValueError("Empty document", "", 0)
    except ValueError as err:
        print("Couldn't parse OpenAI response as JSON " + "err" +completion.choices[0].message.content)
    except Exception as err:
        print("Couldn't parse OpenAI response " + err)

    return response

if __name__ == "__main__":
    answers= []
    with open("prompts/selected_answers.jsonl", "r") as infile:
        for l in infile:
            answers.append(json.loads(l))

    profile= create_user_profile(answers)
    print(profile)