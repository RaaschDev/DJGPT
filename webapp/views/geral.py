from django.shortcuts import render
from django.contrib import messages
import openai
from decouple import config
OPENAI_KEY =  config('OPENAPI_KEY')

def geral(request):
    params = {
        "view":{
            "id":"geral",
            "titulo":"Perguntas gerais"
        },
        
    }
    if request.method == "POST":
        params["code"] = request.POST["code"]
        openai.api_key = OPENAI_KEY
        openai.Model.list()
        try:
            response = openai.Completion.create(
                engine = "gpt-3.5-turbo-instruct",
                prompt = f"{params['code']}.",
                temperature = 0,
                max_tokens = 1000,
                top_p =1.0,
                frequency_penalty = 0.0,
                presence_penalty = 0.0
            )
            params["response"] = response['choices'][0]["text"].strip()
            print(response)
        except Exception as e:
            params["code"] = e


        # params["response"] = params["code"]

    return render(request, "geral.html", context=params)