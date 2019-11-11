# Angel's Blog

## How to view blog
- Go into the blog folder and run `python manage.py runserver` to run the server and go to `http://localhost:8000/` to view the blog
- Routes:
    - `/` the about me/splash page
    - `/blog/` page with all blog posts
    - `/post/<title>` single blog post view that shows the post with title `<title>`
    - `/author/<author name>` page with all posts written by `<author name>`

## How to add posts
- after starting the server, go to `/admin/`
- Username: admin
- Password: password
- Then you can click on the "Post" model and add a new entry

## Additional Features
- Clicking on the author's name leads you to `/author/<author name>` which will show all of that author's posts
- Pretty bootstrap; I figured out how to add a static folder to Django