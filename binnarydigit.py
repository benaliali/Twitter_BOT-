import tweepy
import time
#ces informations deverons être changé par les votres elles sont strictement personnelles
CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_KEY="-"
ACCESS_SECRET=""

#les trois instructions suivantes pour ce connecter a tweeter en utilisant l'APi creé sur https://developer.twitter.com/
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

fileName="lastId.txt"
#recuperer les l'id du dernier teweet déja sauvegarder
def retriveLastId(fileName):
    f_read=open(fileName,'r')
    lastId=int(f_read.read().strip())
    f_read.close()
    return(lastId)
#sauvgarder l'id du dernier tweet dans un fichier
def storeLastId(lastId,filename):
    f_write = open(fileName, 'w')
    f_write.write(str(lastId))
    f_write.close()

def replayToTweets():
    #recuperer l'id enregistre dans le fichier
    lastId=retriveLastId(fileName)
    #extraire les tweet concernant macron
    mentions=api.search('macron',count=100,since_id=lastId)
    #parcourir chaque tweet et lui repondre
    for mention in reversed(mentions):
        storeLastId(mention.id, fileName)
        #eviter de repondre a ces tweet
        if mention.user.screen_name != "BinnaryDigit":
            print('Entrain de répondre...')
            api.update_status("@"+mention.user.screen_name+"  please, follow us on twitter.com/BinnaryDigit !?",mention.id)
while True:
    #appele a la oncion qui repond au tweet
    replayToTweets()
    #le programme sarrete apres chaque 1mnt car le nombre de requetes permis par twitter est de 15 par 15mnt
    time.sleep(60000)
