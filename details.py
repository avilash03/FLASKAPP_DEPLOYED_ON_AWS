def abc(n):
 import imdb
 from imdb import IMDb, IMDbError
 try:
    listn=[]
    ia = imdb.IMDb()
    a=str(n)
    movies = ia.search_movie(a)
    a=movies[0]['title']
    
    b=movies[0]['year']
    
    c=movies[0]['full-size cover url']
    
    
    
    l=movies[0].movieID
    movie = ia.get_movie(l)
    d=movie.get('plot')[0].partition(':')[0]
    
    e=movie.get('plot')[1].partition(':')[0]
    
    listn.append(a)
    listn.append(b)
    listn.append(c)
    listn.append(d)
    listn.append(e)
    return listn

 except IMDbError as m:
    print(m)


