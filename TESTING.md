# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Lighthouse Testing](#lighthouse-testing)
    - [Desktop](#desktop)
    - [Mobile](#mobile)
  - [WAVE Accessibility Testing](#wave-accessibility-testing)
  - [Code Validation](#code-validation)
    - [HTML Validation](#html-validation)
      - [Landing page](#landing-page)
      - [Menu page](#menu-page)
      - [Cats page](#cats-page)
      - [Cat application pages](#cat-application-pages)
      - [Login, Logout, and Register pages](#login-logout-and-register-pages)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
      - [Pawse Project](#pawse-project)
      - [Pages App](#pages-app)
      - [Menu App](#menu-app)
      - [Cats App](#cats-app)
  - [Automated Testing](#automated-testing)
    - [Running the Automated Tests](#running-the-automated-tests)
  - [Manual Testing](#manual-testing)
    - [UX Testing](#ux-testing)
    - [Responsiveness Testing](#responsiveness-testing)
      - [Developer Tools Testing](#developer-tools-testing)
      - [Device Testing](#device-testing)
    - [Browser Compatibility Testing](#browser-compatibility-testing)
    - [User Story Testing](#user-story-testing)
  - [Bugs](#bugs)
    - [Unresolved Bugs](#unresolved-bugs)
    - [Fixed Bugs](#fixed-bugs)

## Lighthouse Testing

All pages of the website were tested using the [Lighthouse tool](https://developer.chrome.com/docs/lighthouse/overview/) in Chrome Developer Tools. The testing was done in an incognito browser for best performance. 

Both mobile and desktop performance was checked. The goal was to score 100 on Accessibility, Best Practices, and SEO, and to have high scores for Performance where possible. 
For some pages, the score for SEO went down to 97/98 on mobile, which was due to insufficient spacing around the Social Media links in the footer. Since this did not persist for all pages and it wasn't an issue on the desktop at all, I did not fix it.

Initial Lighthouse runs showed a few issues with color contrasts and wrong headers, as well as one TypeError caused by Bootstrap on the alert message in my custom JavaScript. All of these issues were fixed and subsequent runs of Lighthouse showed high scores as expected. 

### Desktop

Landing Page:

![Landing Page](docs/lighthouse-validation/landing-desktop.png)

Menu Page:

![Menu Page](docs/lighthouse-validation/menu-desktop.png)

Cats Page:

- Unauthenticated:

![Cats Page Unauthenticated](docs/lighthouse-validation/cats-desktop-u.png)

- Authenticated:

![Cats Page Authenticated](docs/lighthouse-validation/cats-desktop-a.png)

Application Pages:

- Create Application:

![Create Application](docs/lighthouse-validation/application-desktop.png)

- Edit Application:

![Edit Application](docs/lighthouse-validation/application-edit-desktop.png)

- Delete Application:

![Delete Application](docs/lighthouse-validation/application-delete-desktop.png)

Account Pages:

- Register

![Register](docs/lighthouse-validation/register-desktop.png)

- Login

![Login](docs/lighthouse-validation/login-desktop.png)

- Logout

![Logout](docs/lighthouse-validation/logout-desktop.png)

### Mobile

Landing Page:

![Landing Page](docs/lighthouse-validation/landing-mobile.png)

Menu Page:

![Menu Page](docs/lighthouse-validation/menu-mobile.png)

Cats Page:

- Unauthenticated:

![Cats Page Unauthenticated](docs/lighthouse-validation/cats-mobile-u.png)

- Authenticated:

![Cats Page Authenticated](docs/lighthouse-validation/cats-mobile-a.png)

Application Pages:

- Create Application:

![Create Application](docs/lighthouse-validation/application-mobile.png)

- Edit Application:

![Edit Application](docs/lighthouse-validation/application-edit-mobile.png)

- Delete Application:

![Delete Application](docs/lighthouse-validation/application-delete-mobile.png)

Account Pages:

- Register

![Register](docs/lighthouse-validation/register-mobile.png)

- Login

![Login](docs/lighthouse-validation/login-mobile.png)

- Logout

![Logout](docs/lighthouse-validation/logout-mobile.png)

## WAVE Accessibility Testing

The site was tested using the [WAVE web accessibility evaluation tool](https://wave.webaim.org/). 

The result showed no errors. One of the two alerts is for a redundant link (the Pawse logo leading to the landing page, as well as the Pawse text leading to the landing page right next to it). The other alert points out the HTML5 video on the landing page.

![WAVE results](docs/wave-validation.png)

## Code Validation

### HTML Validation

All pages were checked with the [W3 HTML checker](https://validator.w3.org/nu/). 
Since parts of the pages are generated server-side, the pages were checked using the deployed version on Heroku, using the option to "View Page Source" in Chrome and inputting the source code for each page separately into the text input on the W3 Checker. 

At first, several pages had a couple of errors and warnings, but all errors and warnings were fixed until the checker showed none for every page as seen in the below image:

![HTML validation](docs/html-validation.png)

#### Landing page
The landing page showed an error with a missing div end tag. The tag was identified and added. 
It also showed the error that the width for the iframe with the embedded map was set to a percentage instead of an absolute number. This was fixed by moving the style information to the stylesheet instead.

#### Menu page
The menu page showed an error with a wrong header end tag. It had an h5 end tag, but the header was an h4. The end tag was fixed accordingly. 
It also showed an error with the p end tag which could not be correctly matched to the p tag with the class of card-text. This was fixed by changing the tag into a div, which is more appropriate anyway.

#### Cats page
The cats page showed several errors. It showed an error that an element must not appear as a descendant of a button element, which appeared five times on the generated cat cards. This was fixed by adding the button classes directly to the a tag instead and removing the button tags altogether. 
It also showed errors with some div end tags missing and too much, which was fixed by identifying all divs and checking that they had the appropriate end tags.
Lastly, it showed a warning that the application section didn't contain a header. I am not sure why it showed this, because it does contain an h4, just not as a direct child. Either way, this was fixed by changing the section into a div. 

#### Cat application pages
None of the cat application pages showed errors or warnings. 

#### Login, Logout, and Register pages

These all showed the same warning that the trailing slash on self-closing tags does not have any effect. The trailing slash was removed on all pages. 

### CSS Validation

CSS was validated using the [Jigsaw validator from W3C](https://jigsaw.w3.org/css-validator/validator). No errors were found.

![CSS validation](docs/css-validation.png)

### JavaScript Validation

The custom JavaScript was validated using [JSHint](https://jshint.com/) which showed no errors. 

![JS validation](docs/js-validation.png)

### Python Validation

The CI Python Linter was used to validate the Python files created or edited for the Django project. Unchanged project files and settings.py were not validated.

No errors came up for any of the files. Click on the links below to see screenshots of the results. 

#### Pawse Project

- [urls.py](docs/python-validation/pawse-urls.png)

#### Pages App

- [test_views.py](docs/python-validation/pages-test-views.png)
- [urls.py](docs/python-validation/pages-urls.png)
- [views.py](docs/python-validation/pages-views.png)

admin.py and models.py were not used.

#### Menu App

- [admin.py](docs/python-validation/menu-admin.png)
- [models.py](docs/python-validation/menu-models.png)
- [test_models.py](docs/python-validation/menu-test-models.png)
- [test_views.py](docs/python-validation/menu-test-views.png)
- [urls.py](docs/python-validation/menu-urls.png)
- [views.py](docs/python-validation/menu-views.png)

#### Cats App

- [admin.py](docs/python-validation/cats-admin.png)
- [models.py](docs/python-validation/cats-models.png)
- [test_models.py](docs/python-validation/cats-test-models.png)
- [test_views.py](docs/python-validation/cats-test-views.png)
- [urls.py](docs/python-validation/cats-urls.png)
- [views.py](docs/python-validation/cats-views.png)

On urls.py the `noqa` tag was used on the line importing the views since I deemed it less readable if I split this up into several lines.

## Automated Testing

Unit tests were written for all three apps (pages, menu, and cats) to ensure that no bugs were missed. 

Almost all statements were tested with few exceptions.

The test coverage for the apps is as follows:

![Test Coverage](docs/coverage.png)

### Running the Automated Tests

To run the automated tests, you need to adjust your DATABASES in settings.py in the following way: 

```python
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```

You also need to make sure to set DEBUG to 'DEBUG' in env.py. This needs to be done because the test suite needs to create a mock database in sqlite3 for the tests.

Then you can open a terminal and type `python3 manage.py test` and it will run all tests, or you can specify which tests you want to run. 

## Manual Testing

While manual testing tends to take up a lot of time compared to automated testing, the site also underwent a comprehensive suite of manual testing to ensure that it works as expected.

One big advantage of manual testing is that one can test the actual User Experience of the site, which cannot be tested using automated tests since it is somewhat subjective how a user judges the experience. 

Additionally, the manual testing approach ensures an end-to-end integrated testing of the application features and the actual database instead of testing single code statements.

### UX Testing

The site was shared with friends and family during different stages of development and feedback was collected and implemented continuously. 

Examples of feedback that came up during UX testing: 

- The hero image on the home page felt not engaging enough and it was suggested to have something moving, which led to the image being replaced by a video
  - This also led to the zoom effect on the Cats page being implemented, to make it more dynamic
- The login, register, and logout were tested by most users and deemed very intuitive and easy, as well as functional
- The site was judged to be navigated easily
- The design was judged to be pleasant

### Responsiveness Testing

The site was tested continuously on different screen sizes using both Chrome Developer Tools, as well as mobile devices. 

Sometimes, the landing page would show a margin on the right side on mobile devices, both in Chrome Developer Tools as well as on actual devices. This was not consistently reproducible and happened on different kinds of devices and the root cause for it happening remains unknown. Usually, reloading the page would fix this. 
Since this was not reproducible and happened across all devices, I did not put it down as an issue of the testing itself. 

The page was tested in the following way on all devices listed below:

- Navigated to every page using the nav bar/hamburger menu
- Scrolled over every page and checked that all parts are rendered correctly
- Logged in/logged out of the page on every device
- Checked that logging in/out redirects to the previous page
- Clicked on buttons on the cat page to create/edit/delete applications
- Created/edited/deleted applications
- Checked that alert messages show up correctly and disappear automatically
- Checked that form validation works
- Checked that autoplay on the hero video works
- Checked that the zoom on the Cats page works

#### Developer Tools Testing

iPhone 5/SE: All features tested, no issues

iPhone 12 Pro: All features tested, no issues

Samsung Galaxy S8+: All features tested, no issues

iPad Air: All features tested, no issues

#### Device Testing

iPhone 12 Pro: All features tested, no issues

iPhone 14 Pro: All features tested, no issues

iPad mini: All features tested, no issues

### Browser Compatibility Testing

Browser compatibility testing was done on the desktop only. 

The page was tested in the following way on all browsers listed below:

- Navigated to every page using the nav bar/hamburger menu
- Scrolled over every page and checked that all parts are rendered correctly
- Logged in/logged out of the page on every device
- Checked that logging in/out redirects to the previous page
- Clicked on buttons on the cat page to create/edit/delete applications
- Created/edited/deleted applications
- Checked that alert messages show up correctly and disappear automatically
- Checked that form validation works
- Checked that the hover effect on links works
- Checked that autoplay on the hero video works
- Checked that zoom on the Cats page works

Browsers:

- Chrome: All features tested, no issues
- Safari: All features tested, no issues
- Firefox: All features tested, no issues
- Edge: All features tested, no issues

### User Story Testing

| **Epic**                               | **User Story**                                                                                                                        | Testing Method & Expected Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Result                                                                                     | Comment                                                                                                             |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Unauthenticated User Features          | As a user, I want to see a navigation menu so that I can easily navigate to the desired content                                       | 1. Navigating to the website on a desktop/laptop and seeing a navigation bar with navigation elements<br>1a. When hovering over the links, they should be highlighted as feedback to the user of being clickable<br>1b. When clicking on a link, the user should be taken to the linked page<br>1c. The active page should be highlighted in the nav bar<br>2. Navigating to the website on a mobile device and seeing a hamburger menu<br>2a. When clicking on the hamburger menu, the nav bar should open and show all links<br>2b. When clicking on a link, the user should be taken to the linked page<br>2c. The active page should be highlighted when the hamburger menu is open | 1. Pass<br>1a. Pass<br>1b. Pass<br>1c. Pass<br>2. Pass<br>2a. Pass<br>2b. Pass<br>2c. Pass |                                                                                                                     |
|                                        | As a user, I want to see an inviting landing page so that I know what the page is about and what I can do                             | 1. When navigating to the website, a hero image or hero video should be shown to the user that sets the topic of the site<br>2. There should be a short description for the user about what the page is about<br>3. The links in the nav bar should be self-explanatory                                                                                                                                                                                                                                                                                                                                                                                                                 | 1. Pass<br>2. Pass<br>3. Pass                                                              |                                                                                                                     |
|                                        | As a user, I want to see all menu options of the cafe so that I can make an informed decision if I want to visit                      | 1. When navigating to the Menu page, the user should see all choices<br>2. The choices should be sorted by category<br>3. The choices should include proper descriptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 1. Pass<br>2. Pass<br>3. Pass                                                              |                                                                                                                     |
|                                        | As a user, I want to see the cats living in the cafe so that I can familiarize myself with them before my visit               | 1. When navigating to the Cats page, the user should see images of all the cats<br>2. The cats should also have a description so the user knows a bit about them if wanted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1. Pass<br>2. Pass                                                                         |                                                                                                                     |
|                                        | As a user, I want to see whether there are already people interested in the cats so that I can choose one accordingly                 | 1. When navigating to the Cats page, the user should see the current number of applications for any cat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1. Pass                                                                                    |                                                                                                                     |
|                                        | As a user, I want to be able to register to the site so that I get access functionality for authenticated users on the site           | 1. Navigating the website, the user should have access to a link to register from any page in the nav bar<br>2. When clicking on Register, the user should be taken to a form that asks for username, password, and repetition of password<br>3. After registering, the user should be logged in automatically                                                                                                                                                                                                                                                                                                                                                                           | 1. Pass<br>2. Pass<br>3. Pass                                                              |                                                                                                                     |
|                                        | As a user, I want to be able to log in so I can access my account                                                                      | 1. Navigating the website, the user should have access to a link to log in from any page in the nav bar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1. Pass                                                                                    |                                                                                                                     |
|                                        | As a user, I want to have easy access to the social media accounts of the cafe so that I can engage with the owners and other customers   | 1. Navigating the website, the user should be able to find the social media links of the cafe at any point<br>2. The social media navigation links should behave the same as the main nav bar when hovering over the links<br>3. Clicking on a social media link should open the page in a new tab                                                                                                                                                                                                                                                                                                                                                                                      | 1. Pass<br>2. Pass<br>3. Pass                                                              |                                                                                                                     |
| Authenticated User Features            | As an authenticated user, I want to be able to log out of my account so that my account is secure from other users on the same device | 1. When logged in, the logout link should be accessible from any page in the nav bar<br>2. When clicking on logout, the user should be prompted to confirm the action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. Pass<br>2. Pass                                                                         |                                                                                                                     |
|                                        | As an authenticated user, I want to be able to delete my account so that I can forget about the page                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                            | This user story was not implemented                                                                                 |
|                                        | As an authenticated user, I want to be able to voice my interest in one of the cats so that I can adopt it                            | 1. When logged in, navigate to the cats page and click on an adopt button on a cat<br>2. Fill in the form and click the Submit button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. Pass<br>2. Pass                                                                         |                                                                                                                     |
|                                        | As an authenticated user, I want to be able to edit my interest in one of the cats                                                    | 1. When logged in, navigate to the cats page and find your current applications at the bottom of the page<br>2. Click on the edit button on an application<br>3. Edit the text in the form and click the Update button                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1. Pass<br>2. Pass<br>3. Pass                                                              |                                                                                                                     |
|                                        | As an authenticated user, I want to be able to delete my interest in one of the cats                                                  | 1. When logged in, navigate to the cats page and find your current applications at the bottom of the page<br>2. Click on the delete button on an application<br>3. Click the Confirm button                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 1. Pass<br>2. Pass<br>3. Pass                                                              |                                                                                                                     |
| Site Admin Features                    | As a site admin, I want to be able to log in to my admin account so that I can make changes to the content on the site                | 1. Navigate to the page and add /admin to the end of the url<br>2. Login with superuser credentials<br><br>4. Test adding/editing/deleting cats<br>5. Test adding/editing/deleting cat applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 1. Pass<br>2. Pass                                                                         | The functionality was deemed not a priority to add in the UI since everything is possible through the Admin portal |
|                                        | As a site admin, I want to be able to adjust the menu from the front end so that it is always up to date                               | 1. When logged in to the admin portal<br>2. Test CRUD functions for menu category/items                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1. Pass<br>2. Pass                                                                         |                                                                                                                     |
|                                        | - As a site admin, I want to be able to add new menu items from the front end | 1. Test adding menu categories/items                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1. Pass                                                                                    |                                                                                                                     |
|                                        | - As a site admin, I want to be able to edit menu items from the front end | 1. Test editing menu categories/items                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. Pass                                                                                    |                                                                                                                     |
|                                        | - As a site admin, I want to be able to delete menu items from the front end | 1. Test deleting menu categories/items                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1. Pass                                                                                    |                                                                                                                     |
|                                        | As a site admin, I want to be able to adjust the kittens from the front end so that customers always see the current kittens           | 1. When logged in to the admin portal<br>2. Test CRUD functions for cats/cat applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1. Pass<br>2. Pass                                                                         |                                                                                                                     |
|                                        | - As a site admin, I want to be able to add new cats from the front | 1. Test adding cats/cat applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1. Pass                                                                                    |                                                                                                                     |
|                                        | - As a site admin, I want to be able to edit cats from the front end | 1. Test editing cats/cat applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1. Pass                                                                                    |                                                                                                                     |
|                                        | - As a site admin, I want to be able to delete cats from the front | 1. Test deleting cats/cat applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1. Pass                                                                                    |                                                                                                                     |
| Authenticated User/Site Admin Features | As an authenticated user/site admin I want to see feedback from my actions so that I know my action was successful                    | 1. Check that appropriate feedback comes up after submission/updating/deleting in the form of a message at the top of the screen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1. Pass                                                                                    |                                                                                                                     |
|                                        | As an authenticated user/site admin I want to be asked to confirm deletion so that I don't accidentally delete something wrong        | 1. Check that when deleting an application, the confirmation page comes up                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 1. Pass                                                                                    |                                                                                                                     |
| Site Owner Features                    | As a site owner, I want the site to be visually pleasing so that users like to come back/share it                                     | 1. Check all pages for a consistent and pleasant look, and gather feedback from friends/family on the design                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 1. Pass                                                                                    |                                                                                                                     |

## Bugs

### Unresolved Bugs

- As mentioned above in the [Responsiveness Testing](#responsiveness-testing) section, sometimes when the landing page loads, it displays an empty margin on the right side. I was not able to find the root cause for this since the issue was not dependably reproducible. It also fixed itself by reloading the page.

### Fixed Bugs

- When a user clicked on the button to adopt a cat while not logged in, then logged in, they were able to send a second application for the same cat. This could also be done by manually changing the name of the cat on the URL of the application page. 
  - Fix: I fixed this by adding validation in the view in the form_valid() method to check if the user already has an application for that cat
- The footer items did not align properly on small screen sizes
  - Fix: The flexbox settings were adjusted for small screen sizes to center the items on small screens while keeping the space between on larger screens
