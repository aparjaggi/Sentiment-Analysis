#Sentiment Analysis using Amazon Comprehend and boto3
import tkinter as tk
import boto3
import json
root=tk.Tk()
root.geometry("400x260")
root.title("Sentiment Analysis using Amazon Comprehend")
textExample=tk.Text(root,height=10)
textExample.pack()
text_box = tk.Text(root, height = 4) #configuring output textbox
text_box.pack()
def getText():
    aws_mg_con=boto3.session.Session(profile_name="User name") # creating a session
    client=aws_mg_con.client(service_name="comprehend",region_name="us-east-1") #connecting to the comprehend service in a particular region
    result=textExample.get("1.0","end")
    print(result)
    response=client.detect_sentiment(Text=result,LanguageCode='en') #sending the text to amazon comprehend and storing the output in response variable
    Sentiment_Score=json.dumps(response['SentimentScore']) #converting dict to string
    text_box.configure(state="normal") 
    text_box.insert("1.0","The prominant sentiment is: "+response['Sentiment']+"\n"+"The Sentiment score is: "+Sentiment_Score) #printing output on the screen
    

btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()


root.mainloop()