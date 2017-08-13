# -*- coding:utf-8 -*-

query = 'https://en.wikipedia.org/api/rest_v1/page/summary/Douglas_Adams'

response = r"""{"title":"Douglas Adams","displaytitle":"Douglas Adams","pageid":8091,"extract":"Douglas Noel Adams (11 March 1952 – 11 May 2001) was an English author, scriptwriter, essayist, humorist, satirist and dramatist.\nAdams is best known as the author of The Hitchhiker's Guide to the Galaxy, which originated in 1978 as a BBC radio comedy before developing into a \"trilogy\" of five books that sold more than 15 million copies in his lifetime and generated a television series, several stage plays, comics, a computer game, and in 2005 a feature film. Adams's contribution to UK radio is commemorated in The Radio Academy's Hall of Fame.\nAdams also wrote Dirk Gently's Holistic Detective Agency (1987) and The Long Dark Tea-Time of the Soul (1988), and co-wrote The Meaning of Liff (1983), The Deeper Meaning of Liff (1990), Last Chance to See (1990), and three stories for the television series Doctor Who; he also served as script editor for the show's seventeenth season in 1979.","extract_html":"<p><b>Douglas Noel Adams</b> (11 March 1952 – 11 May 2001) was an English author, scriptwriter, essayist, humorist, satirist and dramatist.</p>\n<p>Adams is best known as the author of <i>The Hitchhiker's Guide to the Galaxy</i>, which originated in 1978 as a BBC radio comedy before developing into a \"trilogy\" of five books that sold more than 15 million copies in his lifetime and generated a television series, several stage plays, comics, a computer game, and in 2005 a feature film. Adams's contribution to UK radio is commemorated in The Radio Academy's Hall of Fame.</p>\n<p>Adams also wrote <i>Dirk Gently's Holistic Detective Agency</i> (1987) and <i>The Long Dark Tea-Time of the Soul</i> (1988), and co-wrote <i>The Meaning of Liff</i> (1983), <i>The Deeper Meaning of Liff</i> (1990), <i>Last Chance to See</i> (1990), and three stories for the television series <i>Doctor Who</i>; he also served as script editor for the show's seventeenth season in 1979.","thumbnail":{"source":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Douglas_adams_portrait_cropped.jpg/276px-Douglas_adams_portrait_cropped.jpg","width":276,"height":320,"original":"http://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cropped.jpg"},"originalimage":{"source":"https://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cropped.jpg","width":333,"height":386},"lang":"en","dir":"ltr","timestamp":"2017-08-03T16:37:48Z","description":"English writer and humorist"}"""

info = {'content': 'TEST', 'status': 200}
cache = {'query': query, 'response': response, 'info': info}
