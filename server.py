#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import fifa_data
import os 
import fifa_chat


app = Flask(__name__)
ACCESS_TOKEN = 'EAAGaNy0In3ABAATIVXtDocMPXvhOj4St3XsOoNBGpJZB7ourKAFXPZBvDy9RBzBNJJZAGcPnjQQtxxzyiRGKzgiC0OacSoWDzdvxhKc0BtRA3TEem8L7qCpQbZCRAuwkHf1ZCHUV9DpEsAHk8SSu46zNQeTYvKQ0W4UK40h1NZBgZDZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)


#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET'])
#Before allowing people to message your bot, Facebook has implemented a verify token
# that confirms all requests that your bot receives came from Facebook.
def verify_fb_token():
    
	if request.args.get('hub.verify_token') == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Invalid verification token'


#if the request was not get, it must be POST and we can just proceed with sending a message back to user
@app.route("/", methods=['POST'])
def receive_message():
    # get whatever message a user sent the bot
	data = request.get_json()
	event = data['entry'][0]['messaging']
	for obj in event:
		tre = obj['message']['text']
        #Facebook Messenger ID for user so we know where to send response back to
		sender_id = obj['sender']['id']
		response = fifa_chat.chatbot(tre)
		send_message(sender_id,response)
	return "Message Processed"

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
	bot.send_text_message(recipient_id,response)
	return "success"

if __name__ == "__main__":
	app.run()

