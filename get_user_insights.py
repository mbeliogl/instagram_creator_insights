from defines import getCreds, makeApiCall

### Insights data is not available on IG Users that have fewer than 100 followers.
### Need to test with more followers 


'''
GET https://graph.facebook.com/v8.0/{ig-user-id}/insights
  ?metric={metric}
  &period={period}
  &since={since}
  &until={until}
  &access_token={access-token}

 '''

def getUserInsight(params):

	endpointParams = dict()
 	endpointParams['metric'] = 'audience_city , audience_country, audience_gender_age, audience_locale'
 	endpointParams['period'] = 'lifetime'
 	endpointParams['access_token'] = params['access_token']

 	url = params['endpoint_base'] + params['instagram_id'] + '/insights' 
 
 	return makeApiCall(url, endpointParams, params['debug'])



params = getCreds()
params['debug'] = "YES"
response = getUserInsight(params)