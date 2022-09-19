# ☕Coffee & Work Cafe rating Website using Bootstrap & Flask, WTForms of Python.

🌟Want to work in a cafe? Here's a website which provides a collection of cafes with data related like coffee rating, wifi strength & power plug availability so 
that next time you visit a cafe you can work as well as enjoy your coffee.

🌟Built the website's front-end using HTML, CSS and Bootstrap framework. The back-end is mainly built using Flask framework. The server for testing and validating website
is run with Flask server. Also, extra functionality is added to the website using extensions like Flask-WTForms for creating forms, Flask-Bootstrap for responsiveness &
Jinja for templating a constant design language across the website.

👇Here's a quick look at the final Website👇

![Coffee Wifi Website](https://github.com/bellaryyash23/Coffee_Wifi_Flask/blob/master/samples/site.gif?raw=true)

👆Coffee & Wifi website👆

👉In the 'main.py' file, first the Flask app is set up and the various routes of the website are setup using Flask decorator functions. 

👉The home page is rendered at the home route from the 'index.html' file using the '.render_template()' method. This webpage is designed using the custom styles.css file
and along with that from the inherited bootstrap template using Jinja templating.

![Coffee Wifi Website Home Page](https://github.com/bellaryyash23/Coffee_Wifi_Flask/blob/master/samples/home.jpg?raw=true)

👆Home Page of the Website👆

👉On the home page there is a button which directs the user to the page which contains the list of cafes and all the data related to the reespective cafes. This data is 
acquired from the 'cafe-data.csv' file in the 'main.py' file using the csv reader & writer package. 

👉The csv file contains all the data of the cafes. To render this data in the cafes route, we need to read the data from this file. This is done in the 'cafes' route and this
read data is stored in a list and gets passed to the 'cafes.html' file during the render method call.

👉In the cafe.html file, use of Bootstrap table is done to format this received data and rendered using the Jinja python script templating methods.

![List of Cafes webpage](https://github.com/bellaryyash23/Coffee_Wifi_Flask/blob/master/samples/cafe.jpg?raw=true)

👆Cafe Data list Webpage of Website👆

👉Now, there is a secret route '/add' where we can add new cafe details to the list of existing cafes. On this route the use of WTForms is done to send and receive data
from the form response. Using the WTForms first, the form class is created in the main.py file. This is designed using all the methods which wtforms provides which makes
these forms simple & have added functionaliy compared to regular HTML forms.

👉This form object is passed to the 'add.html' file to render is secret webpage. The magic of WTForms and Bootstrap is that, we can create this form with all the styling
and design with just one line '{{ wtf.quick_form(form) }}' thats it so simple.

👉The data passed by the POST request from this form is caught in the main.py file and now uisng csv writer this data is appended to the already exisitng data of cafes.

![Secret Add route](https://github.com/bellaryyash23/Coffee_Wifi_Flask/blob/master/samples/add.jpg?raw=true)

👆Secret Route to Add new cafe👆
