# Discord-Bot-Spam-Classifier
This bot classifies messages as spam or not using SVM and will then delete them. 
Users which spam more than five times are soft banned
List of users who have spammed refreshes every 5 minutes
classifier_creator.py is for creating model.pkl and does not need to be run
classifier.py contains a function which utilises model.pkl to make predictions from the users message if it is spam or not
bot.py is the main file and will run the bot to detect spam
