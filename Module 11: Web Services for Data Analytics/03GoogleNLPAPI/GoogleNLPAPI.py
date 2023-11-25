# import google libraries for the analysis
from google.cloud import language
from google.oauth2 import service_account

# define a function to analysis the sentiment of a text
def analyze_text_sentiment(text):
    # load the key file
    creds = service_account.Credentials.from_service_account_file('my-msis-5193-projects-7e4b655258b4.json')

    # initialize a client using the key file
    client = language.LanguageServiceClient(credentials=creds,)

    # convert the text into a document type
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    # call function to analysis the sentiment of the text
    response = client.analyze_sentiment(document=document)

    # get the results in variable sentiment
    sentiment = response.document_sentiment

    print(text)
    #print the sentiment score
    print("score :"+str(sentiment.score))
    # print the sentiment magnitude
    print("magnitude :"+str(sentiment.magnitude))


text = "Guido van Rossum is great!"

# run the function
analyze_text_sentiment(text)