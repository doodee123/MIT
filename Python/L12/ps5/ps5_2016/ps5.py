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
def clean_the_text(text):
    newText = []
    text = text.lower()
    #text = " ".join(str(x) for x in text)
    for punc in string.punctuation:
        text = text.replace(punc, " ")
    text = text.split(" ")
    for x in text:
        if x != "":
            newText.append(x)
        if '' in text:
            text.remove('')

    return newText


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
       
    def is_phrase_in(self, text):
        splitText = clean_the_text(text)
        splitPhrase = clean_the_text(self.phrase)
   
        for t in splitText:
            ti = splitText.index(t)
            if t == splitPhrase[0]:
                valid_order = True
                for x in range(len(splitPhrase)):
                    if len(splitPhrase) > len(splitText) - ti:
                        return False                    
                    elif splitText[ti + x] != splitPhrase[x]:
                        valid_order = False
                        break
                if valid_order:
                    return True
               
        return False

            


# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        if self.is_phrase_in(story.get_description()) == False:
            return False
        else:
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
    triggeredStories = []
    
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                triggeredStories.append(story)
    return triggeredStories



#======================
# User-Specified Triggers
#======================
# Problem 11
def sort_triggers(t):
    triggerlist = []
    temp_ADD = []
    temp_T = {}

    for title,trigger in t.items():
        if title == 'ADD':
            temp_ADD.extend(trigger)
        if trigger[0] == 'TITLE':
            temp_T[title] = TitleTrigger(trigger[1])
        elif trigger[0] == 'DESCRIPTION':
            temp_T[title] = DescriptionTrigger(trigger[1])
        elif trigger[0] == 'AND':
            temp_T[title] = AndTrigger(trigger[1],trigger[2])
        elif trigger[0] == 'OR':
            temp_T[title] = OrTrigger(trigger[1],trigger[2])
        elif trigger[0] == 'NOT':
            temp_T[title] = NotTrigger(trigger[1],trigger[2])
        elif trigger[0] == 'AFTER':
            temp_T[title] = AfterTrigger(trigger[1])
        elif trigger[0] == 'Before':
            temp_T[title] = BeforeTrigger(trigger[1])
    for each in temp_ADD:
        triggerlist.append(temp_T[each])
    #print(triggerlist is None)
    return triggerlist

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

    #print(lines) # for now, print it so you see what it contains!
    triggers = {}
    for entry in lines:
        splitEntry = entry.split(",")
        splitLength = len(splitEntry)
        if splitLength == 3:
            triggers[splitEntry[0]]=[splitEntry[1],splitEntry[2]]
        if splitLength == 4:
            triggers[splitEntry[0]]=[splitEntry[1],splitEntry[2],splitEntry[3]]
 
    return sort_triggers(triggers)

SLEEPTIME = 240 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
##        t1 = TitleTrigger("Trump")
##        t2 = DescriptionTrigger("Italy")
##        t3 = DescriptionTrigger("Brexit")
##        t4 = OrTrigger(t2, t3)
##        #t4 = NotTrigger(t2)
##        triggerlist = [t1,t3]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        
        triggerlist = read_trigger_config('triggers.txt')
        
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

