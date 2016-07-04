import requests
from bs4 import BeautifulSoup
import re
import operator
file_links = open( 'links.txt', 'w' )
dictionar = { }
def function ( number_of_pages ):
    page_number = 0
    while page_number < number_of_pages:
        url = "http://www.infoarena.ro/arhiva?display_entries=50&first_entry=" + str( page_number * 50 )
        source_code = requests.get( url )
        plain_text = source_code.text
        soup = BeautifulSoup( plain_text )
        for link in soup.findAll( 'tr', { 'class':re.compile("odd|even")  } ):
            task = link.find( 'td', { 'class':'task' } ) # aici avem linkul  problemei
            task_link = task.find( 'a' )  # aici avem linkul problemei
            href = "http://www.infoarena.ro" + task_link.get('href')

            rating = link.find( 'td', { 'class':'rating' } ) # aici avem ratingul pe care urmeaza sa il evaluam

            if rating.find( 'div', { 'class':'hidden'}) is not None :
                rating2 = rating.find( 'div', { 'class':'hidden'} )
                value = rating2.string
                dictionar.update( { href:value[0] } )
            else :
                dictionar.update( { href:'0'})
        page_number += 1

function( 36 )
sdict = sorted( dictionar.items(), key = operator.itemgetter(1) )
for number, letter in sdict:
    file_links.write("\n".join(["%s %s" % (number, letter)]) + "\n")
file_links.close()
