from langchain.chat_models import ChatOpenAI, GooglePalm
from langchain.schema import SystemMessage, HumanMessage
from openai.error import RateLimitError
import os
from CustomError import CustomError

openAILLM = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.4, max_tokens=100)
def executeOpenAI(lang1, lang2, text):
    try:
        prompt = f"Translate the given text in {lang1} to {lang2}"
        text_content = text
        sys_prompt = [SystemMessage(content=prompt), HumanMessage(content=text_content)]
        output = openAILLM(sys_prompt).content
        if output:
            return output
    except RateLimitError:
        print("Rate limit exceeded. Please try again later.")
        raise CustomError("Licience expired")

print(os.getenv("GOOGLE_API_KEY"))
googlePalmLLM = GooglePalm(google_api_key=os.getenv["GOOGLE_API_KEY"], temperature=0.1)
def executeGooglePalm(lang1, lang2, text):
    try:
        prompt = f"Translate the given text in {lang1} to {lang2}"
        sys_prompt = [SystemMessage(content=prompt), HumanMessage(content=text)]
        output = googlePalmLLM(sys_prompt).content
        return output
    except RateLimitError:
        print("Rate limit exceeded. Please try again later.")
        raise CustomError("Licience expired")