# Package Summary

 ## Twitch_Chat_IRC (Credit-Xenova & Twitch)
 The Twtich_chat_IRC function will extract Twitch chat box logs, logging the messages, user ID, emotes, badges, and subscription status using a combination of Twitch chat IRC, spaCy, socket, re, JSON, argparse, emoji, and CSV libraries. Using a login, which can be a bot or regular user and will need an oath ID authentication.
 
 ## Chatlog_Extractor (Credit-Blouin (me))
The chatlog_extractor function takes the chat log input and returns the named entities, nouns, and verbs, sorted. The function passes the results of the chat logs, gathering the text data messages from the Twitch_chat_IRC, using spaCy to sort and categorize the text. Then the results are a sorted list of the entities, nouns, and verbs and printed. This function can be extended into a data list to be used for profanity filters, looking for keywords or bypasses such as, special characters (&%!@*).
* * * 
# Run Instructions for Twitch_Chat_IRC
1.  First you will need the following packages to properly run Twtich_chat_IRC, Type the following into the terminal -(the following is just an example and your directory may look different)  **C:\users\youruser>pip install -U spacy pip install (package you want to install) import socket, re, json, argparse, emoji, csv from decouple import config**

2.  Next you must change the NICK - (which stands for your username.) --PASS- stands for your Twitch Chat OAuth Password. To generate this password you can follow this link - https://twitchapps.com/tmi/ -  **DO NOT SHARE THIS OAUTH PASSWORD WITH ANYONE** A config file is not necessary, but you can form one with the following - NICK- & PASS-


3.  Adjust buffer size to your needs buffer_size = 16384 mine is listed high because within 3 minutes had over a 1000 chat logs logged and tried to stop it from overflowing/ crashing.

4. To Run type the following command in terminal - **python twitch_chat_irc.py <channel_name> -output <file_name>**

5. Other commands to stop program at message limit - **-message_limit <number_of_messages>** - or to limit the time **-timeout <time_in_seconds>**

6. To stop running program hit ctrl c in the terminal. (Notice) if program crashes data may not be created and you will not find the file in directory.
* * * 
# Install and Run Instructions for Chatlog_Extractor (CSV)

1. We will need spaCy, to get spaCy you may need three modules. To install the package type the following in the Terminal or Console:**(the following is just an example and your directory may look different)** C:\users\youruser\>pip install -U spacy

2. Here are the other packages you may need just follow the same steps above. **pip install -U pip setuptools wheel** **python -m spacy download en_core_web_sm**


3. You will need to import CSV to read in csv type files as well as pass the encoding through encoding='utf-8' not just regular file path. 


4. Make sure your file path is correct this is an example (file_path = 'C:/Users/your-PC-username/Classcode/chat.csv')
 
5.  **To run the code simply  hit run Python file**


5. To run independently you will need to make a different script/file containting the path and calling the function **csv_extractor** and remove line 45-48
* * * 
# Install and Run Instructions for Chatlog_Extractor (Chat.txt)
### Summary - This is still a chat extractor but for txt files instead of CSV
1. Again we will need spaCy follow the above instructions

2. Make sure the file path is correct this is an example **file_path = 'C:/Users/your-PC-username/Classcode/chat2.txt'**

3. File type should match function call .txt



* * *
# Code
### Line 13-17 (Twtich_chat_IRC) Put your username or bot name here along with OAuth
```Python
class TwitchChatIRC():
	__HOST = 'irc.chat.twitch.tv'
    # put your username or bot name here
	__DEFAULT_NICK = 'Blackshadow_Blouin'
    #your generated password oAuth here
	__DEFAULT_PASS = 'OAuth Password'
	__PORT = 6667
```
### Line 75-77 (Twtich_chat_IRC) This is where buffer size can be changed according to your needs, mine was set high because of such high trafic kept causing a crash. (obtained about 1080 messages within three minutes) **Important so buffer overflow doesn't happen**

```Python
def listen(self, channel_name, messages = [], timeout=None, message_timeout=1.0, on_message = None, buffer_size = 16384 , message_limit = None, output=None):
		self.__join_channel(channel_name)
		self.__SOCKET.settimeout(message_timeout)
```

```Python
# Terminal command to run the script
python twitch_chat_irc.py <channel_name> -output <file_name>
```
### Line 45-48 (chatlog_extractor.CSV) This is just an if statement to call into terminal "main". Argument must be stated make sure the argument is for the row you want on the CSV file. Also path must be correct
```Python
if __name__ == '__main__':
    file_path = 'C:/Users/bloui/Classcode/chat.csv'
    #change the arguemnt for CSV path 'message' can be changed to other categories
    csv_extractor(file_path, 'message')
```
### Line 42-44 (chatlog_extractor.txt) An if statement to call into terminal "main" file type should match .txt and no need for argument for rows.
```Python
if __name__ == '__main__':
    file_path = 'C:/Users/bloui/Classcode/chat2.txt' # file type should match function call .txt
    chatlog_extractor(file_path)

```

*** 
# Outlook
This was a really fun project to do, was a lot of work with trial and error. This could easily extend to what I had imagined. The learning curve for me was realizing that beautiful soup was not going to work for twitch chat after passing the twitch website through and the chat did not appear. After some research, I came across documentation on twitch chat and using an IRC to connect through a user or create a bot to the website to log the messages. I then created a chat log extractor to take the data obtained from the twitch IRC, which I used spaCy to sort the messages and could easily change the code to instead of looking for verbs and nouns, to look for profanity. I could even set up spaCy to sort through the data looking for special characters someone might be using to bypass profanity filters. I would say that this project was a success and does what my goal was in the midterm project future statement. Another thing to note is the data obtained could also be useful in not only just a profanity filter, but could also see how many subscribers participate in chat and just give overall statistics to streamers.