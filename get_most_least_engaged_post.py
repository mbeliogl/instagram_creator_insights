


def getMostLeastEngagedTuples(response, post, engList):

	for metric in response['json_data']['data']:
		if(metric['title'] == 'Engagement'):
			engagement_Val = metric['values'][0]['value']


	post.post_engagement = engagement_Val
	tup = (post.post_engagement, post.post_ID)
	engList.append(tup)

	return engList


def getMostLeastEgnagedPost(engList):

	max_engagement = max(engList)[0]
	min_engagement = min(engList)[0]

	for i in range(len(engList)):
		if engList[i][0] == max_engagement:
			print('Most Engaged Post: ' + str(engList[i][1]) + ' ' + 'With Engagement Score: ' + str(max_engagement))
		if engList[i][0] == min_engagement:
			print('Least Engaged Post: ' + str(engList[i][1]) + ' ' + 'With Engagement Score: ' + str(min_engagement))


		### need to format this to be nicer and write to file 