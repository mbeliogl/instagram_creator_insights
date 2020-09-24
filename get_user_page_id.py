from defines import getCreds, makeApiCall
'''
"https://graph.facebook.com/v8.0/me/accounts?access_token={access-token}"

'''


def getPageId(params):

	endpointParams = dict()
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + 'me/accounts'
	

	return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = "YES"
response = getPageId(params)

 