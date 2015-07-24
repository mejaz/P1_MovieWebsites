
import media
import fresh_tomatoes

#Creating instances of the class Movies, available in the file 'media.py'.
movie1 = media.Movies("Forrest Gump", "images/forrest-gump-poster1.jpg", "https://www.youtube.com/watch?v=uPIEn0M8su0", "Tom Hanks and Gary Sinise")
movie2 = media.Movies("A Wednesday", "images/a_wednesday.jpg", "https://www.youtube.com/watch?v=Mii6TZXPrbQ", "Naseeruddin Shah")
movie3 = media.Movies("The Departed", "images/the_departed.jpg", "https://www.youtube.com/watch?v=auYbpnEwBBg", "Leonardo Decaprio, Matt Damon and Jack Nicholson")
movie4 = media.Movies("Sholay", "images/sholay.jpg", "https://www.youtube.com/watch?v=36SMdfwisLg", "Amitabh Bachchan and Dhamendra")
movie5 = media.Movies("The Incredible Hulk", "images/hulk.jpg", "https://www.youtube.com/watch?v=xbqNb2PFKKA", "Edward Norton and Liv Tyler")
movies = [movie1, movie2, movie3, movie4, movie5]

#Calling function from the file 'fresh_tomatoes.py'
#It takes a list as an arguments
fresh_tomatoes.open_movies_page(movies)