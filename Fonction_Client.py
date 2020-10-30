#!/usr/bin/env python
# coding: utf-8

# In[21]:


import boto3

s3 = boto3.resource('s3')
sqs=boto3.resource('sqs')

requestQueue = sqs.get_queue_by_name(QueueName='requestQueue')
responseQueue = sqs.get_queue_by_name(QueueName='responseQueue')


def ChartSend():
    #le client créer un tableau de 20 entiers et l'envoie dans la requestQueue
    msg = ''
    count = 0
    print("Entrez un entier")
    while count < 20:
        x = input()
        if x.isdigit() :
            msg = msg + x + 'sep'
            count += 1
        else :
            print("Ce n'est pas un entier, recommencez s'il vous plait")
    #on affiche le tableau pour voir si tout fonctionne
    tableauBrute=msg.split('sep')
    tableauBrute.remove('')
    for i in range (len(tableauBrute)) :
        tableauBrute[i]=int(tableauBrute[i])
    print('Nos données brutes sont : ',tableauBrute)
    response = requestQueue.send_message(MessageBody=msg)
    
def ChartSent():
    print('rentrez l ID de votre tableau')
    ID= input()
    s3.Bucket('mybucket1808').download_file(str(ID), 'My_Chart.txt')

