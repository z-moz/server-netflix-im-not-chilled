from requests import api
from rest_framework.response import Response
from rest_framework.views import APIView

# access the film database:
url = 'https://www.whats-on-netflix.com/wp-content/plugins/whats-on-netflix/json/movie.json'
db = api.get(url)
films = db.json()


# retrieve a specific film by its netflix id:
class filter_out_one_film(APIView):
    def get(self, request, id):
        results = list(
            filter(lambda film: film['netflixid'] == str(id), films))
        return Response(results[0])



# returns the whole film db and filters it:
class filter_out_a_list(APIView):
    def get(self, request):

        # filter params:
        search_term = request.GET.get('search_term', None)
        title = request.GET.get('title', None)
        director = request.GET.get('director', None)
        actors = request.GET.get('actors', None)
        language = request.GET.get('language', None) 
        category = request.GET.get('category', None) 
        titlereleased = request.GET.get('titlereleased', None) 
        rating = request.GET.get('rating', None) 

        # sort params: 
        sort_by =  request.GET.get('sort_by', None) 
        reverse = bool(request.GET.get('reverse', False))

        # pagination params:
        res_num_only = bool(request.GET.get('res_num_only', False))
        page_len = int(request.GET.get('page_len', 15))
        page_num = int(request.GET.get('page_num', 1))


        # giant terrible filter block:

        # search_term
        if search_term not in [None, '']:
                a = list(filter(lambda film: search_term.title() in film['title'], films))
                b = list(filter(lambda film: search_term.title() in film['director'], films))
                c = list(filter(lambda film: search_term.title() in film['actors'], films))

                d = a + b + c

                e = list({
                        film['netflixid']: film
                        for film in d
                }.values())
        else:
                e = films
        
        if title not in [None, '']:
                f = list(filter(lambda film: title.title()
                                in film['title'], e))
        else:
                f = e

        if director not in [None, '']:
                g = list(
                    filter(lambda film: director.title() in film['director'], f))
        else:
                g = f

        if actors not in [None, '']:
                h = list(
                    filter(lambda film: actors.title() in film['actors'], g))
        else:
                h = g

        if titlereleased not in [None, '']:
                i = list(
                    filter(lambda film: film['titlereleased'] != '' and film['titlereleased'][0:3] in titlereleased, h))
        else:
                i = h

        if language not in [None, '']:
                print(language.title())
                j = list(filter(lambda film: film['language'] not in [None, ''] and language.title() in film['language'], i)) # finds the swiss german but can't do cumulative

        else:
                j = i

        if category not in [None, '']:
                k = list(
                    filter(lambda film: film['category'] not in [None, ''] and film['category']  in category.title(), j))
        else:
                k = j

        if rating not in [None, '']:
                filtered = list(
                    filter(lambda film: film['rating'] not in [None, ''] and film['rating'] in rating, k))
        else:
                filtered = k

        if not res_num_only: 

                # sort:
                invalid = ["N/A/10"] # anything I came across, how to find these automatically?
                # filter out empty and invalid values in the chosen sorting category:
                if sort_by is not None:

                        sorted = list(
                        filter(lambda film: bool(film[sort_by]) == True and film[sort_by] not in invalid, filtered))

                        # sort and order: 
                        def sortBy(item):
                                return item[sort_by]
                        sorted.sort(reverse=reverse, key=sortBy)
                else:
                        sorted = filtered

                # paginate:
                result = paginate(sorted, page_len, page_num)

        else:
                result = (len(filtered))

        print(len(filtered))
        return Response(result)


# -------------- function definitons: ------------

def paginate(list, page_len, page_num):
        paginated = []

        # indices of first and last item on page:
        idx_start = page_len * (page_num - 1)
        idx_end = page_len * page_num

        # validate idx_start:
        if idx_start > len(list):
                return paginated

        # validate idx_end:
        elif idx_end > len(list):
                idx_end = len(list)

        # get items into list to be shown on page:
        for idx in range(idx_start, idx_end):
                paginated.append(list[idx])

        return paginated


# -------------- code that works but not great: ------------

# # don't need?
# from .serializers import FilmSerializer
# from django.core.paginator import Paginator

# # read all, with pagination (page 1 only for now):
# class FilmView(APIView):
#     def get(self, request):
#         # paginate:
#         p = Paginator(films, 15)
#         page = p.page(120)
# # serialize:
#         results = FilmSerializer(page, many=True).data
#         return Response(results)

# # read all, works but slow, no pagination:
# class FilmView(APIView):
#     def get(self, request):
#         results = FilmSerializer(films, many=True).data
#         return Response(results)

# returns the first film:
# def get_all_films(request):
#     res = films[0]
#     return Response(res)

# returns the whole film db:
# def get_all_films(request):
#     return Response(films)

# # my pagination for json data:
#         page_len = 3
#         page_num = 1
#         results = []
#         idx_start = page_len * (page_num - 1)
#         idx_end = page_len * page_num
#         for idx in range(idx_start, idx_end):
#             results.append(films[idx])
#         return Response(results)


# -------------- the django URL filter attempt: -------------------------- 

# from django.http import QueryDict
# from url_filter.backend.plain import PlainFilterBackend
# from url_filter.filtersets.plain import PlainModelFilterSet



# class FilmFilterSet(PlainModelFilterSet):
#       filter_backend_class = PlainFilterBackend

# class Meta(object):
#         model = {
#                 "title": "",
#                 "type": "",
#                 "titlereleased": "",
#                 "image_landscape": "",
#                 "image_portrait": "",
#                 "rating": "",
#                 "quality": "",
#                 "actors": "",
#                 "director": "",
#                 "category": "",
#                 "imdb": "",
#                 "runtime": "",
#                 "netflixid": "",
#                 "date_released": "",
#                 "description": "",
#                 "language": "",
#                 }


# query = QueryDict(

#         # use:
#         #       capitalise each search word
#         #       ' at beginning and end of string
#         #       & between key value pairs
#         #       = between keys and values
#         #
#         # for these categories use:
#         #       'title__contains=New'
#         #       'director__contains=Tarantino'
#         #       'actors__contains=Keanu'
#         #
#         #       'language__in=Swiss German,Norwegian'
#         #       'category__in=Short,Drama'
#         #       'titlereleased__contains=201' # to narrow down to decade: 201 for 2010-2019, 196 for 1960-1969 etc.
#         #       'rating__in=    '  # rating categories: {'NC-17', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-Y7-FV', 'TV-Y', 'PG-13', 'NR', 'TV-14 ', 'N/A', 'TV-MA', 'PG', 'M', 'PG ', 'TV-14', 'G', 'R'}
#         #
#         # example:
#         #       'type=Movie&titlereleased=2020'

#         )

# fs = FilmFilterSet(data=query, queryset=films)
# filtered_list = fs.filter()

# print(query)
# print(len(filtered_list))

# paginated = paginate(filtered_list, 10, 1)

# e = list({
#         film['category']: film
#         for film in films
# }.values())


# new_dict = dict()
# for obj in films:
#     if obj['category'] not in new_dict:
#         new_dict[obj['category']] = obj['category']

# print(new_dict)

# lang = []
# for obj in films:
#         lang.append(obj['language'])

# print(len(lang))

# new_dict = dict()
# for obj in lang:
#     if obj['language'] not in new_dict:
#         new_dict[obj['language']] = obj['language']


# print(new_dict)

# print(len(lang))
# print(len(new_dict))

