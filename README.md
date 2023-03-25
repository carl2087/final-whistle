# The Final Whistle

The Final Whistle is a full stack web application built using the Django Framework. The main purpose of the site is to provide a platform for the user to write a short blog posting their opinion on the current affairs that is happening in football. The intended target audience is anyone who has an interest in football from teenagers to adults. 

The application has full CRUD functionality for user generated posts and provides an easy for other users of the site to comment on the posts upvote and downvote posts and create their own accounts as well.

The site also features a back-end admin dashboard that allows admin of the site to review and authorise posts as well as comments.

The site is hosted on Heroku the link is below

[The Final Whistle](https://the-final-whistle.herokuapp.com/)


[![The Final Whistle devices image](./assets/readme-images/am-i-responsive.png)](https://the-final-whistle.herokuapp.com/)

# Table of contents

# Project objectives

## Main objective

The main objective of this project was to create a full stack website as part of [The Code Institute](https://codeinstitute.net/) Diploma in Full Stack Software Development.
This project is my fourth portfolio project on the course. Amongst other assesment criteria, this project had to be built using HTML, CSS, JavaScript, Python and the Django framework, and feature full CRUD functionality and user authorisation. The project also had to be planned and designed using agile methodologies. 

One of my main interests is sports I decided to create a website where users of the site can create posts about the current affairs in football.

My aim was to create a minimum viable product that can be built upon with more features in the future and also to create a website that I would enjoy creating and using in the future as well.

## Site users

Users of the site can create posts, and comments, upvote and downvote posts and add tags to their own created posts. Users can view, edit and delete their own posts also.
I tried to make the site as appealing as it could be to as broad of an audience as possible with a clear layout an easy way of learning how to use the site and the ability to 
customise the created posts with an image.

## Site owner

The goal for the site owner is to provide a stable user experience that is enjoyable to encourage user interaction. The site should be accessible and appealing to new users, it should also be scaleable with an easy way to add more features in the future. Content on the site should be easily moderated to ensure community standards are met and be of high quality. 

<br>

[Back to table of contents](#table-of-contents)

# Project management

## Agile development

I managed this project using an [Agile](https://agilemanifesto.org/) methodology. I used GitHub projects to refine epic tasks to break them down into user stories. This ensured that tracking and organising the project into iterations was manageable. The GitHub project board had a to do section where user stories where first placed, an in progress tab where user stories where moved to when being worked on, a done section where the stories where moved when completed. A bugs tab for any coding problems that arose during the process and a won't-have section for features that where not included in this stage of the project.

[The Final Whistle user stories](https://github.com/users/carl2087/projects/7)

I also used GitHub projects to organise my project tasks in the same way this included tasks such as creating wireframes, choosing the colour theme for the site and writing the readme document.

[The Final Whistle project tasks](https://github.com/users/carl2087/projects/8)


## GitHub stories images

![User stories the final whistle](./assets/readme-images/user-stories.png) 
![Project tasks the final whistle](./assets/readme-images/project-tasks.png)


## Database schema

I drew the database schemas up in Microsoft Excel &copy; The shema diagrams where used to plan the database models, fields and also the relationships between the models and how they would interact with each other. The Final Whistle consists of two models one for comments and one for posts. There is an oppurttunity to create a third model for the football teams in a future release of the site.

![Database schema comment model](./assets/wireframes/comment-model-diagram.png)
![Database schema post model](./assets/wireframes/post-model-diagram.png)

<br>

[Back to table of contents](#table-of-contents)


# User experience and design

When planning the site and how it would affect the user experince is first created wireframes for the project to decide on the layout of each page.
I then used [Color Hunt](https://colorhunt.co/) to decide on the colour theme for the site. I used Google &copy; fonts to decide on which fonts I would use for the site. I have included images below relating to the steps I undertook.

## Wireframe images

### Home page for desktop

<br>

![Home page desktop](./assets/wireframes/home-page.png)

### Home page for tablet

<br>

![Home page tablet](./assets/wireframes/home-page-tab.png)

### Home page for mobile phone

<br>

![Home page mobile](./assets/wireframes/home-page-mob.png)

### Create a post page 

<br>

![Create a post page](./assets/wireframes/create-post.png)

### Create a post page tablet 

<br>

![Create a post page tablet](./assets/wireframes/create-post-tab.png)

### Create a post page mobile phone

<br>

![Create a post page mobile](./assets/wireframes/create-post-mob.png)

### Comment page 

<br>

![Create a comment page](./assets/wireframes/comment-on-a-post.png)

### Comment page tablet

<br>

![Create a comment page tablet](./assets/wireframes/comment-on-a-post-tablet.png)

### Comment page mobile phone

<br>

![Create a comment page mobile](./assets/wireframes/comment-on-a-post-mobile.png)

### Login and user register pages

<br>

![Log in page](./assets/wireframes/log-page.png)
![Register page](./assets/wireframes/reg-page.png)

### Login and user register pages

<br>

![Log in page tablet](./assets/wireframes/log-page-tab.png)
![Register page tablet](./assets/wireframes/reg-page-tab.png)

### Login and user register pages

<br>

![Log in page mobile](./assets/wireframes/log-page-mob.png)
![Register page mobile](./assets/wireframes/reg-page-mob.png)


## Colour sheme

I used [Color Hunt](https://colorhunt.co/) to select the colour scheme for the site I find it a useful site as it has a random generator button so you can see a lot of different colour schemes quickly. I decided to use the colour palette below as the colours are not too bright and work well together.

Color hunt palette

![Color hunt colour palette](./assets/wireframes/color-hunt-palette.png)

Color hunt palette codes

![Color hunt colour palette code](./assets/readme-images/color-hunt-palette-code.png)

## Logo 

For the logo I used a whistle icon from [flaticon](https://www.flaticon.com/free-icon/whistle_3627675?term=whistle&page=1&position=34&origin=search&related_id=3627675) the use of this logo is free as long as it is attributed. I placed the whistle icon on a white square background with rounded corners.

<br>

![Whistle icon](./assets/readme-images/whistle-icon.png)

## Favicon

I created the favicon on [real favicon generator](https://realfavicongenerator.net/). I used the whistle icon above to keep the design of the site consistent.

<br>

![Favicon](./assets/readme-images/favicon.png)


## Typography

I used Google&copy; fonts to decide on which type of fonts to use on The Final Whistle for headings and titles I used [Nunito](https://fonts.google.com/specimen/Nunito) and for bodies of text I used [Rubik](https://fonts.google.com/specimen/Rubik). I chose these fonts because they are clear and synergize well together I chose to use a different fonts for headers and bodies of text just to give the site some nice customization.

<br>

![Nunito](./assets/readme-images/nunito-title-text.png)
![Rubik](./assets/readme-images/rubik-bodies-of-text.png)

## CSS framework

To help speed up design and building of the site I decided to use the Materialize&copy; front-end framework I chose this because firstly I like the way the cards looked and worked which forms the basis of the index page on the site and also to challenge myself to use a different framework from Bootstrap&copy;. This did have it's challenges along the way to ensure everything worked as it should but in the end I think it was the right choice and would do it again.

<br>

![Materielize](./assets/readme-images/materialize-logo.png)


## Site structure

I tried to keep the site structure simple, clean and easy to learn how to use to encourage users of the site to want to come back and use it again and again. Content is hidden from users of the site who are not logged in and prompt the user to register or login to access the different areas of the site. The navbar at the top of the page will change options depending on the login state of the site user.

<br>

![navbar logged in](./assets/readme-images/logged-in-links.png)
![navbar logged out](./assets/readme-images/logged-out-links.png)

[Back to table of contents](#table-of-contents)

# Features

## Existing features

### Home page

The home page is the first page of the site that users see when they navigate to The Final Whistle URL. It's designed to be simple with eye-catching cards with images that relate to the post users can click the title of the post to initiate a card action that reveals the excerpt of the post to give the user a small glimpse of what the post says if they then decide to click on the full post link they will be taken to the post detail screen where they can read the full post or comment on the post.

<br>

Home page Desktop

![The Final Whistle homepage](./assets/readme-images/homepage-desktop.png)

Home page tablet

![The Final Whistle homepage tablet](./assets/readme-images/homepage-tablet.png)

Home page mobile phone

![The Final Whistle homepage mobile](./assets/readme-images/homepage-mobile.png)

### Navbar

The site has a navbar along the top which which has links for the home page which is The Final Whistle logo and depending on the current logged in state for the user there will be links to register and login or logout. There is also a home button link as well which is always visible. On smaller devices The Final Whistle logo moves to the centre of the navbar and a hamburger menu appears with the relevant site links nested inside.

![The Final Whistle homepage mobile](./assets/readme-images/navbar-desktop.png)

![The Final Whistle homepage mobile](./assets/readme-images/navbar-tablet-mobile.png)

![The Final Whistle hamburger menu](./assets/readme-images/hamburger-menu.png)

### Footer


## Future Features

## Technologies used

# Testing

manual testing deployed early to Heroku ...

# Deployment

# Credits

The main image at the top of the readme is created on [Am I responsive](https://ui.dev/amiresponsive)

# Acknowledgements