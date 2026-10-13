
import time
from django.conf import settings
from google import genai
from google.genai import errors


def generate(prompt: str) -> str:
    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=(
                    "Crie uma descrição comercial do carro em até "
                    "500 caracteres. Não invente informações. "
                    "Retorne apenas a descrição.\n\n"
                    f"Carro: {prompt}"
                ),
                config={
                    "max_output_tokens": 500,
                    "temperature": 0.4,
                },
            )

            description = (response.text or "").strip()

            if not description:
                raise ValueError("O Gemini retornou uma descrição vazia.")

            return description[:500]

        except errors.ServerError:
            if attempt == 2:
                raise

            time.sleep(2 ** attempt)

    raise RuntimeError("Não foi possível gerar a descrição.")