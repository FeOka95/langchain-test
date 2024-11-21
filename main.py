import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

number_of_days = 7
number_of_childs = 2
activity = 'beach'

prompt_model = PromptTemplate.from_template(
    "Create a travel itinerary of {number_of_days} days for a family of {number_of_childs} childs that like {activity}"
)

prompt = prompt_model.format(number_of_days=number_of_days,
                            number_of_childs=number_of_childs,
                            activity=activity)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=OPENAI_API_KEY)

response = llm.invoke(prompt)
print(response.content)