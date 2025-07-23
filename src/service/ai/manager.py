import json
from openai import OpenAI

from config import SystemPrompts

class AI:
    _ai_client: OpenAI
    
    def __init__(self, base_url: str):
        self._ai_client = OpenAI(
            base_url=base_url,
            api_key="not-needed"
        )
    def _make_request(self, prompt: str, system_prompt: str | None = None):
        try:
            messages=[
                {"role": "user", "content": f"/no-think {prompt}"},
            ]
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
                
            response = self._ai_client.chat.completions.create(
                model="qwen/qwen3-4b",
                messages=messages
            )
            answer = response.choices[0].message.content
            answer = (answer
                    .replace("<think>", "")
                    .replace("</think>", "")
                    .strip()
                    )
            return answer
        except Exception as e:
            print("Ошибка при генерации ответа:", e)

    def get_kino_name(self, type: str, text: str):
        resp = self._make_request(
            prompt=json.loads(f'{{"type": "{type}", "text": "{text}"}}'),
            system_prompt=SystemPrompts.EXTRACT_KINO_NAME.value
        )
        return resp