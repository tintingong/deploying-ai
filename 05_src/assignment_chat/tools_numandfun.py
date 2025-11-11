from langchain.tools import tool
import json
import requests


@tool
def get_num_facts(n:int=1):
    """
    Returns n random number facts from the Number  API.
    """
    url = "http://numbersapi.com/random/math?json"
    params = {
        "count": n
    }
    response = requests.get(url, params=params)
    resp_dict = json.loads(response.text)
    facts_list = resp_dict.get("data", [])
    facts = "\n".join([f"{i+1}. {fact}\n" for i, fact in enumerate(facts_list)])
    return facts

@tool
def get_fun_facts(n:int=1):
    """
    Returns n fun facts from the fun facts API.
    """
    url = "interesting-facts-api.p.rapidapi.com"
    params = {
        "limit": n
    }
    response = requests.get(url, params=params)
    resp_dict = json.loads(response.text)
    facts_list = resp_dict.get("data", [])
    facts = "\n".join([f"{i+1}. {fact['attributes']['body']}\n" for i, fact in enumerate(facts_list)])
    return facts
