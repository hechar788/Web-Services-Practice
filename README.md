# Web-Services-Project
ARA-BCDE Web services project

Version 1.0
- Initial flask website structure created with basic home and profile page.
- Flask blueprint created in views.py as structure for web app routes
- Basic redirect feature created, will redirect user to home page when /redirect route is visited

The only html template thus far is index.html which is being used as a base for both pages.
Profile page takes name argument from url link to return a name object to the html page.
  eg. 127.0.0.1:8080/profile?name=Hector

Version 1.1
- Profile.html added for profile page construction inherits from index.html
- Updated profile name argument, 'get' method, to return empty string instead of None in unkown name variable case.
