scrape-kbb
==========

Mainly this excercise is to use requests, beautifulsoup, pandas and matplotlib along with collaborating with @nettns who is new to python/github and these technologies.

Specifically it would be nice to do analysis like the following:
 - How is my depreciation changing week to week (requires weekly scraping)
 - What is the depreciation curve for a given used vehicle
 - What is the optimal mileage point to sell you used vehicle


### Glossary ###
 - Make: Vehicle Manufacture
 - Model: Relase name of a Vehicle
 - Year: Release year of a Vehicle
 - Style: Trim of the Vehicle
 - Intent: Intent <buy/sell><sup>1 2</sup>
 - Mileage: Self Explanitory

 <sup>1</sup> Buy Intent 		(key)
  - Certified Pre Owned 		(cpo)
  - Suggested Retail 			(retail)
  - Private Party				(private-party)<sup>3</sup>
 
 <sup>2</sup> Sell Intent 		(key)
  - Trade In Value				(trade-in)
  - Private Party 				(private-party)<sup>3</sup>

  <sup>3</sup> Same value, regardless of intent (only difference is page formatting)


### References ###
 - http://www.r-bloggers.com/how-to-buy-a-used-car-with-r-part-1/