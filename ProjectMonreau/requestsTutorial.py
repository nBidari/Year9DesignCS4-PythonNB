# USER: https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBkbidNavhMbjzAkd63OXEEyweWgHCviOE
# PASS: https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBkbidNavhMbjzAkd63OXEEyweWgHCviOE

#email: "nima.bidari@ucc.on.ca"
#password: "helloibrahim"

import requests

i = 0

while i < 40:
	requests.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBkbidNavhMbjzAkd63OXEEyweWgHCviOE", allow_redirects = False, data = {

		'email': 'nima.bidari@ucc.on.ca',
		'password': 'helloibrahim'

		})

	i = i+1

	print("Get Trolled Ib!")