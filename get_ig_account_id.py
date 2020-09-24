from defines import getCreds, makeApiCall
'''
"https://graph.facebook.com/v8.0/134895793791914?fields=
	instagram_business_account&access_token={access-token}"
'''


def getIgAccountId(params):

	endpointParams = dict()
	endpointParams['fields'] = 'instagram_business_account'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['page_id']

	return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = "YES"
response = getIgAccountId(params)