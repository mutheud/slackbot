
import os
from app import *
# from .libs.slack_api import SlackClient
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack_sdk import WebClient
import json
from datetime import datetime

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    os.environ.get('SIGNING_SECRET'), '/slack/events', app)
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
token = '1IRRHY820u7lLQM0LddpbuN3'
# channel = 'C03HDKLB6KA'
event ={}


class SlackClient:

    def __init__(self,event,token,channel,user,day):
        self.event = event
        self.token = token
        self.channel = channel
        self.user = user
        self.day = day

    @slack_event_adapter.on("app_mention")
    def listen_for_commands(event):
        def command_hello(event):
        # import ipdb;ipdb.set_trace()
            channel = event['event']['channel']
            client.chat_postMessage(
                channel=channel,
                text="Hello :wave: "
            )

        def local_time(event):
            day = event['event']['ts']
            channel = event['event']['channel']
            dt_time = int(float(day))
            # import ipdb; ipdb.set_trace()
            dt = datetime.fromtimestamp(dt_time)
            dat = dt.strftime("%m/%d/%Y, %H:%M:%S")

            client.chat_postMessage(
                channel=channel,
                text = dat
            )
        text = event['event']['text']
        txt = text.lower
        if txt == 'Hello' or 'hey':
            return command_hello(event) + local_time(event)


    @slack_event_adapter.on("app_mention")
    def command_comment(event):

        channel = event['event']['channel']
        ts = event['event']['ts']
        client.chat_postMessage(
            channel=channel,
            thread_ts= ts,
            text = "Hello again :wave:"
        )



    @slack_event_adapter.on("app_mention")
    def command_show_comment(event):
        channel = event['event']['channel']
        ts = event['event']['ts']
        client.conversations_replies(
            channel=channel,
            thread_ts= ts,
        )


if __name__ == "__main__":
    app.run(debug=True)
    # SlackClient().event_test()
