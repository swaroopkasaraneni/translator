from langchain.chat_models import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage
from openai.error import RateLimitError

import os
from CustomError import CustomError
from dotenv import load_dotenv

load_dotenv()

openAILLM = ChatOpenAI(model_name='gpt-3.5-turbo',openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.4, max_tokens=100)
def executeOpenAI(lang1, lang2, text):
    try:
        prompt = f"Translate the given text in {lang1} to {lang2}"
        text_content = text
        sys_prompt = [SystemMessage(content=prompt), HumanMessage(content=text_content)]
        output = openAILLM(sys_prompt).content
        if output:
            return output
    except Exception:
        print("Rate limit exceeded. Please try again later.")
        raise CustomError("OpenAi Licience expired")
