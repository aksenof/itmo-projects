<b> Задание: </b> 

В качестве практического примера применения интеллектуального анализа web-данных рассмотреть следующую задачу: «Составить топ жанров фильмов, представленных в топ 250 фильмов по версии IMDb»

<b> Решение: </b> 

В качестве языка программирования был выбран язык Python версии 3.7. Для извлечения и управления данными в базе данных фильмов IMDb был использован API: IMDbPY (for Python).  
__________

install api imdb: pip install imdbpy
__________ 

<b> Описание программы: </b>

Был реализован алгоритм, благодаря которому составляется список жанров – от самого распространённого жанра до самого малоизвестного. Суть алгоритма заключается в следующем: программа обрабатывает каждый фильм и, в заранее созданный список, заносит жанры данного фильма. После обработки всех фильмов в полученном списке суммируется количество одинаковых жанров. Далее осуществляется сортировка от самой большой суммы – до самой маленькой. Затем происходит печать полученных результатов.  

Также, в программе есть возможность указать количество фильмов из топ250 фильмов для составления топа жанров. Отсчёт ведётся с первого места в топ250. Например, если указать число 5, то будет топ жанров первых 5 фильмов из топ250. Однако для поставленной задачи требуются все 250 фильмов. Следовательно, укажем программе число 250. 

<b> Результат прогона программы: </b>

start 

Enter number of films from top250 IMDb: 250 

1 The Shawshank Redemption ['Drama'] 

...

250 Fanny and Alexander ['Drama'] 

rating: 

1 ['Drama', 182] 

2 ['Thriller', 61] 

3 ['Adventure', 56] 

4 ['Crime', 54] 

5 ['Comedy', 46] 

6 ['Mystery', 36] 

7 ['Action', 34] 

8 ['Fantasy', 33] 

9 ['Sci-Fi', 30] 

10 ['War', 29] 

11 ['Romance', 29] 

12 ['Family', 25] 

13 ['Biography', 24] 

14 ['Animation', 20] 

15 ['History', 17] 

16 ['Western', 8] 

17 ['Sport', 6] 

18 ['Musical', 5] 

19 ['Music', 5] 

20 ['Horror', 5] 

21 ['Film-Noir', 4] 

end 

__________

<b> Вывод: </b>

Таким образом, на сайте IMDb самый распространённый жанр фильмов – это Drama (182 фильма из 250), а самый нераспространённый – Film-Noir (4 фильма из 250). 
