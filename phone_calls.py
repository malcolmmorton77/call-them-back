from twilio.rest import TwilioRestClient
import tokensconfig as tcfg

# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = tcfg.from_phone

# list of one or more phone numbers to dial, in "+19732644210" format
# for now, I have verified my own number for testing, but if you want to make calls,
# purchase a number for $1.15 a month
DIAL_NUMBERS = [tcfg.to_phone]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient(tcfg.acct_sid, tcfg.acct_token)


def dial_numbers(numbers_list):
  print("Dials one or more phone numbers from a Twilio phone number.")
  for number in numbers_list:
    print("Dialing " + number)
    # set the method to "GET" from default POST because Amazon S3 only
    # serves GET requests on files. Typically POST would be used for apps
    client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

## testing texting for messages
def text_numbers(numbers_list):
  print("Texts one or more phone numbers from the Twilio phone number.")
  for number in numbers_list:
    print("Texting " + number)
    client.text.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

if __name__ == "__main__":
  dial_numbers(DIAL_NUMBERS) 