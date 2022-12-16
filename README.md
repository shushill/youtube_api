Youtube API
---


Try It
---

open folder youtubeapi and run the following commands below:

run `docker-compose build` now, <br />
run `docker-compose up -d` now, <br />
run `docker-compose exec web python manage.py makemigrations` now, <br />
run `docker-compose exec web python manage.py migrate` now, <br />

if you want to close the docker container, then run:

run `docker-compose down` now, <br />

The above command will set up all the requirements, will do migrations, indexing in tables.

In the YoutubeAPI go to rooms folder and in the jobs.py, we can insert any query and youtube api will fetch the data from youtube services.
<img width="1438" alt="Screenshot 2022-12-16 at 6 12 40 PM" src="https://user-images.githubusercontent.com/28860154/208100988-118c46fa-b8c7-4f36-8cee-f6c5778dd6b5.png">

And, Please change the Youtube API keys in .env folder inside youtubeapi.




How to run:
---

- First Open http://127.0.0.1:8000/
	- This will start data pulling from youtube in every 10 seconds.
	
	
<img width="1440" alt="Screenshot 2022-12-16 at 6 03 15 PM" src="https://user-images.githubusercontent.com/28860154/208099988-2fb97561-2b34-487a-b01b-34dafdc7141f.png">



Tech Stack Used:
----
	HTML
	CSS
	Django
	Django Rest Framework
	Docker
	Postgresql
	

References:
---


- [https://www.geeksforgeeks.org/youtube-data-api-set-1/](https://www.geeksforgeeks.org/youtube-data-api-set-1/)

- [geeksforgeeks] (https://geeksforgeeks.com/)

- [https://developers.google.com/youtube/v3/docs/search/list]( https://developers.google.com/youtube/v3/docs/search/list)
-  [youtube search api] 

