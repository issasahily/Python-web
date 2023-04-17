"""function that make the text translate"""
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
#load enviroment variable from .env file
load_dotenv()
#without load_dotenv we cannot get the value from .env file
#et values of specified enviroment variables
# apikey = os.environ['apikey']
# url = os.environ['url']
authenticator = IAMAuthenticator("cnnI1I5wXnOgYzRoxecjM6w6-o8DS7ksNISYltVx0xYh")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/e28886be-1e6c-4a12-b296-be06bfefd272")

def english_tofrench(english_text):
    """ funtion to translate text from englich to frensj
    """
    #write the code here
    if len(english_text)==0:
        return ""
    frenchtranslation=language_translator.translate(
        text=english_text,
        model_id="en-fr"
    #return the results of a previously run function. You will be able to get the id of your action
    ).get_result()
    #its return object with key "translations" that contain array with index translation
    return frenchtranslation["translations"][0]["translation"]

def french_toenglish(french_text):
    """ function to translate text from french to englisj
    """
    #write the code here
    if len(french_text)==0:
        return ""
    englishtranslation=language_translator.translate(
        text=french_text,
        model_id="fr-en"
    ).get_result()
    return englishtranslation["translations"][0]["translation"]
