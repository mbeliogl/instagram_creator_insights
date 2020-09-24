from defines import getCreds, makeApiCall

'''
Grabbing basic account info. i.e. [id, followers, following, biography...]

'''


def getAccountInfo(params):

 	endpointParams = dict()
 	endpointParams['fields'] = 'business_discovery.username(' + params['user_name'] + ')\
 	{username, website, name, ig_id, id, profile_picture_url, biography, follows_count,\
  	followers_count, media_count}'


 	endpointParams['access_token'] = params['access_token']

 	url = params['endpoint_base'] + '/' + params['instagram_id']

 	return makeApiCall(url, endpointParams, params['debug'])


params = getCreds()
params['debug'] = "NO"
response = getAccountInfo(params)






 
