# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyBxUGqEvrIxL0-5-wzfhr2EjmHXdQe3vcA")


registration_id = "fOh4ofj-C8E:APA91bGcQgikWmNEDc3N8qVnHyBPCTVjdmQA4HSEW_R7yuuirD97JS2_37CivZv2_8cPVFYKEqg-4B_Y5drPRsO4IXbIVLfqxW4MpJXDyE89KE1WTUUPMzzW5_I0fEDySQM5R0TsaWF8"
message_title = "Innbrudd"
message_body = "Bevegelse oppdaget"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


print result
