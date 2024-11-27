
from imports import *

class OpenAIChatBot:
    """Class to interface with the OpenAI chatbot"""

    def __init__(self):
        # Load API key
        with open("files/API/jarvis_api_key.txt", 'r') as f:
            self.api_key = f.read().strip()
        self.client = openai.OpenAI(api_key = self.api_key)
        self.pl: list[str] = [ "You will pretend to be the AI assistant to Tony stark. Address me by 'sir' please."]


    
    # Define the function
    def _get_api_response(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are JARVIS, a highly intelligent AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.99,
                max_tokens=100,
                top_p = 1,
                frequency_penalty=0.4,
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

    def _update_list(self, message: str, pl: list[str]) -> list[str]:
        self.pl.append(message)

    def _create_prompt(self, message: str, pl: list[str]) -> str:
        p_message: str = f'\nYou: {message}'
        self._update_list(p_message, pl)
        prompt: str = ''.join(pl)
        return prompt

    def get_bot_response(self, message: str, pl: list[str]) -> str:
        prompt: str = self._create_prompt(message, pl)
        bot_response: str = self._get_api_response(prompt)
        if bot_response:
            self._update_list(bot_response, pl)
            return bot_response
        else:
            bot_response = "Something went wrong..."
        return bot_response

