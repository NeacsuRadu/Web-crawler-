import requests
from bs4 import BeautifulSoup

file_links = open( 'links.txt', 'w' )


def function ( number_of_pages ):
    page_number = 0
    while page_number < number_of_pages:
        url = "http://www.infoarena.ro/arhiva?display_entries=50&first_entry=" + str( page_number * 50 )
        source_code = requests.get( url )
        plain_text = source_code.text
        soup = BeautifulSoup( plain_text )
        for link in soup.findAll( 'td', { 'class':'task'} ):
            href = "http://www.infoarena.ro" + link.find('a').get('href')
            file_links.write( href + '\n' )
        page_number += 1
function( 36 )