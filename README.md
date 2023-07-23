# Pawse - Introduction

<!-- Image with responsive screenshot here -->

<!-- write introduction here -->

<!-- Link to live site -->

## Table of Contents

<!-- TOC goes here -->

- [Pawse - Introduction](#pawse---introduction)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
    - [Strategy \& Scope: User Stories](#strategy--scope-user-stories)
    - [Structure: Site flow](#structure-site-flow)
    - [Skeleton: Wireframes](#skeleton-wireframes)
    - [Surface: Visual Design](#surface-visual-design)
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

- As a user, I want to see a navigation menu so that I can easily navigate to the desired content
- As a user, I want to see all menu options of the cafe so that I can make an informed decision if I want to visit 
- As a user, I want to see the cats living in the cafe so that I can already familiarize myself with them before my visit
- As a user, I want to see whether there are already people interested in the cats so that I can choose one accordingly
- As a user, I want to be able to register to the site so that I get access functionality for authenticated users on the site
- As a user, I want to be able to login so I can access my account
- As a user, I want to have easy access to social media accounts of the cafe so that I can engage with the owners and other customers
  
- As an authenticated user, I want to be able to log out of my account so that my account is secure from other users on the same device
- As an authenticated user, I want to be able to delete my account so that I can forget about the page
- As an authenticated user, I want to be able to voice my interest in one of the cats so that I can adopt it
- As an authenticated user, I want to be able to edit my interest in one of the cats 
- As an authenticated user, I want to be able to delete my interest in one of the cats

- As a site admin, I want to be able to log in to my admin account so that I can make changes to the content on the site
- As a site admin, I want to be able to adjust the menu from the frontend so that it is always up to date
  - As a site admin, I want to be able to add new menu items from the frontend
  - As a site admin, I want to be able to edit menu items from the frontend
  - As a site admin, I want to be able to delete menu items from the frontend
- As a site admin, I want to be able to adjust the kittens from the frontend so that customers always see the current kittens
  - As a site admin, I want to be able to add new cats from the frontend
  - As a site admin, I want to be able to edit cats from the frontend
  - As a site admin, I want to be able to delete cats from the frontend

- As an authenticated user/site admin I want to see feedback from my actions so that I know my action was successful
- As an authenticated user/site admin I want to be asked to confirm deletion so that I don't accidentally delete something wrong

- As a site owner, I want the site to be visually pleasing so that users like to come back/share it





<!-- Add table, User Stories mapped to Epics -->

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

<!-- Add color scheme -->

<!-- Add Fonts -->

<!-- Add image strategy? -->


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

### Media

<!-- add media links -->

### Code

<!-- Add tutorial links/links to code used -->