
from defines import getCreds, makeApiCall, displayApiCallData
from get_most_least_engaged_post import getMostLeastEngagedTuples, getMostLeastEgnagedPost
from get_most_least_commented_post import getMostLeastCommentedTuples, getMostLeastCommentedPost
import string

class Post:
	def __init__(self, post_num, post_ID, is_video, post_engagement, post_permalink, post_comments_count):
		self.post_ID = post_ID 
		self.is_video = is_video
		self.post_num = post_num
		self.post_engagement = post_engagement
		self.post_permalink = post_permalink
		self.post_comments_count = post_comments_count


'''
'https://graph.facebook.com/{graph-api-version}?fields=id,media_type,media_url,username,timestamp&access_token={access-token}'

'''
def getUserMedia(params):	#method returns user media objects (photo/video posts)


	endpointParams = dict()
 	endpointParams['fields'] = 'id, caption, media_type, media_url, permalink,\
 	thumbnail_url, timestamp, username, comments_count'
 	endpointParams['access_token'] = params['access_token']

 	url = params['endpoint_base'] + params['instagram_id'] + '/media'

 	return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = "NO"
response = getUserMedia(params)
numPosts = len(response['json_data']['data'])
print('NUMPOSTS: ' + str(numPosts))



def makePostList(response, numPosts):

	postList = []

	for i in range(numPosts):
		post = Post(i, 0, False, 0, ' ', 0)	#id, engagement, comments_count default to 0. is_video defaults to false. permalink defaults to empty string
		for key in response['json_data']['data'][i]:	
			if(key == 'id'):
				post.post_ID = response['json_data']['data'][i][key]
			if(key == 'media_type' and str(response['json_data']['data'][i][key]) == 'VIDEO'):
				post.is_video = True
			if(key == 'permalink'):
				post.post_permalink = response['json_data']['data'][i][key]
			if(key == 'comments_count'):
				post.post_comments_count = response['json_data']['data'][i][key]

			

		postList.append(post)
	return postList

postList = makePostList(response, numPosts) #list of Post objects 
print(postList)
#getting most/least commented post 
com_count_list = getMostLeastCommentedTuples(postList, [])





#### ---------------------------- Writing -------------------------- ###
fout = open("media_Insights.txt", "w")
fout.write('Link:' + response['url'])
fout.close()


def writeResponseMediaInsights(response, post):
	fout = open("media_Insights.txt", "a") 
	fout.write('\n\n')

	fout.write('Post Number: ' + str(post.post_num) + '\n')
	fout.write('Post ID: ' + str(post.post_ID) + '\n')
	fout.write('Post Link: ' + str(post.post_permalink) + '\n')
	fout.write('Comments Count: ' + str(post.post_comments_count) + '\n\n')
	
	for metric in response['json_data']['data']:
		media_insight_Value = metric['values'][0]['value']
		fout.write(metric['description'] + ': ' + str(media_insight_Value) + '\n')	
	
	fout.close()



engList = []
def getUserMediaInsights(params, postList):	#method returns user media insights 
	
	endpointParams = dict()
	post_num = 0
	for obj in postList:
		obj.post_num = post_num
		if(obj.is_video):
			endpointParams['metric'] = 'impressions, reach, saved, engagement, video_views'
		else:
			endpointParams['metric'] = 'impressions, reach, saved, engagement'

		endpointParams['access_token'] = params['access_token']
		url = params['endpoint_base'] + obj.post_ID + '/insights'

		response = makeApiCall(url, endpointParams, params['debug'])

		post_num += 1
		writeResponseMediaInsights(response, obj)

		getMostLeastEngagedTuples(response, obj, engList)

	return response


params = getCreds()
params['debug'] = "NO"		
getUserMediaInsights(params, postList)
getMostLeastEgnagedPost(engList)
print('\n')
getMostLeastCommentedPost(com_count_list)

#print engList




