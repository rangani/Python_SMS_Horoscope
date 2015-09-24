import requests
import horoscope as hs

zsigns = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
print ("Zodiac Signs: ", zsigns)

number = input('Enter the phone number: ')
sign = input('Enter the sign: ')

predictions = hs.horoscope()

for zsign, message in predictions.items():
   message = zsign + ": " + message
   if str(zsign) == str(sign):
      payload = {'number': number, 'message': message}

print('payload:', payload)
r = requests.post("http://textbelt.com/text", data=payload)
if r.json()['success']:
    print('Success!')
else:
    print('Error!')
