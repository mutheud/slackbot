import os
# Use the package we installed
from slack_bolt import App
import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)


def send_slack_message(channel, blocks):
    return client.chat_postMessage(
        channel=channel,
        blocks=blocks

    )
# import pdb;pdb.set_trace()
def read_messages():
    response=client.conversations_open(
        users=["U03GPQR5UBU","U03GPQR5UBU"]
    )

    return response

# def send_slack_info(channel,blocks,user):
#     return client.chat_postEphemeral(
#         channel=channel,
#         blocks=blocks,
#         user = user
#     )




# ID of channel you want to post message to
user= 'U03GPQR5UBU'
channel ='C03HDKLB6KA'
blocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"
        }
    }
]
# message = "How are you?"


try:
    response = send_slack_message(channel, blocks)


except SlackApiError as e:
    print(f"Error: {e}")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3001)))
