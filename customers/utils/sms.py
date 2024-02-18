import requests
import json


def send_sms(mobile_number, message):
    try:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            # 'apiKey': AFRICASTALKING_API_KEY,
        }

        mobile_number = mobile_number[-9:]

        recipient_mobile_number = f'254{mobile_number}'

        data = {
            'recipient_mobile_number': recipient_mobile_number,
            'message': message,
            'sender_id': 'SasaPay'
        }

        response = requests.post(
            'https://residents.co.ke/apps/dashboard/api/v1/sms/send/',
            headers=headers,
            json=data
        )

        print(response.text)

        return True

    except requests.RequestException as e:
        print("An exception occurred:", str(e))
        return False
    except Exception as e:
        print("An exception occurred:", str(e))
        return False