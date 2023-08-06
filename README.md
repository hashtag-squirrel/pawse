# Pawse - Introduction

<!-- Image with responsive screenshot here -->

Pawse is a full-stack website project for a cat cafe. 

It is a remake of the HTML & CSS only website ["In the Meowment"](https://hashtag-squirrel.github.io/in-the-meowment/), which was made earlier this year, as a showcase of my development as a coder. 

This project was made from scratch, only taking the idea of the previous cat cafe website and fleshing it out from the ground up. 

<!-- Link to live site -->

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
    - [Frameworks](#frameworks)
    - [Modules/Packages](#modulespackages)
  - [Testing \& Validation](#testing--validation)
  - [Deployment \& Development](#deployment--development)
    - [Deployment on Heroku](#deployment-on-heroku)
    - [Forking the Repository](#forking-the-repository)
    - [Cloning the Repository](#cloning-the-repository)
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


<!-- Add section about target audience -->

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

I tried different color palettes using [Coolors](https://coolors.co/283d3b-197278-ffffff-c44536-772e25) and ended up with this palette using red and teal tones with a simple white background:

![Color Scheme](static/docs/pawse-colors.png)

#### Fonts

Building on the idea of a minimalistic modern look and feel of the site, I wanted simple fonts for the site. 

For any flowing text, I picked [Karla](https://fonts.google.com/specimen/Karla?preview.text=Welcome%20to%20our%20cafe&preview.text_type=custom&category=Sans+Serif), an elegant but playful sans serif font. 

For the headings on the page, I picked [Raleway](https://fonts.google.com/specimen/Raleway?preview.text=Pawse&preview.text_type=custom&category=Sans+Serif), which is also very minimalistic and sans serif. 

#### Logo

The logo design is based on the name of the cafe, which is a pun made of paws of a cat and pause like a break. Therefore, the logo is a stylized cat paw with a pause sign on the big circle. 


## Database Design

The Entity Relationship Diagram shows the basic structure of the database.

![ERD](static/docs/pawse-erd.png)

The User model is provided by Django and extended with a UserRole model. 

The MenuCategory and MenuItem models are utilized to display the menu list divided by category and holds information about the price of the different items as well. 

The Cat model is used to store all relevant information about the cats of the cafe, including the name, date of birth, description and an image of the cat. Additionally, the Application model holds information about any application sent in by the users for any cats. 


## Agile Development

<!-- Add info about sprints -->

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

Site Admin features:
- Add/Edit/Delete Menu items/sections
- Add/Edit/Delete Cats

### Future Features

<!-- Add future features -->

## Technologies

### Languages

### Frameworks

### Modules/Packages

## Testing & Validation

<!-- Add content in TESTING.md -->

## Deployment & Development

### Deployment on Heroku

### Forking the Repository

### Cloning the Repository

## Credits

Text content for the landing page in the About section and Testimonials section was generated by OpenAIs ChatGPT-3.5 (July 20 version).

### Media

[Base for the logo:](https://pixabay.com/vectors/paw-print-dog-cat-animal-pet-5892565/)
[Hero image on home page](https://pixabay.com/photos/cat-mammal-animal-cafe-pet-feline-8101641/)
[Whiskers](https://www.pexels.com/photo/orange-cat-in-close-up-photography-9443839/)
[Luna](https://www.pexels.com/photo/a-tuxedo-cat-on-a-hanging-wooden-bridge-7726104/)
[Oliver](https://www.pexels.com/photo/brown-cat-lying-on-knitted-textile-952581/)
[Amber](https://www.pexels.com/photo/close-up-photo-of-sitting-brown-tabby-cat-2373663/)
[Mocha](https://www.pexels.com/photo/cute-cat-lying-on-sofa-4154508/)
[Simba](https://www.pexels.com/photo/fluffy-ginger-cat-15511201/)

### Code

[Sticky Footer Tutorial](https://devpractical.com/bootstrap-sticky-footer/)
[How to add a second model in a view](https://www.appsloveworld.com/django/100/28/refer-to-multiple-models-in-view-template-in-django)
[Calculation for age from days](https://www.codesansar.com/python-programming-examples/convert-number-days-years-months-days.htm)