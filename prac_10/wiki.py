import wikipedia

try:
    search = input("Search: ")
    while search != '':
        web_page = wikipedia.page(search)
        print("\t-{}-\n{}\nVisit page at {}".format(web_page.title, web_page.summary, web_page.url))
        search = input("Search: ")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
