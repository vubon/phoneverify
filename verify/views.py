# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from twilio.rest import Client

# Create your views here.


def index(request):
    return render(request, 'index.html')


def test(request):
    # put your own credentials here
    account_sid = "ACb1198191b353896cd4cedfe0bee18788"
    auth_token = "426fe34ea601d9c9a169679d44b0dc16"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+8801737388296",
        from_="+15005550006",
        body="Tomorrow's forecast in Financial District, San Francisco is Clear",
        media_url="https://climacons.herokuapp.com/clear.png")

    print('Message Sent', message.sid)

    return render(request, 'test.html')
