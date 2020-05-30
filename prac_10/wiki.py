import wikipedia

search = ' '
while search != '':
    try:
        search = input("Search: ")
        web_page = wikipedia.page(search)
        print(web_page.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)