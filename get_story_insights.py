from defines import getCreds, makeApiCall, displayApiCallData
import string

'''

'https://graph.facebook.com/v8.0/17895695668004550/insights?metric=impressions,reach&access_token=IGQVJ...'

'''


class Story:
	def __init__(self, story_num, story_ID, story_permalink):
		self.story_num = story_num
		self.story_ID = story_ID
		self.story_permalink = story_permalink




def getUserStories(params):
	endpointParams = dict()
 	endpointParams['fields'] = 'id, caption, media_type, media_url, permalink,\
 	thumbnail_url, timestamp, username'
 	endpointParams['access_token'] = params['access_token']

 	url = params['endpoint_base'] + params['instagram_id'] + '/stories'

 	return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = "NO"
response = getUserStories(params)
numStories = len(response['json_data']['data'])



def makeStoryList(response, numStories):

	storyList = []

	for i in range(numStories):
		story = Story(i, 0, ' ')
		for key in response['json_data']['data'][i]:	
			if(key == 'id'):
				story.story_ID = response['json_data']['data'][i][key]
			if(key == 'permalink'):
				story.story_permalink = response['json_data']['data'][i][key]

		storyList.append(story)
	return storyList

storyList = makeStoryList(response, numStories) #list of Story objects

#### ---------------------------- Writing -------------------------- ###
fout = open("story_Insights.txt", "w")
fout.write('Link:' + response['url'])
fout.close()


def writeResponseStoryInsights(response, story):
	fout = open("story_Insights.txt", "a") 
	fout.write('\n\n')

	fout.write('Story Number: ' + str(story.story_num) + '\n')
	fout.write('Story ID: ' + str(story.story_ID) + '\n')
	fout.write('Story Link: ' + str(story.story_permalink) + '\n\n')


	''' see below comment for ERROR CODE 10 
	for metric in response['json_data']['data']:
		story_insight_Value = metric['values'][0]['value']
		fout.write(metric['description'] + ': ' + str(story_insight_Value) + '\n')
	'''
	fout.close()
	

#Story objects metrics will return error code 10 if < 5
#(ERROR CODE 10) Not enough viewers for the media to show insights

def getUserStoryInsights(params, storyList): #get insights on each story from StoryList
	endpointParams = dict()
	story_num = 0

	endpointParams['metric'] = 'exits, impressions, reach, replies, taps_forward, taps_back'
	endpointParams['access_token'] = params['access_token']

	for story in storyList:
		story.story_num = story_num
		
		url = params['endpoint_base'] + story.story_ID + '/insights'

		response = makeApiCall(url, endpointParams, params['debug'])
		story_num += 1
		writeResponseStoryInsights(response, story)

	return response

params = getCreds()
params['debug'] = "NO"		
getUserStoryInsights(params, storyList)











