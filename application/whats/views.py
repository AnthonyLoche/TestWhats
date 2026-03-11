from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

VERIFY_TOKEN = "EAANO0hU2hPUBQZCY6829CrckyRF4AYEAawYpVCoXmL3wg6sX8QcULZAtdGlgzHZCouKLNGivDf9IZAUpwWloqcs4ZAandgasQKnbeSgDSxDYod46op4AMy5fc4RH3o4ZAyvBuvMtjZA6lSA6FKenjmGNKRDUW1CJ6qknvvK72R9I4TZCXyNPCIx9ZCDlpIvV9DoJ6KZBGuIXU2mtEROIQLtgRoGu137OcG2VG19k745hQADof6H7ic5pCNUZCmx1r63icahPpOu4lrJF97odVxtCIsX"

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