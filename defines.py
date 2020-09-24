import requests 
import json



def getCreds(): #get API credentials 
	creds = dict()
	creds['access_token'] = ''
	creds['client_id'] = ''
	creds['client_secret'] = ''  # all taken from FB graph API

	creds['app_id'] = ''

	creds['graph_domain'] = 'https://graph.facebook.com/'
	creds['graph_version'] = 'v8.0'

	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
	creds['debug'] = 'NO'
	creds['user_name'] = '' #instagram account username 

	creds['page_id'] = '' #run get_user_page_id.py 
	creds['instagram_id'] = '' #run get_ig_account_id.py 



	return creds 



#makes a git request to IG graph api point
def makeApiCall(url, endpoint_params, debug = 'NO'): 		
	data = requests.get(url, endpoint_params)  #sent request

	response = dict()		#create dictionary for response 
	response['url'] = url 
	response['endpoint_params'] = endpoint_params
	response['endpoint_params_clean'] = json.dumps(endpoint_params, indent = 4)
	response['json_data'] = json.loads(data.content) #saves content from git request
	response['json_data_clean'] = json.dumps( response['json_data'], indent = 4)

	#debug! 
	if(debug == 'YES'):
		displayApiCallData(response)

	#writeResponseBasicData(response)
	#writeResponseMedia(response)

	return response


#display the DEBUG (response)
def displayApiCallData(response):
	print "\nURL: "
	print response['url']

	print "\nEndpoint Params: "
	print response['endpoint_params_clean']

	print "\nResponse: "
	print response['json_data_clean']


'''
Methods for writing response data to file with clean view
'''

def writeResponseBasicData(response):
	fout = open("business_discovery.txt", "w")
	fout.write('Link:' + response['url'])
	fout.close()

	fout = open("business_discovery.txt", "a") 
	fout.write('\n\n')
	

	for key in response['json_data']['business_discovery']:
		fout.write(key + ' : ' + str(response['json_data']['business_discovery'][key])+'\n')
		
	fout.close()


def writeResponseMedia(response):
	fout = open("media.txt", "w")
	fout.write('Link:' + response['url'])
	fout.close()

	fout = open("media.txt", "a") 
	fout.write('\n\n')

	numPosts = len(response['json_data']['data']) #number of media posts returned
	post_media_id = []

	for i in range(numPosts):
		fout.write('Post Number: ' + str(i) + '\n\n')
		for key in response['json_data']['data'][i]:
			fout.write(key + ' : ' + str(response['json_data']['data'][i][key])+'\n')
			if(key == 'id'):
				post_media_id.append(str(response['json_data']['data'][i][key]) + '\n')
		fout.write('\n\n')
	fout.close()

	return post_media_id













