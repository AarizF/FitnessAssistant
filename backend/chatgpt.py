from openai import OpenAI
import os

def get_api_key():
    try:
        with open(os.path.expanduser("~/Developer/gpt key.txt"), "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise ValueError("API key file not found at ~/Developer/gpt key.txt")

def get_chatgpt_response(data):
    name = data['name']
    age = data['age']
    sex = data['sex']
    height = data['height']
    current_weight = data['currentWeight']
    target_weight = data['targetWeight']

    api_key = get_api_key()
    client = OpenAI(api_key=api_key)

    content = f"You are a highly experienced fitness trainer with expertise in nutrition and weight loss. Your client is a {age} year old {sex}, {height} cm and weighs {current_weight} kg. They want to lose weight and reach {target_weight} kg. They are looking for a diet plan  and an exercise routine that will help them achieve their goal. Give them a meal plan for every day of the week including how many calories they should consume per meal as well as an exercise routine to help the maintain muscle. Break down the exercise routine by days of the week and include the number of sets and reps for each exercise."

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )

    #print(response.choices[0].message.content)
    return response.choices[0].message.content