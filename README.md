# yelp-classification
## Georgetown Data Science Yelp Classification Project
### Team members 
Virginia Sun(project coordinator), Ed O’Brien, Robertson Wang, Nas Baig, Peter Kang

### Domain chosen 
Travel and Entertainment/ Food

### Hypothesis or project topic
There exists a correlation between the textual sentiment embedded in restaurant reviews and the rating of that review. If the hypothesis is true, then canonical machine learning algorithms should be able to do an adequate job in classifying restaurant reviews based on cleaned up text. Since a restaurant’s average rating based on the ratings of the underlying reviews that it receives, we would like calibrate a classification system in order to best predict a restaurant’s rating based on its reviews.

### Available data sources (or where you’re going to get the data from) 
The dataset to be used will be the yelp_academic_dataset_review.json
file available from the https://www.yelp.com/dataset_challenge/dataset website.  It is yet to be determined whether we will be incorporating the yelp_academic_dataset_user.json
 dataset or the yelp_academic_dataset_business.json dataset. 
	
We may use the yelp api to get new reviews to add to our dataset, or use web scraping techniques if the api becomes too difficult to use for getting large amounts of reviews. Additional review site data sets , such as comments from the google places api, might be useful for our model.

### Project description
In a nutshell, we want to be able to predict the quantitative restaurant rating(output) based on the review text(input) provided. We will train our model on a subset of the total restaurant reviews. Using another subset of the overall restaurant reviews, we will use our model to predict the rating of the restaurants using the text of the review. One idea for the data product would be to build a ipython notebook that displays a review to the user, and then has the user guess what the rating is. We could also have them guess what rating and what restaurant the review is for.  

The machine learning algorithms we will use are all available as part of the scikit-learn Python module. Specifically, we will be using a linear support vector machine, bagged decision trees, and random forest. Further, we will also use multinomial logit regression to provide another model for comparison and to provide a sanity check on other models. Based on previous work done by researchers at UCSD on a previous iteration of the Yelp dataset, we believe that these methods will provide reasonably accurate results. 

### Questions or avenues of exploration required for the project 
* Can we find places that have text reviews that predict a higher score than it should have.
* What are the trends in reviews that can predict a high score or low score?
* Do trends that predict reviews change from city to city?
* Are there style trends in reviews that change over time?
* How much does knowing the reviewers past reviews and ratings help predict future ratings?
* Are their fake reviewers, or paid reviewers, in our data? If so, can we find them?
* If we train our model on reviews that are also not restaurantes, how does that impact our accuracy?
* What happens if we train models on only certain cities, and then have those models predict ratings for reviews in other cities? 
* If we know the weather of the city the day that the review was written, does that help us predict the rating better? Or the time of year? Or time of day? Do people write reviews drunk?( at bars at late night?) Does this inform our model for prediction?
* What are the characteristics (certain words, specific attributes, length of the reviews, etc.) of reviews for top 5% restaurants are not shown in the reviews for the rest? 
* If we do go with the jupyter notebook data product, we could take information about the user and then make predictions about their guesses for ratings.
* We could show users reviews of places they have been, and see if they agree with the reviews. We could use this ‘review of a review’ to suggest new places.  For example , they could review some reviews, with a thumbs up for agree with the review and thumbs down if they disagree. Then we could use that to make better predictions on what type of places they might like.
* We could also use the review of a review to make a dating app - it could suggest people you might want to meet, and also suggest a place you both might like. 
* Another idea is “suggest a date”  or “ pick a place” it would take one users reviews and other users reviews and suggest a place they both might like. You could put multiple users in and then it would find a place for the people to go to
