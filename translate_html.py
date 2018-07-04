from google.cloud import translate
import re
import sys
import click

def main():

    translate_client = translate.Client()

    # Retrieving the text to translate

    try:
        input = ''.join(sys.argv[1:])
    except Exception as e:
        print("Missing query")
        sys.exit()


    # The target language
    target = 'en'

    # Translates the text
    translation = translate_client.translate(
        str(input),
        target_language=target)

    # Replaces all URLs to their translated version
    pattern = 'href="(http|https):\/\/www.arrondissement.com\/'
    translated_url = 'href="https://www.arrondissement.com/eng/'
    output = re.sub(pattern, translated_url, translation['translatedText'])
    print(output)

if __name__ == '__main__':
    main()
