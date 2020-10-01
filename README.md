

#### Definitions:

> Usage:
>
> 1. In file _defines.py_, fill in the required credentials 
> 2. To the the page_id, run _python get_user_page_id.py_ 
> 3. To get the instagram_idm run _get_ig_account_id.py_ 



#### Business Discovery:

> Usage: 
>
> 1. In file _defines.py_, uncomment line 45 [writeResponseBasicData(response)] 
> 2. Run _python business_discovery_.py 

> Output:
>
> 1. business_discovery.txt 
>
>    The file contains the following fields:
>
>    - `biography`*
>    - `id`*
>    - `ig_id`
>    - `followers_count`*
>    - `follows_count`
>    - `media_count`*
>    - `name`
>    - `profile_picture_url`
>    - `username`*
>    - `website`*



#### Media and Insights: 

> Usage:
>
> 1. In file _defines.py_, comment out line 45 [writeResponseBasicData(response)] 
> 2. In file _defines.py_, uncomment line 46 [writeResponseMedia(response)] 
> 3. Run _python get_media_and_insights.py_
> 4. In file _defines.py_, comment out 46 [writeResponseMedia(response)] 
> 5. In get_media_and_insights.py, uncommnet lines 69-128 [writeResponseMediaInsights(response, post), getUserMediaInsights(params, postList)]
> 6. Run _python get_media_and_insights.py_ 

> Output: 
>
> 1. media.txt 
>
>    The file contains the following fields: 
>
>    - Post Number
>    - username 
>    - timestamp 
>    - comments_count 
>    - media_type (photo/video)
>    - id 
>    - media_url
>
> 2. media_Insights.txt 
>
>    The file contains the following fields: 
>
>    - Post Number 
>    - Post ID
>    - Post Link 
>    - Comments Count 
>      - Total number of times the media object has been seen
>        Total number of unique accounts that have seen the media object
>        Total number of unique accounts that have saved the media object
>        Total number of likes and comments on the media object



#### Story Insights:

> Usage: 
>
> 1. Run _python get_story_insights_.py 

> Output: 
>
> 1. story_Insights.py 
>
>    The file contains the following fields:
>
>    - Story Number 
>    - Story ID
>    - Story Link 

```python
		#Story objects metrics will return error code 10 if < 5
  		#(ERROR CODE 10) Not enough viewers for the media to show insights
```



#### User Insights: 

> Usage:
>
> 1. Run _python get_user_insights.py_

> Output: 
>
> ```python
> #Insights data is not available on IG Users that have fewer than 100 followers.
> #Full functionality will be implemented later 
> ```
>



#### Extras:

> Selenium webdriver script for loggin in to [instagram](https://www.instagram.com/)
>
> Usage:
>
> 1. Run _python account_info_bot.py_ 

> The functionality will eventually be expanded to include more useful insights and statistics.  A simple and intuitive GUI will also be implemented. 
