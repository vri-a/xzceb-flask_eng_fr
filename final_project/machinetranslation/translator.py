"""Module that provides functions to translate text from English to French and vice versa."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function to translate text from English to French."""
    french_text = MyMemoryTranslator(source="en-US", target="french").translate(english_text)
    return french_text

def french_to_english(french_text):
    """Function to translate text from French to English."""
    english_text = MyMemoryTranslator(source="french", target="en-US").translate(french_text)
    return english_text
