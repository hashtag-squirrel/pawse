# Pawse - Introduction

![Pawse Responsive image](static/docs/pawse-responsive.png)

Pawse is a full-stack website project for a cat cafe. 

It is a remake of the HTML & CSS only website ["In the Meowment"](https://hashtag-squirrel.github.io/in-the-meowment/), which was made earlier this year, as a showcase of my development as a coder. 

This project was made from scratch, only taking the idea of the previous cat cafe website and fleshing it out from the ground up. 

[Pawse Live Site](https://pawse-4504aa9c3705.herokuapp.com/)

## Table of Contents

- [Pawse - Introduction](#pawse---introduction)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
    - [Strategy \& Scope: User Stories](#strategy--scope-user-stories)
    - [Structure: Site flow](#structure-site-flow)
    - [Skeleton: Wireframes](#skeleton-wireframes)
    - [Surface: Visual Design](#surface-visual-design)
      - [Colors](#colors)
      - [Fonts](#fonts)
      - [Logo](#logo)
  - [Database Design](#database-design)
  - [Agile Development](#agile-development)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks \& Libraries](#frameworks--libraries)
    - [Other Tools](#other-tools)
  - [Testing \& Validation](#testing--validation)
  - [Deployment \& Development](#deployment--development)
    - [Deployment on Heroku](#deployment-on-heroku)
    - [Local Deployment](#local-deployment)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)


## UX

### Strategy & Scope: User Stories

| **Epic**                               | **User Story**                                                                                                                        |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Unauthenticated User Features          | As a user, I want to see a navigation menu so that I can easily navigate to the desired content                                       |
|                                        | As a user, I want to see an inviting landing page so that I know what the page is about and what I can do                             |
|                                        | As a user, I want to see all menu options of the cafe so that I can make an informed decision if I want to visit                      |
|                                        | As a user, I want to see the cats living in the cafe so that I can already familiarize myself with them before my visit               |
|                                        | As a user, I want to see whether there are already people interested in the cats so that I can choose one accordingly                 |
|                                        | As a user, I want to be able to register to the site so that I get access functionality for authenticated users on the site           |
|                                        | As a user, I want to be able to login so I can access my account                                                                      |
|                                        | As a user, I want to have easy access to social media accounts of the cafe so that I can engage with the owners and other customers   |
| Authenticated User Features            | As an authenticated user, I want to be able to log out of my account so that my account is secure from other users on the same device |
|                                        | As an authenticated user, I want to be able to delete my account so that I can forget about the page                                  |
|                                        | As an authenticated user, I want to be able to voice my interest in one of the cats so that I can adopt it                            |
|                                        | As an authenticated user, I want to be able to edit my interest in one of the cats                                                    |
|                                        | As an authenticated user, I want to be able to delete my interest in one of the cats                                                  |
| Site Admin Features                    | As a site admin, I want to be able to log in to my admin account so that I can make changes to the content on the site                |
|                                        | As a site admin, I want to be able to adjust the menu from the frontend so that it is always up to date                               |
|                                        | - As a site admin, I want to be able to add new menu items from the frontend                                                          |
|                                        | - As a site admin, I want to be able to edit menu items from the frontend                                                             |
|                                        | - As a site admin, I want to be able to delete menu items from the frontend                                                           |
|                                        | As a site admin, I want to be able to adjust the kittens from the frontend so that customers always see the current kittens           |
|                                        | - As a site admin, I want to be able to add new cats from the frontend                                                                |
|                                        | - As a site admin, I want to be able to edit cats from the frontend                                                                   |
|                                        | - As a site admin, I want to be able to delete cats from the frontend                                                                 |
| Authenticated User/Site Admin Features | As an authenticated user/site admin I want to see feedback from my actions so that I know my action was successful                    |
|                                        | As an authenticated user/site admin I want to be asked to confirm deletion so that I don't accidentally delete something wrong        |
| Site Owner Features                    | As a site owner, I want the site to be visually pleasing so that users like to come back/share it                                     |

The target audience for the site consists of people 13 and above who want to meet cats and have a drink and/or some food.
Parts of the target audience may want to meet cats outside of their home because they can't have cats of their own.
Other parts of the target audience may want to meet cats they can adopt.
And even other parts may just want to hang out with cats and friends. 

### Structure: Site flow

The website consists of four main pages that can be accessed via the nav bar. 

Additional functionalities can be accessed from the nav bar or as subpages, depending on whether a user is signed in or not and depending on the user role. 

This sitemap chart shows the high-level flow of the site: 

![Sitemap](static/docs/pawse-sitemap.png)

### Skeleton: Wireframes

The wireframes for the different pages can be divided into unauthenticated users, authenticated users and site admins.

1. Home

| **Page Version**                  | **Mobile**              | **Desktop**                   |
|-----------------------------------|-------------------------|-------------------------------|
| Unauthenticated                   | ![Home Mobile](static/docs/mobile-u-landing.png) | ![Home Desktop](static/docs/desktop-u-landing.png) |
| Unauthenticated - nav expanded | ![Home Nav Expanded Mobile](static/docs/mobile-u-landing-nav-expanded.png) | ![Home Nav Expanded Desktop](static/docs/desktop-u-landing-nav-expanded.png)  |
| Authenticated                     | Same as unauthenticated | ![Home A Desktop](static/docs/desktop-a-landing.png) |
| Authenticated - nav expanded   | ![Home A Nav Expanded Mobile](static/docs/mobile-a-landing-nav-expanded.png) | Same as Unauthenticated with nav expanded, but with Authenticated nav bar options |
| Site Admin                        | Same version as authenticated | Same version as authenticated |

2. Menu

| **Page Version**       | **Mobile**              | **Desktop**             |
|------------------------|-------------------------|-------------------------|
| Unauthenticated        | ![Menu Mobile](static/docs/mobile-u-menu-list.png) | ![Menu Desktop](static/docs/desktop-u-menu-list.png) |
| Authenticated          | Same as unauthenticated | Same as unauthenticated |
| Site Admin             | N/A                     | ![Menu S Desktop](static/docs/desktop-s-menu-list.png) |
| Site Admin - Add/Edit Menu Item     | N/A                     | ![Add Menu Item Desktop](static/docs/desktop-s-add-edit-menu-item.png) |
| Site Admin - Add/Edit Menu Category | N/A                     | ![Add Category Desktop](static/docs/desktop-s-add-menu-category.png) |

3. Cats

| **Page Version**               | **Mobile** | **Desktop** |
|--------------------------------|------------|-------------|
| Unauthenticated                | ![Cats Mobile](static/docs/mobile-u-cats.png) | ![Cats Desktop](static/docs/desktop-u-cats.png) |
| Authenticated                  | ![Cats A Mobile](static/docs/mobile-a-cats.png) | ![Cats A Desktop](static/docs/desktop-a-cats.png) |
| Authenticated - added interest | ![Cats added interest Mobile](static/docs/mobile-a-cats-added-interest.png) | ![Cats added interest Desktop](static/docs/desktop-a-cats-added-interest.png) |
| Site Admin                     | N/A        | ![Cats S Desktop](static/docs/desktop-s-cats.png) |
| Site Admin - Add/Edit Cat                   | N/A        | ![Add Cat Desktop](static/docs/desktop-s-add-edit-cat.png) |

4. Sign Up/Sign In/My Account

| **Page Version**               | **Mobile** | **Desktop** |
|--------------------------------|------------|-------------|
| Unauthenticated - Sign Up                | ![Sign Up Mobile](static/docs/mobile-u-sign-up.png) | ![Sign Up Desktop](static/docs/desktop-u-sign-up.png) |
| Unauthenticated - Sign In                | ![Sign In Mobile](static/docs/mobile-u-sign-in.png) | ![Sign In Desktop](static/docs/desktop-u-sign-in.png) |
| Authenticated - My Account             | ![My Account Mobile](static/docs/mobile-a-my-account.png) | ![My Account Desktop](static/docs/desktop-a-my-account.png) |

### Surface: Visual Design

#### Colors

I was not fully satisfied with the color scheme used on my first cat cafe project, I felt the colors were a little stuffy, so I wanted to have a fresh look for this project.

My goal was to have a more elegant and modern look for the page, light and inviting with colors that pop. 

I tried different color palettes using Coolors.co and first ended up with [this palette](https://coolors.co/283d3b-197278-ffffff-c44536-772e25) using red and teal tones with a simple white background. However, I felt the teal and red were a little too heavy. 

I tried [another palette](https://coolors.co/palette/000000-14213d-fca311-e5e5e5-ffffff) from the same site and am much happier with the result:

![Color Scheme](static/docs/pawse-colors.png)

#### Fonts

Building on the idea of a minimalistic modern look and feel of the site, I wanted simple fonts for the site. 

For any flowing text, I picked [Karla](https://fonts.google.com/specimen/Karla?preview.text=Welcome%20to%20our%20cafe&preview.text_type=custom&category=Sans+Serif), an elegant but playful sans serif font. 

For the headings on the page, I picked [Raleway](https://fonts.google.com/specimen/Raleway?preview.text=Pawse&preview.text_type=custom&category=Sans+Serif), which is also very minimalistic and sans serif. 

#### Logo

The logo design is based on the name of the cafe, which is a pun made of paws of a cat and pause like a break. Therefore, the logo is a stylized cat paw with a pause sign on the big circle. 

![Logo](static/images/logo-highlight.png)


## Database Design

The Entity Relationship Diagram shows the basic structure of the database.

During development, the entities and their fields were changed based on the needs that came up. 

Here is the initial ERD:

![ERD](static/docs/pawse-erd-old.png)

And here is the updated version, reflecting the current state of the models:

![ERD new](static/docs/pawse-erd-new.png)

The User model is provided by Django.

The MenuCategory and MenuItem models are utilized to display the menu list divided by category and holds information about the price of the different items as well. An update made during development was to add in an the "order" field on the MenuCategory model, which is used to display the categories in a specified order on the website. 

The Cat model is used to store all relevant information about the cats of the cafe, including the name, date of birth, description and an image of the cat. Additionally, the Application model holds information about any application sent in by the users for any cats. 

The Cat model was updated during development to include a slug field, which was needed to display the correct application. 

## Agile Development

The project was planned and carried out using Agile methodologies. The tool used for this was GitHub Issues. 

[Kanban boards](https://github.com/users/hashtag-squirrel/projects/2) were set up to track tickets through statuses Backlog, Todo, In Progress and Done. 

Two boards were set up: [A Task/User Story board](https://github.com/users/hashtag-squirrel/projects/2/views/1) and an [Epic board](https://github.com/users/hashtag-squirrel/projects/2/views/4). This was done to keep track of the different types of issues separately. 

When planning out the User Stories, they were grouped into Epics and all were created as issues in GitHub Issues using custom templates. The Tasks and User Stories were linked to the Epics as needed. Tasks were created for features that were not covered by User Stories, but needed for the project, e.g. the planning of the project and the general setup, as well as polishing/bug fixing tickets later on in the project. 

The Epics and their related tickets were split up into several [Milestones](https://github.com/hashtag-squirrel/pawse/milestones?state=closed), which represented approximately one week long sprints. Initially, I planned eight sprints, but condensed the last three milestones into one big milestone lasting for more than one week. There was also a phase at the end of Sprint 5 where I went back to the planning board and planned out the remaining tickets for the last milestone. 

In order to keep best track over the time needed for the tickets, I created a [Roadmap](https://github.com/users/hashtag-squirrel/projects/2/views/2?groupedBy%5BcolumnId%5D=Milestone) displaying the milestones and their respective tickets, which is shown here:

![Roadmap](static/docs/agile-roadmap.png)

At the start of every sprint, I checked the tickets belonging to the respective milestone and added Acceptance Criteria for every ticket, as well as an estimate in Story Points. I also made sure that every ticket was prioritized according to MoSCoW prioritization and tagged appropriately. 

The goal of the planning was to even out the work I had to do over all sprints and when I generated a chart with Story Points per Sprint, I can see that it worked out quite well. Sprint 6 was expected to have more storypoints since it lasted about twice as long as other sprints. 

![Story Point Chart](static/docs/agile-storypoint-chart.png)

I also checked that each sprint had no more than 40% of tickets that were categorized as anything else than must-haves. 

## Features

### Existing Features

<!-- Add features including screenshots -->
All user features:
- Navigation 
- Footer
- Pages:
  - Home Page
  - Menu 
  - Cats - Overview
  - Cats - Detail

Authenticated user features:
- Login/Registration
- Add/Edit/Delete interest in cat
- My Account page



### Future Features

Additionally to more content that could be added to the existing pages, there are many features that can be added to flesh out the project. Here is a list of potential features that can be added with varying amounts of work:

Unauthenticated User features:
- Adding an Articles page where information about the cats/cafe/news can be shared
- A gallery with more impressions of the cafe

Authenticated User features:
- An Account overview page
- The possibility to delete one's own account
- Adding comments on the cats
- Adding testimonials after a visit
- A booking system for visits
- A messaging system to discuss details/status of applications

Site Admin features in the UI:
- Add/Edit/Delete Menu items/sections
- Add/Edit/Delete Cats

## Technologies

### Languages

- HTML5
- CSS3
- JavaScript
- Python 3.11

### Frameworks & Libraries

- Bootstrap v5.2
- Django v3.2

Django libraries:

- gunicorn 
- dj-database-url
- psycopg2 
- dj3-cloudinary-storage
- urllib3
- pillow
- django-allauth
- django-autoslug
- django-crispy-forms
- crispy-bootstrap5
- django-active-link

Test coverage:
- coverage

To create a virtual environment:
- pipenv

### Other Tools

- Git - used for version control
- GitHub - used for online storage of codebase and GitHub Issues tool
- VS Code - used as the coding editor of choice
- Balsamiq - for creation of the wireframes
- Lucidchart - used to create diagrams
- ElephantSQL - used to host the PostgreSQL database
- Cloudinary - as static file storage
- Heroku - used to host the application
- WAVE - to evaluate the accessibility of the site.
- [RGB to Hex converter](https://www.rgbtohex.net/) - to convert color codes

## Testing & Validation

All testing and validation is documented in [TESTING.md](TESTING.md)

## Deployment & Development

### Deployment on Heroku

1. Login to the Heroku dashboard and create a new app.
2. Navigate to Settings and add the Python Buildpack
3. Set environment variables in the Config Vars section of the Settings tab.
   - You need to define the following variables:
     - `DATABASE_URL` - `<Your Postgres URL>`
     - `CLOUDINARY_URL` - `<Your Cloudinary URL>`
     - `SECRET_KEY` - `<Your Secret Key>`
4. Connect your GitHub repository to your Heroku app.
5. In the Deploy tab, enable automatic deploys from your GitHub repository using the "main" branch.
6. Click the "Deploy Branch" button to deploy the "main" branch.
7. Once the app has been deployed, click the "View App" button to view the app.

### Local Deployment

1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. Create a virtual environment typing `pipenv shell` in your terminal
5. Install the required dependencies specified in the Pipfile by typing `pipenv install` in the terminal.
6. Note: The project is setup to use environment variables. You will need to set these up in your local environment.
  - For local deployment, you will need to create an `env.py` file in the root directory of the project and set the environment variables in this file as follows:
    - `os.environ['DATABASE_URL'] = '<Your Postgres URL>'`
    - `os.environ['SECRET_KEY'] = '<Your Secret Key>'`
    - `os.environ['CLOUDINARY_URL'] = '<Your Cloudinary URL>'`
    - `os.environ["DEBUG"] = 'DEBUG'`
7. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
8. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.
9.  Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

## Credits

Text content for the following sections were generated by OpenAIs ChatGPT-3.5 (July 20 version):

- Landing page: About section, Testimonials section and Contact section
- Menu page: Menu items
- Cats page: Cat names and descriptions

### Media

[Base for the logo:](https://pixabay.com/vectors/paw-print-dog-cat-animal-pet-5892565/)
[Hero image on home page](https://pixabay.com/photos/cat-mammal-animal-cafe-pet-feline-8101641/)
[Hero video on home page](https://coverr.co/videos/a-grey-and-white-cat-licks-its-lips-otuDwMne0G)
[Whiskers](https://www.pexels.com/photo/orange-cat-in-close-up-photography-9443839/)
[Luna](https://www.pexels.com/photo/a-tuxedo-cat-on-a-hanging-wooden-bridge-7726104/)
[Oliver](https://www.pexels.com/photo/brown-cat-lying-on-knitted-textile-952581/)
[Amber](https://www.pexels.com/photo/close-up-photo-of-sitting-brown-tabby-cat-2373663/)
[Mocha](https://www.pexels.com/photo/cute-cat-lying-on-sofa-4154508/)
[Simba](https://www.pexels.com/photo/fluffy-ginger-cat-15511201/)
[Repeatable Paw Vector](https://www.vecteezy.com/vector-art/2469425-seamless-pattern-with-animal-paw-prints-gray-paws-on-a-white-background-vector-illustration-endless-background)
[Cat image on 404 page](https://www.pexels.com/photo/orange-tabby-cat-hiding-its-face-209037/)
[Cat image on 500 page](https://pixabay.com/photos/cat-black-cat-work-computer-963931/)

### Code

[Sticky Footer Tutorial](https://devpractical.com/bootstrap-sticky-footer/)
[How to add a second model in a view](https://www.appsloveworld.com/django/100/28/refer-to-multiple-models-in-view-template-in-django)
[Calculation for age from days](https://www.codesansar.com/python-programming-examples/convert-number-days-years-months-days.htm)
[Custom template tag for cats page](https://stackoverflow.com/questions/31916408/is-django-can-modify-variable-value-in-template)
[Redirect to same page after login/logout/register](https://stackoverflow.com/a/13595154)