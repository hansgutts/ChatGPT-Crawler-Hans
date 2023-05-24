import requests
import json

try :
    URL = "https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/test.json"  #link to JSON file

    download = requests.get(URL)                #Pull raw file from github, basically a txt file
    finqa = download.json()                     #convert it from json file to python dictionary
    questions = []                              #initialize questions array

    for entry in finqa :                                                     #go through each entry in the json file
        pretext = " ".join([str(item) for item in entry["pre_text"]])        #get the pretext from json file. add " " between each line. code gotten from "https://www.geeksforgeeks.org/python-program-to-concatenate-all-elements-of-a-list-into-a-string/"
        table = ", ".join([str(item) for item in entry["table"]])            #get the table from json file. add ", " between each line to make it read like table for ChatGPT
        posttext = " ".join([str(item) for item in entry["post_text"]])      #same as pretext
        qa = entry["qa"]                                                     #retrieve qa section from json file. it is another dictionary
        question = qa["question"]                                                    #get question (ask) from finqa. questions are only one line long
        answer = qa["answer"]                                                        #same as question, but answer instead
        questions.append([pretext, table, posttext, question, answer])               #add to list of questions to ask ChatGPT

except Exception as e :
    print("Failed: ")
    print(e)
    
