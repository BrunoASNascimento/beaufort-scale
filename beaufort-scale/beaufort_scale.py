import json
import os


def loading_language(language):
    #! Clear string
    language = (language.lower()).replace(' ', '')

    #! Test language
    directory = 'beaufort-scale/translate/'
    list_file = [sub.replace('.json', '') for sub in os.listdir(directory)]

    if language in list_file:
        name_file_translate = (directory+language+'.json')
        with open(name_file_translate, 'r') as json_file:
            data = json.load(json_file)
    else:
        print(
            f'ERROR: Not exist the {language} in translate, please select a in list {list_file}'
        )
    return data


def beaufort_scale_ms(value, language='en'):
    #! Loading translate dict
    translate_dict = loading_language(language)

    #! Beaufort scale in m/s
    if(value < 0.5):
        str_value = translate_dict['Calm']
    elif((value >= 0.5) and (value < 1.5)):
        str_value = translate_dict['Light_air']
    elif((value >= 1.5) and (value < 3.3)):
        str_value = translate_dict['Light_breeze']
    elif((value >= 3.3) and (value < 5.5)):
        str_value = translate_dict['Gentle_breeze']
    elif((value >= 5.5) and (value < 7.9)):
        str_value = translate_dict['Moderate_breeze']
    elif((value >= 7.9) and (value < 10.7)):
        str_value = translate_dict['Fresh_breeze']
    elif((value >= 10.7) and (value < 13.8)):
        str_value = translate_dict['Strong_breeze']
    elif((value >= 13.8) and (value < 17.1)):
        str_value = translate_dict['High_wind']
    elif((value >= 17.1) and (value < 20.7)):
        str_value = translate_dict['Fresh_Gale']
    elif((value >= 20.7) and (value < 24.4)):
        str_value = translate_dict['Strong_Gale']
    elif((value >= 24.4) and (value < 28.4)):
        str_value = translate_dict['Storm']
    elif((value >= 28.4) and (value < 32.6)):
        str_value = translate_dict['Violent_storm']
    elif(value >= 32.6):
        str_value = translate_dict['Hurricane_force']

    return str_value
