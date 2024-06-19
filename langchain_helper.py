from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from secretapikey import openai_api_key
import os

os.environ["OPENAI_API_KEY"] = openai_api_key


def get_restaurant_name_and_items(cuisine):
    # Initialize the LLM with desired parameters
    llm = OpenAI(temperature=0.7)

    # Define the prompt template for generating restaurant names
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Recommend a fancy name for this."
    )

    # Define the name chain
    name_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_name,
        output_key='restaurant_name'
    )

    # Define the prompt template for generating menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Recommend 15 menu items for {restaurant_name}"
    )

    # Define the food items chain
    food_items_chain = LLMChain(
        llm=llm,
        prompt=prompt_template_items,
        output_key='menu_items'
    )

    # Define the SequentialChain with correct input and output handling
    sequential_chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Provide the initial input and run the chain
    result = sequential_chain({'cuisine': cuisine})

    return result


if __name__ == "__main__":
    print(get_restaurant_name_and_items("Italian"))


