import openai

# Load API key
with open("../files/API/jarvis_api_key.txt", 'r') as f:
    api_key = f.read().strip()

client = openai.OpenAI(api_key = api_key)
# Define the function
def get_api_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are JARVIS, a highly intelligent AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=100,
            top_p = 1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" You:", " JARVIS:"]
        )
        # Extract the assistant's reply
        choices: dict = response.choices[0]
        text: str = choices.message.content
        #print(choices)
        #text: str = response.choices[0]['message']['content']
        return text

    except Exception as e:
        print("ERROR:", e)
        return "An error occurred."

def update_list(message: str, pl: list[str]) -> list[str]:
    pl.append(message)

def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nYou: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt

def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)
    if bot_response:
        update_list(bot_response, pl)
        return bot_response
    else:
        bot_response = "Something went wrong..."
    return bot_response

