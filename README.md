# Party-Analyzer
The purpose of this project is to explore the Twitter API and **sklearn**'s machine learning models. I collected tweets from
eight politicians - four Democrats and four Republicans - and classified them using three models: Decision Tree, Support Vector
Machine, and Multinomial Naive Bayes.

## Data Collection
The data collection process can be found in [get_data.py](get_data.py).

I used the Twitter API to get tweets from eight users: Nancy Pelosi, Alexandria Ocasio-Cortez, Ilhan Omar, Chuck Schumer,
Donald Trump, Mitch McConnell, Ted Cruz, and Lindsey Graham. Each tweet comes with information like the text, re-tweet count,
the date it was created, etc. I created a dictionary to hold that data and appended that to one of two lists, depending on
whether the user was a Democrat or Republican. I then dumped that data to one of two json files. This allowed me to collect
data over the span of a week and add it to existing data, since the free license of the Twitter API has limitations. 

I acknowledge that collecting tweets from such a limited amount of users can cause negative effects on the models, specifically
when it comes to how well they can generalize, but since the purpose of this project was exploration, I decided to go with a
simple approach.

## Data Processing
The data processing process can be found in [process_data.py](process_data.py).

The first thing I did was load the two json files into a pandas dataframe. I could then use **textacy**'s preprocessing 
library to clean up the text of the tweets by getting rid of things like emojis, emails, punctuation, etc. Using 
**sklearn**'s feature_extraction library, I was able to create 2000 labels for each tweet. 

The last thing I needed to do was create a target array and split the data into training and testing data. I just went 
through the data I had and assigned each tweet a 1 if the user was a Republican and a 0 otherwise. I then split the data into
training and testing with a ratio of 0.8/0.2, using **sklearn**'s model_selection library.

## Learning
The models can be found in [learner.py](learner.py).

I used three models for classification: Decision Tree, Support Vector Machines, and Mulinomial Naive Bayes. Before fitting
each of these models, I performed a Grid Search to find the best set of parameters using **sklearn**'s model_selection
library. I then fit each model using my training data, and calculated its accuracy using my testing data. 

The accuracies were as follows:
- Decision Tree: 0.9809
- Support Vector Machine: 0.9826
- Multinomial Naive Bayes: 0.9287

While I acknowledge that there's a good chance that these models could be overfitting (the Decision Tree has a depth of ~200
#yikes), I have not visualized my data or run tests with more data, especially tweets from users that weren't included in
training. This could be done in the future, but since the purpose of this project was to get familiar with the Twitter API
and **sklearn**, I will not be implementing any further testing in this project.
