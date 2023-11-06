# Web-Services-Practce
ARA-BCDE Web services practice

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

Version 2.0 (Current)
- Added session functionality for user logins.
- Created logout page which removes user from session and redirects back to login page.
- Updated html templates to be centered with better use of block features and inheritance.
- Added redirection functionality for bad url paths
