# Steps to run dockerfile

Inside the Sql_project folder run ,

`docker buildx build -t yuji/sql_injection:latest .`

modify the name , container_name and tag as per your preference.

Run `docker run -p 5000:5000 yuji/sql_injection` after the containerization is complete.


