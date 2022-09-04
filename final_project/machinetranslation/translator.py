from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY='IEmr4LRxEzC5daZ0pS1jfFRMVopgfCPvLILZuhcmyvDm'
URL='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/36445b50-8a98-484c-a7c0-bfe5cb050920'

#apikey1 = os.environ['apikey']
#url = os.environ['url']

#englishtext = 'Hello'
#frenchtext = 'Bonjour'

# Prepare the Authenticator 
authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)



def english_to_french(english):
    """
    This function translates english to french
    """
    frenchtranslation = language_translator.translate(
        text=english,model_id='en-fr'
        ).get_result()
    return frenchtranslation.get("translations")[0].get("translation")


def french_to_english(french):
    """
    This function translates french to english
    """
    englishtranslation = language_translator.translate(
        text=french,model_id='fr-en'
        ).get_result()
    return englishtranslation.get("translations")[0].get("translation")

