
from defines import getCreds, makeApiCall

def getLongLivedAccessToken(params):

	'''
		"https://graph.facebook.com/{graph-api-version}/oauth/access_token?  
    grant_type=fb_exchange_token&          
    client_id={app-id}&
    client_secret={app-secret}&
    fb_exchange_token={your-access-token}"

	'''



	endpointParams = dict()
	endpointParams['grant_type'] = 'fb_exchange_token'
	endpointParams['client_id'] = params['app_id']
	endpointParams['client_secret'] = params['client_secret']
	endpointParams['fb_exchange_token'] = params['access_token']

	url = params['endpoint_base'] + 'oauth/access_token'

	return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = "YES"
response = getLongLivedAccessToken(params)

print "\--- ACCESS TOKEN INFO --- \n"
print "Access Token: "
print response['json_data']['access_token']
