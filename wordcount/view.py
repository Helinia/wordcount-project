from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split() #split the string into list of words

    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            #add to the counter
            word_dictionary[word] += 1

        else:
            #create new element in dictionary and set counter to 1
            word_dictionary[word] = 1


    sorted_words = sorted(word_dictionary.items(),key = operator.itemgetter(1), reverse = True)

    #render() takes the request and shows the user of whatever is in count.html
    #The dictionary (third argument) contains parameters obtained from
    #the last web page and are also pass to count.html to be used

    #note: cannot pass a dictionary inside a dictionary to html!
    #word_dictionary is passed to html as a list
    #the method items() returns a list of dict's (key,value) tuple pairs
    return render(request,'count.html',{'fulltext': fulltext,'count':len(wordlist),'sorted_words':sorted_words})



def about(request):
    return render(request,"about.html")
