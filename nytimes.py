from requests import *
from bs4 import *

def page_data(url):
	if not url.startswith('https://'):
		url = 'https://' + url
	text = get(url).text
	html = BeautifulSoup(text, "html.parser")
	lines = html.get_text().splitlines()
	output = [x for x in lines if x != '']	
	return str(html)

contents = page_data(input('link:\n'))

def main():
    browseLocal(contents)

def strToFile(text, filename):
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename))

main()
	

