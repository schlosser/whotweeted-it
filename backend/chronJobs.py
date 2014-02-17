import databaseMethods as db
import twitterMethods as twit



#wipe database, fill database, clear all but top 10 high scores

def main():
	db.wipeTweets()
	twit.fillTweetDatabase()
	db.purgeScores()
	print db.getScoreDbSize()

if __name__ == "__main__":
	main()
