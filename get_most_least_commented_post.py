
'''
comments count list contains tuples
i.e. (post_comments_count, post_ID)

'''
def getMostLeastCommentedTuples(postList, com_count_list): 

	for post in postList:
		tup = (post.post_comments_count, post.post_ID)
		com_count_list.append(tup)

	return com_count_list



def getMostLeastCommentedPost(com_count_list):
	most_comments = max(com_count_list)[0]
	least_comments = min(com_count_list)[0]

	for i in range(len(com_count_list)):
		if com_count_list[i][0] == most_comments:
			print('Most Commented Post: ' + str(com_count_list[i][1]) + ' ' + 'With ' + str(most_comments) + ' Comments')
		if com_count_list[i][0] == least_comments:
			print('Least Commented Post: ' + str(com_count_list[i][1]) + ' ' + 'With ' + str(least_comments) + ' Comments')

