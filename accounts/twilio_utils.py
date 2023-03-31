from twilio.rest import Client
from django.conf import settings
import random

twilio_account_sid = 'ACf7964953d2169c138ac18b42bd390937'
twilio_auth_token = 'a0747748e3bc9ac65f29ea47313e61b6'
twilio_phone_number = '+15076186286'

client = Client(twilio_account_sid, twilio_auth_token)
def send_otp_sms(phone_number):
    otp = str(random.randint(1000,9999))
    message = client.messages.create(
        to = f'{phone_number}',
        from_=twilio_phone_number,
        body=f'Your OTP is {otp}.'
    )
    return message
