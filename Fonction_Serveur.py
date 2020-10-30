#!/usr/bin/env python
# coding: utf-8

# In[35]:


import boto3
import numpy as np
import random
import sys

from datetime import datetime

s3 = boto3.resource('s3')
sqs=boto3.resource('sqs')


requestQueue = sqs.get_queue_by_name(QueueName='requestQueue')
responseQueue = sqs.get_queue_by_name(QueueName='responseQueue')

def QueueTreatment():
    response=requestQueue.receive_messages()

    for message in response :
        #on stock le message en local
        tableauBrute=message.body.split('sep')
        tableauBrute.remove('')
        for i in range (0,len(tableauBrute)) :
            tableauBrute[i]=int(tableauBrute[i])
        print(tableauBrute)
        #on supprime le message
        message.delete()
        #on effectue nos traitements
        minStr = str(min(tableauBrute))
        maxStr = str(max(tableauBrute))
        meanStr = str(np.mean(tableauBrute))
        medianStr = str(np.median(tableauBrute))
        #on créer la réponse et on l'envoie
        réponse = 'Le min est '+minStr+', le max est '+maxStr+', la moyenne est '+meanStr+', la médiane est '+medianStr
        responseWorker = responseQueue.send_message(MessageBody = réponse)

#on créer le log file        

def createlogFile():
    response=responseQueue.receive_messages()
    for message in response :
        with open ('myfile.txt', 'w') as mf:
            mf.write(message.body)
            mf.close()
        seedValue = random.randrange(sys.maxsize)
        s3.Bucket('mybucket1808').upload_file( 'myfile.txt' ,str(seedValue))
        print('Ceci est l ID de votre fichier, notez le pour le retrouver, il sera nommé par cet ID :'+ str(seedValue))
        message.delete()

