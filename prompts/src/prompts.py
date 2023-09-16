class UserProfilePrompt:
    def __init__(self):
        self.chat_context= "You are a helpful writing assistant."
        self.prompt = """
            > Instructions

            - Speak a bit like a gen Z influencer. *Make it fun, but stay polite!*
            - Speak directly to me, for example: "Hey there! With your conscious choices you're making one more step to save our world!".
            - Feel free to invent a funny name for me that make sense given the profile that you will make for me -- but make sure that I won't be offended with the name. For example, a guy that always takes care to avoid plastic when shopping, because he cares a lot about the environment, but still drives a car to work instead of using a bike, might be called "Eco-Eddie with a Dash of Diesel". If the name sounds too "made up", skip it -- it's not necessary!
            - My multiple-choice questions and answers are given in this JSON format. The answer I picked is called `selected_answer`, the other 3 that I rejected are the `alternatives`. The themes characterize the question.
            ```
            {"question": "Cool party trick: Using organic paper plates or washing up afterwards?", "selected_answer": "Washing up FTW", "alternatives": ["Organic plates, pls", "Mix it up", "Depends on the party"], "themes": ["Organic products", "Waste reduction", "Avoiding disposable items"]}
            ```
            - Produce my profile in the following JSON format: `{"scores": {"theme_1": score, "theme_2": score}, "profile": "..."}`

            Your task is to create a short profile for me. For each question, look at the themes as if they are character traits. What do my choices tell you about me in terms of each theme? Most of the themes can be seen as an axis from "don't care" to "very important". How high do I score on each of these axes? Repeat this process for every question. Finally, produce an average score for every theme that has at least 5 answers.

            With this analysis, can you now produce an overall character profile about me, that relies heavily on my scores for each theme, but also fleshes it out with a cute background story? Think like a Buzzfeed quiz result.
            Write the score only for the *top 5* themes, that have enough answers and are different enough from each other. Then write a short paragraph max 50 words with the profile.

            > Let's try a short example

            Answers:

            ```
            {"question": "Packing for a picnic - is it disposable plates or reusable dishes?", "selected_answer": "Disposable plates", "alternatives": ["Reusable dishes", "A mix", "No picnic here"], "themes": ["Packaging", "Avoiding disposable items", "Waste reduction"]}
            {"question": "Your 'canvas' for grocery shopping is...?", "selected_answer": "A canvas bag", "alternatives": ["A plastic bag", "A mix", "Basket, please"], "themes": ["Packaging", "Reusable shopping bags", "Overconsumption avoidance"]}
            {"question": "Doing your bit for the planet with that thermostat?", "selected_answer": "Smart, auto-adjusts", "alternatives": ["Yes, energy-efficient", "No, old school", "What's a thermostat?"], "themes": ["Energy efficiency", "Green living", "Carbon footprint reduction"]}
            {"question": "Eating out or ordering in: how much packaging waste do you have?", "selected_answer": "I always cook at home", "alternatives": ["Almost none", "Loads", "Depends"], "themes": ["Packaging", "Avoiding disposable items", "Waste reduction"]}
            {"question": "Sporting some kicks: are they ethically made?", "selected_answer": "No idea", "alternatives": ["Absolutely", "Not really", "Depends on the brand"], "themes": ["Ethical consumption", "Sustainably-sourced materials", "Fair trade"]}
            {"question": "Been to any cool beach cleanups lately?", "selected_answer": "Nah, not my thing", "alternatives": ["Yes, many", "A few", "Not yet, but interested"], "themes": ["Community cooperation", "Ocean conservation", "Waste reduction"]}
            ```
        """
        self.attempt = """
            Alrighty then, here we go!
            The top 5 themes with enough answers are:
            Avoiding disposable items - Average Score: 2.3 (Points for washing up and home cooking but deducted for those disposable plates.).
            Packaging - Average Score: 2.7 (A canvas bag is good, but using disposable plates and dining in most times lessen the impact.)
            Waste reduction - Average Score: 2.3 (Well, cooking at home helps to minimize waste, but opting for disposable plates doesn't exactly shout waste reduction, nor does lack of beach cleanup participation.)
            Energy efficiency - Score: 5 (Spot on with the smart thermostat! Keep that green energy flowing!)
            Overconsumption avoidance - Score: 5 (Great choice with the canvas bag and home cooking!)

            So, here's your creative profile:
            ```
            {"scores": {"Avoiding disposable items": 2.3, "Packaging": 2.7, "Waste reduction": 2.3, "Energy efficiency": 5, "Overconsumption avoidance": 5}, "profile": "Hello 'Part-Time Green Giant'! You've got a strong grip on reducing overconsumption and improving energy efficiency. Just swap those disposable plates for some washable ones and join a beach cleanup. Soon, you'll be an unstoppable green force! Keep the good vibe going!"}
            ```
            Isn't this cool, Part-Time Green Giant?! You're making moves, just need a nudge here and there to really conquer this green game! 🌍💚
        """
        self.feedback = """
            Good job! Your reasoning is sound.
            Please don't write out your reasoning or an explanation for the real input.
            If you really want to say something more in the profile, you can squeeze it, but keep it short and sweet: aim for 50 words, but 70 words is the hard limit.
        """

    def lead(self, personal_answers):
        "Personal answers must be a list of JSON strings with the 'answer' format"
        return "```\n"+"\n".join(personal_answers)+"\n```"

    def messages(self, personal_answers):
        "Personal answers must be a list of JSON strings with the 'answer' format"
        return [
            {"role": "system", "content": self.chat_context},
            {
                "role": "user",
                "content": self.prompt,
            },
            {
                "role": "assistant",
                "content": self.attempt,
            },
            {
                "role": "user",
                "content": self.feedback + '\n' + self.lead(personal_answers),
            },
        ]