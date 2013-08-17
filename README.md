### scrape-kbb ###
-------------------------
The primary goal of the project is to capture Kelly Blue Book (KBB) value information to use for depreciation ananalysis.

This will be accomplished by querying KBB for several configuraiton of a particular make and movel of vehicle. Price information is updated weekly on KBB and will be captured on weekly intervals. The program will query the site for the make, model, style (trim), and mileage. The program will capture price information for one of three purchasing intents, and for a variety of vehicle conditions. 

### Design ###
-------------------------
Mainly this excercise is to use requests, beautifulsoup, pandas and matplotlib along with collaborating with @nettns who is new to python/github and these technologies.

Specifically it would be nice to do analysis like the following:
 * How is my depreciation changing week to week (requires weekly scraping)
 * What is the depreciation curve for a given used vehicle
 * What is the optimal mileage point to sell you used vehicle

### Behavior ###
-------------------------
Took a while poking around on the site to make the following list. In general the site isn't very clear as to what rabbit hole you have gone down to yield a specific or set of cost(s). There seems to be three intents, outlined below with example option queries and example yields.

All base urls appear as:

    http://www.kbb.com/<make>/<model>/<year>-<make>-<model>/<style>/?intent=<intent>&pricetype=<pricetype>

Intent : buy-new

	pricetype : none
	yields : MSRP, Fair Purchase Price, Dealer Invoice

Intent : buy-used

	pricetype : Certified Pre Owned (cpo) (?intent=buy-used&amp;pricetype=cpo)
	yields : Single Price [Excellent]
	
	pricetype : Suggested Retail (retail) (?intent=buy-used&amp;pricetype=retail)
	yields : Single Price [Excellent]
	
	pricetype : Private Party (private-party) (?intent=buy-used&amp;pricetype=private-party)
	yields : List of Prices, [Excellent, Very Good, Good, Fair] 

Intent : trade-in-sell

	pricetype : Trade In Value (trade-in) (?intent=trade-in-sell&amp;pricetype=trade-in)
	yields : List of Prices, [Excellent, Very Good, Good, Fair] 
	
	pricetype : Private Party (private-party) (?intent=trade-in-sell&amp;pricetype=private-party)
	yields : List of Prices, [Excellent, Very Good, Good, Fair] 



### References ###
* http://www.r-bloggers.com/how-to-buy-a-used-car-with-r-part-1/
