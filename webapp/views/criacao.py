from django.shortcuts import render
from django.contrib import messages
import openai
from decouple import config
OPENAI_KEY =  config('OPENAPI_KEY')
linguagens = ['c',
 'clike',
 'cpp',
 'csharp',
 'css',
 'csv',
 'dart',
 'django',
 'docker',
 'go',
 'graphql',
 'java',
 'javascript',
 'kotlin',
 'makefile',
 'markdown',
 'markup',
 'markup-templating',
 'mongodb',
 'php',
 'python',
 'ruby',
 'rust',
 'scala',
 'sql',
 'swift',
 'xml-doc',
 'yaml'
 ]

def criacao(request):
    params = {
        "view":{
            "id":"criacao",
            "titulo":"Criação de código"
        },
        "linguagens":linguagens
    }
    if request.method == "POST":
        params["code"] = request.POST["code"]
        params["linguagem"] = request.POST["linguagem"]
        if params["linguagem"] == 'Selecione uma linguagem':
            messages.success(request, "Por favor selecione uma linguagem")
            return render(request, "criação.html", context=params)
        openai.api_key = OPENAI_KEY
        openai.Model.list()
        try:
            response = openai.Completion.create(
                engine = "gpt-3.5-turbo-instruct",
                prompt = f"Respond only with code. code:{params['code']} in {params['linguagem']}.",
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

    return render(request, "criacao.html", context=params)