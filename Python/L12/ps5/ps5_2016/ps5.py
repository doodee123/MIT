# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz



#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate



#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def is_phrase_in(self, text):
        phrase = self.phrase.lower()
        text = text.lower()
        #print('text is ', text)

        for punc in string.punctuation:
            text = text.replace(punc, " ")
        splittext = text.split(" ")

        newText = []
        for x in splittext:
            if x != "":
                newText.append(x)
        splittext = newText
            
        print("Minus the spaces and we get ", splittext)
        
        if '' in phrase:
            phrase = phrase.strip()

        #if '' in splittext:
            #phrase = splittext.strip()
            
        test = []
        phraseTemp = phrase.split()
        for word in phraseTemp:
            print('The word is', word)
            print('splittext is ,',splittext)
            print('phrasetemp is ,',phraseTemp)
            if word in splittext:
                #index = phrase.index(word)
                #print('the length of the ', word, ' is ', len(word))
                #print('the length of the trigger word in phrase is ', len(phrase[index]))
                test.append(word)
            else:
                return False

        if '' in test:
            test.remove('')


        #TriggerBool = False
        
        for word in test:
            #print("testing: ", testPhrase)
            print('test is, ', test)
            index = test.index(word)
            length = len(test)
            print('Word Index is ', index, ' and word is ', test[index])
            for item in splittext:
                itemIndex = splittext.index(item)
                print('Item Index is ', itemIndex, ' and word is ', splittext[itemIndex])
                if word not in splittext:
                    print (word, " not in ", item, 'from splittext')
                    return False
                else:
                    if word in splittext:
                        print("Entering While Loop ", itemIndex+1, " is itemIndex+1 ", len(splittext), " is len(splittext) AND ", index+1, " is index+1 ", len(test), " is len(test)")
                        #print('index+1 is ', index+1, 'index length is ', len(test), ' and itemIndex+1 is ', itemIndex+1, ' and its length is ', len(splittext))
                        while itemIndex+1 < len(splittext) and index+1 < len(test):
                              if word == splittext[itemIndex]:
                                  print("While loop first IF triggered")
                                  if splittext[itemIndex+1] == test[index+1]:
                                      print("first IF inner IF triggered")
                                      print(word, ' is the word and triggers the check if ', splittext[itemIndex+1], '  == ', test[index+1])
                                      return True
                                      #print("test can be found in splittext")
                                  else:
                                      return False
                              elif word == splittext[itemIndex]:
                                  print("While loop ELIF triggered")
                                  if splittext[itemIndex+1] != test[index+1]:
                                      print("ELIF inner IF triggered")
                                      return False
                              else:
                                  print("While loop ELSE triggered")
                                  #return False
                                  break
                                
##                            if word == splittext[itemIndex] and splittext[itemIndex+1] == test[index+1]:
##                                print(word, ' is the word and triggers the check if ', splittext[itemIndex+1], '  == ', test[index+1])
##                                #TriggerBool = True
##                                return True
##                                #break
##                                #print("test can be found in splittext")
##                            elif word == splittext[itemIndex] and splittext[itemIndex+1] != test[index+1]:
##                                print("while loops elif triggered")
##                                return False
##                            else:
##                                return False                            
                    else:
                        return False
                        
        #return TriggerBool
        # split the text to match the phrase when it gets triggered? 


# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        #return self.is_phrase_in(story.get_title())
        if self.is_phrase_in(story.get_title()) == False:
            #print("TitleTrigger should be returning False")
            return False
        else:
            #print("TitleTrigger is True")
            return True

#cuddly = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
#separate  = NewsStory('', 'The purple blob over there is a cow.', '', '', datetime.now())
#exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '',  datetime.now())
#symbols   = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
#PhraseTrigger("PURPLE COW").is_phrase_in(cuddly.get_title())
#PhraseTrigger("PURPLE COW").is_phrase_in(separate.get_title())
#PhraseTrigger("PURPLE COW").is_phrase_in(exclaim.get_title())
#PhraseTrigger("PURPLE COW").is_phrase_in(symbols.get_title())
badorder  = NewsStory('', 'Cow!!! Purple!!!', '', '', datetime.now())
PhraseTrigger("PURPLE COW").is_phrase_in(badorder.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
##        return self.is_phrase_in(story.get_description())
        if self.is_phrase_in(story.get_description()) == False:
##            print("DescriptionTrigger should be returning False")
            return False
        else:
##            print("DescriptionTrigger is True")
            return True
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def evaluate(self, story):
        
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

    def __init__(self, date):
        self.date = datetime.strptime(date, "%d %b %Y %H:%M:%S")
        self.date.replace(tzinfo=pytz.timezone("EST"))

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        UTCdate = self.date.replace(tzinfo=pytz.timezone("EST"))
        UTCpubdate = story.pubdate.replace(tzinfo=pytz.timezone("EST"))
        if UTCdate > UTCpubdate:
            #print("IS it true?")
            return True
        else:
            #print ("False?")
            return False

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        UTCdate = self.date.replace(tzinfo=pytz.timezone("EST"))
        UTCpubdate = story.pubdate.replace(tzinfo=pytz.timezone("EST"))
        if UTCdate < UTCpubdate:
            return True
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T

    def evaluate(self, story):
        #return not self.T.evaluate(story)
        if self.T.evaluate(story) == True:
            return False
        else:
            if self.T.evaluate(story) == False:
                return True

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        if self.T1.evaluate(story) == True and self.T2.evaluate(story) == True:
            return True
        else:
            return False

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        if self.T1.evaluate(story) == True or self.T2.evaluate(story) == True:
            return True
        else:
            return False
        

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    #triggeredStories = []
    
    #for story in stories:
        #for trigger in triggerlist:
##            print("============================")
##            print(story.get_title())
##            print(story.get_description())
##            print(trigger.evaluate(story))
##            print("============================")
            #if trigger.evaluate(story) != True:
                #triggeredStories.append(story)
                #pass
            #else:
##                print("============================")
##                print(story.get_title())
##                print(story.get_description())
##                print(trigger.evaluate(story))
                #triggeredStories.append(story)


    #stories = triggeredStories
    #return triggeredStories
    #return stories  



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 240 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Trump")
        t2 = DescriptionTrigger("Italy")
        t3 = DescriptionTrigger("Trump")
        t4 = OrTrigger(t2, t3)
        #t4 = NotTrigger(t2)
        triggerlist = [t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .")
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

