import pandas as pd
import requests
import json
from pyChatGPT import ChatGPT
import csv

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..vr1H2Tqzy1v6tnNt.abM-VltFxgn8rTz0_HbOpyFAKyvx-E_p1iVJU0eUISrCWPOCc-J6PGtbAamHLlw-qkPj1FJ6b0BYhHLDwA5dMQ2x2z3X6wapbNXTnjCFADPiWtMYSPHHOoWmpXzY_k4q33t5Soaevbtq6WFF3sefkx0xX3ZhP6QXdN7oyxtGt7oYiUd2LpyvFqviVF4p-_ds4MlvFXm66MQH_q2LTK2-a9BCroH8xVHwyDXTUj6HVB5vQv-mgNgLfSzwoc3tSijeHRX6MZ3ROKxxBmwHDC3hcIO7Ura4MnfzSV0W85yMKM9ZTcmAxbZ8OgsjETpbQurA7fRg4a3j19sbZ28GAZ-XPDUBGpRENfo24Ic5_t3Jp9ZMQdLQlWXS3QNl7ao0K-qj2mFbmUFDtkG2_Wr8wxpmtMg7fjRwz7WzdxbujQnaB0azQIKP-tAY9JqJOiRqOp5A1ryxlyPaGYXHlLnLr2Z00fqmjeL7ao56oSN-YFKSgJCBLarHWeReQ_BIeP5Eozawsn1ZZm2UEMmuyPmcfCbA5T5yxlWzKibnSrQF7tqYB6NGECz7dIc3GiyHB8tIWQ2LKSBhvEdcS8AmhzkwAqDpSp9aLAl7XJifFtOK0P8sLYheAci5bGhyTXUgF3WfFgfKq-U_XjB7Ktns6bQameKhHv5bdNCs2pcs5w9_nrq-2vp8U1lgsbYhRYjd7Ypc79-858VrDUVar_fx2cNProYlD3OQFMJR5Xu7WBL7A208XrFow8rh9TWqGgtThsenZYr47NVaKPHUqUeS8wTYhGgnmj1NwksNuvy_QHtsJQ0vGwN5818aW2WgGiE3Y7KV50C2a8vIS4gS9mdwj0PLYnXG-qnrhVLIlArXJ5Wx0o0uH24AhlLqUtUpdBPzBDvLtcfdRt4s-A2g7kqO6rt9Vv_T3-uiGfSlzOpo90YYWDxkXtZ17Xk0qQ6M0WilaaiIjteTHfRSro03I2K_qJWJ6OXpWigLTzMcLIWtJcODrVKCQH31HB2q2pXE1vcPMppBAtxz0XUB9j_MZFVh1XL-9iBhRPplGmm3jA_q7GUDUv03yJeyCqKYOb0HmW3mFzvLzXeoR9bJo8u3AgtSYfpKfSdfAuh0ngOHcShBSGb9499QdcjWYjmczLmMpFwK9pDXrx-HdJlJrDWz2GzjD_mWjyJz6WIYxykZIZkuRC3FypfeiH7Jd8kPeKaKPLJ1QbCLVwPVwQr3GcjPcpLuKtlovGRWJyXp6_cR4O_sHXfPqBTh1_2QOktoNVu6rh9-W2x-VUjWT-zB_wcMBFM8e4qkLurmlE6a1QxQXr175BaFH1c5eWO3eAiOrXuQGcON3bUW2oa1js-r3-_BHoCptq0qITtLDLiNMjm4Lrkk6hVAYgBTnXex8GCcbK4Dt3P2V99APILK919XGeflv0h6mdUKuYNUTIqm5Xky1pOYCClu8L9APL-wWM7nnObuxTWM1qDQGd7ovzJ3viATsvOJhhMPeSLk7qVjYQ1ZxjHFQMIchiEQ_2q0y3APK1BstJzx2RCnezKDDO3G-I9gtZbseOTcpth3vYIPkQOBbfRA1u7JBTZC_oIQSHRLG1njwSVrnjtWzosNfA9QIn8maKn0QhlYkC7UKaF0hJ7guLOV5tj5u4YQZeADN5_1-4ui_CPaX18KsmmcX-wZVuK2uLYs_CVAyH88XdTquKo1DAwhjm7oKFbaCPP_O0wO0NLrheHCoChhDt-dwsjRiLkfYX8LzH6MrfEBofmrUvxCfbO3bm1upVE0I7MQFKDNB_6ihl3JmT_R3gpQy0ox5EMsR1rYvQP1ocqXtoQKE7e8UtLeoUOdC_yeX1mZq4jtmR7HWrv57ke1N80UJdhqV1MVHPZvV42ZzNmBJYAUyxilPX4aS7Ik5ArGzOCr9rm5RaTCpVFK12E4epT4tuPmiuR40hn1Ym2jm-kR5Mqw6x-ZwYcZyvdRcf42gepdodSnShmMIDoSAs3Sm54u0QcxiWLAJ139cXlVvM1WaCw60jJjrr4yO2msem06AVVusTk2bRHweWrWaP2Fl7dOdPoTFWLPhsaA_b1ggOjUV1-Atdj2rT516uagus98h5E55brkV-ceSe-EtdOW1KZRw97pXnq3kzmGBijAMjtfi5oKf2kp1jzHB0BnClZ_PpztRRHCOCmj7fexp49fjtA8XFow3kVHnsdsnzYXECGTPLDPsmJVSbLaFtkrHUtHn_X9h5io1u7nVLIVJoQBUefNBvyiq-mPpPBzz7MZnslDrN4IKiNSVjNJse0xjmBOdJvsXgJwh-3UwJUzbRSB5gcib8PvD6AB2tk-CqhDK0NtPn6fNaB0M-sIINEm0vo8LM07N70n1a5K7NywP4yV4V4994gg-7yrTjHR1VB-o7Pva2xG4JsSGbhJ9qoFDl-9fYeHmqV_GBoe9jE6Fc6hntQiI4RfQRU6WaFs62JzxjwgjI3MW4N4w82a4X6ZJdfEfqDCroNGl3hgsu5TT41Wi5C5ya-RxTRp50RZJRHlg0FfYcjuIXJuMDz7Rj9jJKAX5BHrsChjH8DMCVoXTlGTxHxiOL10v172c_pOPQZWxRGHnhpWGpLrgJJTlOZKAQuiar7Bm5r0VtygzM23UfcnE7l2xbzyxRctEHd16snvQs8AKUANj7wqOCcT7v-q446BaB8Ztw2km7huk0U.-vZ10TvIpKs_hmiCAfYIWw"
session = ChatGPT(session_token, verbose=True)
try :
    i = 0
    with open("FinQA_processed.csv") as questions :   #open csv that contains the text, table, question, and answer
        reader = csv.reader(questions)                #open a reader to go through each question
        next(reader, None)                            #skip the header
        for question in reader :                      #go through each question
            if i == 1 :                               #i only want to upload one for now
                break
            print("Given the following information, \"" + question[0] + "\" " + question[1]) #concatenate the question and answer
            print()
            print("=" * 20)
            print()
            msg = "Given the following information, \"" + question[0] + "\" " + question[1] #build the message
            resp = session.send_message('Hello, how are you?')                              #send the message to chatGPT, right now just simple string to ensure error is not due to datatype or something
            print(resp)                                                                     #print chatgpt response

            session.reset_conversation()  # reset the conversation
            session.clear_conversations()  # clear all conversations
            session.refresh_chat_page()  # refresh the chat page
            
            i += 1

        questions.close()
except Exception as e :
    print("Failed: " + str(e))