import pandas as pd
import requests
import json

try :
    #URL = "https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/dev.json"  #link to JSON file #this is the dev.json and it has far fewer entries
    #URL = "https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/test.json"  #link to JSON file #more than above, less than below
    URL = "https://raw.githubusercontent.com/czyssrs/FinQA/main/dataset/train.json" #link to JSON file

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
        if not (question == "" or answer == "") :                                        #if we dont have a question or an answer, we don't want it
            questions.append([pretext + table + posttext, question, answer])               #add to list of questions to ask ChatGPT

    pd.DataFrame(questions).to_csv("FinQA_processed.csv", header=["input", "question", "answer"], index=False)

except Exception as e :
    print("Failed: ")
    print(e)
    
#eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..mT6w-0iN51jZi98w.9_dDJ7LGRKa4DseBiMzuGTkR3kWHJ_rHwJnCuzwCK6I-40eTEBtb0osc2Obt3kdWJkmqf0TsIoUAjzYlfiPuGc0d5Pe-9j3yIvgKnhrtZEiHZcvD2MPOQLhqx-1OGlHunmwTL5oMxLsoddC6ZytTsZPDpLevdU4w2GeAiVYP7nvcWnYiKJlYMS2QOqHWpz-Niz0EcPwcu9SANCtgZdr9rPPMX0Ouh6HLt-RaZghd67dAlaBh70WtTARkpsldyx1Hf3mwdJxr5uBSNkXTUySjKIKBetThbyopRsys-uu-x2H3lIeMqwtuQfy-Q8Uocd2I_0uIrEIA8Gg_7Wfyc0z0G8yDUaVX2q7zfwvk-i1rD5eYcG_3TTFIzMpI4ZGwcI60an_h8AfXxPJIbleSrCL9yNdNBltNSn08ekgDbGu6udApqRqzO6NKxeKAT_N_z-1v-gqrmYV_oX4A6jxeWYA27tpmjgaTdurxF_YuBKYsGGwZbHbO5QUl3OUwv4sZ_7E2e7ud-gJzC03WGRl0UAjURpSLyjHJMdDPHS2HNKcUW9nghK7LHpxi7-tmFWOb_rRfOjTkpJB8N18uZTXT0cw91t80JjJdWiScvrvj-UZN3S0NJD0F5MWcDKc7llkJRi4KM3J16fihEWDbfOjKOo7azjVIXw6yMLLL6T5O3xISwQiv-cMkE19cDCnFuR84o-EMp1T8Jgbq_etaP_QJtvOOC_GOjJa1v5VGvOXynYu7pBGZJNVOMgCmw9T7vglkmc5pZuVzgNBv70btAM4D5IcVOnlDShAV4lHg6P-KDUv9yEvZanYJtVslLI1qXIZEi5Y03QeQPjrZOJUlfL_GhuMoaTijY_BajO9qxLT9cxqNIGgOns5pewPzWHYA-5a5CdkcGrZ7xPIENw1bJfzyrsgg8Q8HLgStFhDbLU6eEZHKmliyKqEK_z8i_Gly9806OCL-VaUwnqH-38UMOecFju86F_TzfxbTvwLhmG-LW9F4jn-xp715d3LRwNvUrp1raUUw2NExybqZuTiLDesBd0hmTmIC5B48vmCVdSQ4ucCKIL3tz2nEBSmkMorhrvudZY72-lsxcCDrYdUBFqrlDQCGCIY4cYU_PjI6hSUOqKxRlkkM5Nyf-huWPFgeIkrWzMeV4I_rGWL6bxFbvqytNUAlCkq3yKhZMqTFdXXDZDyF3yDwaCTTlgFVH_xwO3AKqMmsMlKlzzDMkIb3_wr46d_5DCtyDOT7LHItMd3lKhcJe3Hs9kz4rDrWZwrdlPOk9VGE_fqlCbeE8cuijbRyrrhA_L6mRSFfnYXVwF93PrcTRA7L5ft7lTFvP6g8AypgYoAfqemBo8TD4fv-M6yGUDoRuVk4NM4yC5sl1CjZJa6yvYA_ZV6rzfQRN7fCfR0TNoF3-k5Qabx11RNbmhO_5eay24vkIHlahUyBdgLyJQ8EwlBLuFiknDXUSkTN6dWjvnSoc-8MiNgFd78s9zdlZntbvlpOd_N5aIH_p-ROBNjh-r8F6uysZU7kmv10QvL-Or_KTpGH3H0NwaVN2tO_6WDKPvnqrnZq5U_lRRncDUqYObHeMZOJ-bKejXTsMHandLI9zfOvWW_ekztvVJhfmIANLkauYCvh4BAkqN4RiRutPVEboIUOVsEanJ9KHtDF3Obg7yiQ8G1KbElzgAUKJ42FZyVI4AlvPtEINsUb-hJHbxjknauvFCADDnkTb79_IuvVFr_otM6MCISXp3gr1ND36RCJbzXA-0FTiC-MYF2wf_wmXbEyBNulVmCmTNyKsEAFgjT6I3tEdfmQtW5yGbrTP6OFGMY23AtNW5MS6IVtb-bN6H0XRUHbOZWPyfyY785TvIncaoEM3QilxLT18omJ6BlKgTiPkh1CdEvTPRJVXrFO9OZlXs5msNqFJo3HS3Snkc6y7CXlwhRwoqcBrwZXrTXIRfZahnMBvV5S7vEHsg0fhgAT2J3IC0LoqqVaceOT6bmqdRl0soHK39M_MxMy0vlhrcwfkyu63by_F1ZbJWoUW9nNbof0aGVd12I1AFlDgGjitfO0IgJOVIOp_l60evWX6ZJUgIVLJ2gUPPApcPBI_95yairo4M09v3NlPlk1M6onqMIx5mPbIYleH0xIh_CsRMvaRf1u0tB4owZNBmf9rwqdeV9tsGfqO42VlsldF2Eam8Ep003kF3I1mR39oQfyBlSdkKaSBuhGe6LVhNwaCNneYyVYPB8T_SY_jXJzRyrm2s3PqqZVtO1w463VEGw16YiZj0LLr-7Y4sZO_C2zWbZl43PdKQQ81oZYYYdMB70PwIoO5lNmYFOITXdmcDjnw9aUw00KAP9kVxel90ZsP0KmJad1vxOfz7wwucuurntGPswc-w12iGA-5IbMIO4uy_o0ppP1XC-CbClvQtWsg-_F0H0NKouRTwrCQqL0BCyf4rH72_AwhO-H2xg6mf5sLckSU_ZE3RY-WqIfELeLxKSpjXRUwzlaD919gjGFioeWq3axlKiMtOB_RvuBVoCAGqoC2mcG7x7cJpH-OEt4dWB8laXvG9zrVICuVGxBgAzEJl7Q9mftnRcBLgcV2Wt8ad5ykVQgICuMjpzWsfmlF2BNaCaIa7PL1b21GRWoXxmEBtEGBsFM5_obsG8UviZnoWesUwyavlHdW4pbq1k3DYWJ8maKhAQ.W7bYYntkJcM1pueeCHcXbQ