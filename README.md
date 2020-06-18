# Youtube-Channnel-Data-Analyzer
Extract youtube statistics of a channel. Uses the YouTube Data API. It extracts channel statistics like viewCount, subscriberCount, and videoCount. It further extracts statistics for each video, like title, description, viewCount, likeCount, duration and much more...

#Requirements
pip install requests (for GET requests)
pip install tqdm (for the Progressbar)

#API Key
https://developers.google.com/youtube/v3/getting-started
https://console.developers.google.com/

You need a Google Account to access the Google API Console, request an API key, and register your application.

Create a project in the Google Developers Console and obtain authorization credentials so your application can submit API requests.

After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:

Go to the API Console and select the project that you just registered. Visit the Enabled APIs page. In the list of APIs, make sure the status is ON for the YouTube Data API v3.
