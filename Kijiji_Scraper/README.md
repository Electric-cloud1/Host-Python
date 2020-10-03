# Kijiji Web Scraper #

<a href="http://fvcproductions.com"><img src="https://kijijiforbusiness.ca/wp-content/uploads/2018/09/Kijiji_logo_PURPLE_RGB_EN.png" title="kijiji_web" alt="Kijij_wbber" width="250" height="128"></a>
[![CodeFactor](https://www.codefactor.io/repository/github/Weezity/Kijiji_Web_Scraper/Badge)](https://www.codefactor.io/repository/github/Weezity/Kijiji_Web_Scraper)


## Description ##

A mini 'project' that allows user to scrape a certain category in Kijiji, returns new values during the runtime whenever it can find a new value. Overlapping items are not outputted, allowing for data scrapping usages and data science.

## How to use ##
Enter your parameters in the main, including the specific page you are scraping in Kijiji and the amount of pages you want it to monitor. Then run runfile.py. 

>In case you want to leave this overnight, please ensure your computer is not a potato. Or just run it on AWS.



## Problems and things learned ##
Grasped the basics of request and web scraping. 

Problems solved:
- [x] Preventing log overlaps 
- [x] Switching pages
- [x] Webhook breaking on duplicate runs



## Imports: ##

Beautiful soup for web scraping

Requests for accessing the web
