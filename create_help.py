import json

list_dict = []

term_dict = {'term': 'Any URL-encoded text string. Note: URL encoding replaces spaces with the plus (+) character and all characters except the following are encoded: letters, numbers, periods (.), dashes (-), underscores (_), and asterisks (*).'}

term_country = {}

term_media = {'media':'movie, podcast, music, musicVideo, audiobook, shortFilm, tvShow, software, ebook, all'}

term_entity = {'movie': 'movieArtist, movie', 
               'podcast': 'podcastAuthor, podcast',
               'music':'musicArtist, musicTrack, album, musicVideo, mix, song', 
               'musicvideo':'musicArtist,musicVideo',
               'audiobook':'audiobookAuthor, audiobook',
               'shortfilm':'shortFilmArtist, shortFilm',
               'tvshow':'tvEpisode, tvSeason',
               'software':'software, iPadSoftware, macSoftware',
               'ebook':'ebook',
               'all':'movie, album, allArtist, podcast, musicVideo, mix, audiobook, tvSeason, allTrack'}

term_attribute = {}

term_limit = {}

term_lang = {}

term_version = {}

term_explicit = {}

list_dict.append(term_dict)
list_dict.append(term_country)
list_dict.append(term_media)
list_dict.append(term_entity)
list_dict.append(term_attribute)
list_dict.append(term_limit)
list_dict.append(term_lang)
list_dict.append(term_version)
list_dict.append(term_explicit)

json.dump(list_dict, open('opthelp.txt', 'wb'))
