from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

VERIFY_TOKEN = "rexy_webhook_2024"

@csrf_exempt
def whatsapp_webhook(request):

    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)

        return HttpResponse("Token inválido", status=403)

    # Recebimento das mensagens
    if request.method == "POST":
        data = json.loads(request.body)

        print("Webhook recebido:")
        print(json.dumps(data, indent=2))

        return JsonResponse({"status": "ok"})