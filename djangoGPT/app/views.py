from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import openai
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Create your views here.
def index(request):
    return render(request,'app/index.html')    

def chat_view(request):
    input_text = request.POST.get('input_text', '')
    openai.organization = env("ORGANIZATION_OPENAI")
    openai.api_key = env("SECRET_OPENAI")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=2000
    )
    return JsonResponse({'response': response.choices[0].text})