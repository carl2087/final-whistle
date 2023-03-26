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


[Back to table of contents](#table-of-contents)


# User experience and design

When planning the site and how it would affect the user experince is first created wireframes for the project to decide on the layout of each page.
I then used [Color Hunt](https://colorhunt.co/) to decide on the colour theme for the site. I used Google &copy; fonts to decide on which fonts I would use for the site. I have included images below relating to the steps I undertook.

## Wireframe images

### Home page for desktop


![Home page desktop](./assets/wireframes/home-page.png)

### Home page for tablet


![Home page tablet](./assets/wireframes/home-page-tab.png)

### Home page for mobile phone


![Home page mobile](./assets/wireframes/home-page-mob.png)

### Create a post page 


![Create a post page](./assets/wireframes/create-post.png)

### Create a post page tablet 


![Create a post page tablet](./assets/wireframes/create-post-tab.png)

### Create a post page mobile phone


![Create a post page mobile](./assets/wireframes/create-post-mob.png)

### Comment page 


![Create a comment page](./assets/wireframes/comment-on-a-post.png)

### Comment page tablet


![Create a comment page tablet](./assets/wireframes/comment-on-a-post-tablet.png)

### Comment page mobile phone


![Create a comment page mobile](./assets/wireframes/comment-on-a-post-mobile.png)

### Login and user register pages


![Log in page](./assets/wireframes/log-page.png)
![Register page](./assets/wireframes/reg-page.png)

### Login and user register pages


![Log in page tablet](./assets/wireframes/log-page-tab.png)
![Register page tablet](./assets/wireframes/reg-page-tab.png)

### Login and user register pages


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


![Whistle icon](./assets/readme-images/whistle-icon.png)

## Favicon

I created the favicon on [real favicon generator](https://realfavicongenerator.net/). I used the whistle icon above to keep the design of the site consistent.


![Favicon](./assets/readme-images/favicon.png)


## Typography

I used Google&copy; fonts to decide on which type of fonts to use on The Final Whistle for headings and titles I used [Nunito](https://fonts.google.com/specimen/Nunito) and for bodies of text I used [Rubik](https://fonts.google.com/specimen/Rubik). I chose these fonts because they are clear and synergize well together I chose to use a different fonts for headers and bodies of text just to give the site some nice customization.


![Nunito](./assets/readme-images/nunito-title-text.png)
![Rubik](./assets/readme-images/rubik-bodies-of-text.png)

## CSS framework

To help speed up design and building of the site I decided to use the Materialize&copy; front-end framework I chose this because firstly I like the way the cards looked and worked which forms the basis of the index page on the site and also to challenge myself to use a different framework from Bootstrap&copy;. This did have it's challenges along the way to ensure everything worked as it should but in the end I think it was the right choice and would do it again.


![Materialize](./assets/readme-images/materialize-logo.png)


## Site structure

I tried to keep the site structure simple, clean and easy to learn how to use to encourage users of the site to want to come back and use it again and again. Content is hidden from users of the site who are not logged in and prompt the user to register or login to access the different areas of the site. The navbar at the top of the page will change options depending on the login state of the site user.


![navbar logged in](./assets/readme-images/logged-in-links.png)
![navbar logged out](./assets/readme-images/logged-out-links.png)

[Back to table of contents](#table-of-contents)

# Features

## Existing features

### Home page

The home page is the first page of the site that users see when they navigate to The Final Whistle URL. It's designed to be simple with eye-catching cards with images that relate to the post users can click the title of the post to initiate a card action that reveals the excerpt of the post to give the user a small glimpse of what the post says if they then decide to click on the full post link they will be taken to the post detail screen where they can read the full post or comment on the post.

Home page Desktop

![The Final Whistle homepage](./assets/readme-images/homepage-desktop.png)

Home page tablet

![The Final Whistle homepage tablet](./assets/readme-images/homepage-tablet.png)

Home page mobile phone

![The Final Whistle homepage mobile](./assets/readme-images/homepage-mobile.png)

### Navbar

The site has a navbar along the top which which has links for the home page which is The Final Whistle logo and depending on the current logged in state for the user there will be links to register and login or logout. There is also a home button link as well which is always visible. On smaller devices The Final Whistle logo moves to the centre of the navbar and a hamburger menu appears with the relevant site links nested inside.

Desktop navbar

![The Final Whistle homepage mobile](./assets/readme-images/navbar-desktop.png)

Tablet and mobile home page

![The Final Whistle homepage mobile](./assets/readme-images/navbar-tablet-mobile.png)

Hamburger menu

![The Final Whistle hamburger menu](./assets/readme-images/hamburger-menu.png)

### Footer

The footer for The Final Whistle has the title of the site and also has social links to popular platforms where The Final Whistle will have presence when clicked on they open in a new tab to keep the site ready and waiting to go back to.

Desktop Footer

![The Final Whistle footer desktop](./assets/readme-images/footer-desktop.png)

Tablet and mobile footer

![The Final Whistle footer tablet and mobile](./assets/readme-images/footer-tablet-mobile.png)

### Create a post 

On this page thsi enables a registered or logged in user to create a post if the user is not logged in they will be prompted to create an account or sign in to their account. The form will prompt the user if they have not filled out a required part of the form. The user can choose whether they want to upload their own image if the user declines to do so, a generic image is added automatically. When a user has succesfully submitted a post they are shown a message that lets them know that their post is awaiting approval.

Create a post page

![The Final Whistle create a post page](./assets/readme-images/create-a-poat-page.png)

Screen when not logged in 

![The Final Whistle not logged in create a post page](./assets/readme-images/not-logged-in-create-post.png)

Post succesful message

![The Final Whistle post successful](./assets/readme-images/post-succesful-message.png)


### My posts page

There is a link on the home page that will take the user to their own posts page which has links underneath each post that allow the user to edit their own posts and also delete their own posts as well if a user decides to edit their own posts they are taken to a new screen with the edit a post form which is pre-populated with the data that was entered on the original post. On this page there is a submit button to save the changes and a cancel button which will give the user chance to confirm the cancel in case it was pressed accidentally by the way of a modal appearing. The delete button works the same way a modal appears to give the user the chance to confirm the delete or cancel the delete. If the user is not logged in or registered they will be taken to a screen to prompt them to log in or register an account.

My posts page

![The Final Whistle my posts page](./assets/readme-images/my-post-page.png)

Edit post

![The Final Whistle edit post page](./assets/readme-images/edit-post-page.png)

Edit succesful message

![The Final Whistle edit successful page](./assets/readme-images/post-edit-succesful.png)


Cancel edit post modal

![The Final Whistle cancel edit modal](./assets/readme-images/cancel-edit.png)

Delete post modal

![The Final Whistle cancel edit modal](./assets/readme-images/delete-post-modal.png)

Not logged in page

![The Final Whistle not logged in page](./assets/readme-images/not-logged-in-my-posts.png)

### Post detail page

When a user clicks on the full post link on the cards that feature on the home page they are taken to the post detail page. The post detail page features an enlarged image that was uploaded with the post that if clicked on will go full screen to give the user a better experience of viewing it. The comments made on the post are underneath the image. With the post content to the right of the image there are icons underneath the text that show the number of comments made and gives the option to upvote and downvote the post. The arrows are only clickable if the user is logged in and will be red rather than blue if the user has clicked on them also if the user is logged in they will be able to comment on the post and if they are not logged in there is a link instead asking them to log in to be able to leave a comment. 

Post detail page desktop

![The Final Whistle post detail page](./assets/readme-images/post-detail-page.png)

Post detail page tablet and mobile

![The Final Whistle post detail page tablet](./assets/readme-images/post-detail-tablet.png)
![The Final Whistle post detail page mobile](./assets/readme-images/post-detail-mobile.png)

Post detail page when not logged in 

![The Final Whistle post detail page not logged in](./assets/readme-images/post-detail-no-log-on.png)

Upvote and downvote arrows

![The Final Whistle post detail upvote and downvote](./assets/readme-images/upvote-downvote.png)

Number of comments icon

![The Final Whistle post detail number of comments](./assets/readme-images/num-of-comments.png)

### Login and register 

To give visitors of the site the ability to register for an account and to be able to sign in etc. I used a Django feature called allauth this makes it easier to set up security for users and streamlines the whole process.

Register form

![The Final Whistle create an account](./assets/readme-images/create-account-page.png)

Login form

![The Final Whistle login page](./assets/readme-images/login-page.png)

### Custom 404 page

I decided to add a customer 404 page that adds a bit of humour if the user navigates to an unknown URL, it stays within the football theme and I found the gif on 
[Giphy](https://giphy.com/happydogstickers).

404 page

![The Final Whistle 404 page](./assets/readme-images/404-page.png)

### Back to top button

For an ease of life function I included a back to top button the button only appears when the screen is scrolled down by more then 600 pixels. I did this so that when accessing the site on tablets and mobile phones it is easier to get back to the top of the page as there is quite a lot of screen scroll involved on these devices. I sourced the code for the button from [W3schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp).

Back to top button

![The Final Whistle back to top button](./assets/readme-images/back-to-top-button.png)

## Future Features

There is scope for a lot of expansion to The Final Whistle. The site as it is, is a minimal viable product, however there are features I would like to add in the future.

### Share button

A share button that appears on on the post detail page to enable users of the site to share the posts on other social media platforms which I believe would drive more traffic to the site and would add more functionality to the site as well

### Favourite posts

The ability to bookmark the users favourite posts to give easy access back to them, also within this feature the ability to bring up posts that the user has commented on as well so they can easily jump back into any conversations they may have been having.

### Search function

The ability to search through posts on the site by team, title, user, content and also tags that are on the posts as well. I believe this would add great functionality to the site and take more advantage of the tagging system as well.

### Social network sign in

The ability to use other social networks to log into the site this would bring the site in line with a lot of other websites and is a nice qulaity of life improvement.

### Password reset

To give users of the site the option to change their passwords and also reset their passwords as well if they forget what it is. When implementing this I would also add in confirmation emails to users of the site on succesfully creating their accounts.

### Team databse/model

I would also like to add a database for the football teams as well with individual pages that gives a brief overview and history for each club storeed in the database.

[Back to table of contents](#table-of-contents)

# Technologies used

## Languages

[HTML5](https://www.w3.org/standards/webdesign/htmlcss)

* This provides the basic structure and layout of the site 

[CSS3](https://www.w3.org/standards/webdesign/htmlcss)

* This provides the custom styling for site along with the Materialize framework

[JavaScript](https://www.javascript.com/)

* This provides the front-end scripting logic for the site 

[Python](https://www.python.org/)

* This provides the back-end logic for the site handling data on the back end working hand in hand with Django

[Git](https://git-scm.com/)

* This provides version control on the site 

## Frameworks

[Materialize](https://materializecss.com/)

* A modern responsive front-end framework based on Material Design

[Django](https://www.djangoproject.com/)

* Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Software used in production

[Balsamiq](https://balsamiq.com/)

* Used to build the wireframes for the project

[GitHub](https://github.com/)

* An internet hosting service used for version control. Used to host The Final Whistle repository and for the project board used for project management and user stories.

[Gitpod](https://www.gitpod.io/)

* Gitpod is a cloud development environment for teams to efficiently and securely develop software.

[Heroku](https://www.heroku.com/)

* Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. It is also where The Final Whistle is hosted as well.

[ElephantSql](https://www.elephantsql.com/)

* ElephantSQL installs and manages PostgreSQL databases for you.

[Cloudinary](https://cloudinary.com/)

* Cloudinary is an end-to-end image- and video-management solution for websites and mobile apps, covering everything from image and video uploads, storage, manipulations, optimizations to delivery.

[Lighthouse testing](https://web.dev/measure/?gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY3_TZb_Nus0EkkAH7Bb9l7_N7g3dud-sCco_igeA9lq3_387rdItZcaAmH5EALw_wcB)

* PageSpeed Insights (PSI) reports on the user experience of a page on both mobile and desktop devices, and provides suggestions on how that page may be improved.

[Responsive design](https://responsivedesignchecker.com/)

* This is a website that allows you to easily test if the site you have created is fully responsive across a range of devices.

[Google Chrome dev tools](https://developer.chrome.com/docs/devtools/)

* Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser.

[Wave web accessibility evaluation tool](https://wave.webaim.org/)

* WAVE® is a suite of evaluation tools that helps authors make their web content more accessible to individuals with disabilities. WAVE can identify many accessibility and Web Content Accessibility Guideline (WCAG) errors, but also facilitates human evaluation of web content.

[Excel](https://www.microsoft.com/en/microsoft-365/excel)

* Microsoft Excel is the industry leading spreadsheet software program, a powerful data visualization and analysis tool.

[Slack](https://slack.com/intl/en-gb)

* Slack is an instant messaging program designed by Slack Technologies and owned by Salesforce. I use Slack to communicate with other Code Institute students to troubleshoot problems or just to help when the going gets tough!

[Back to table of contents](#table-of-contents)

# Testing

## Manual testing 

I deployed the site straight away to Heroku to ensure the Django app was set up correctly and I kept on testing the functionality of the site throughout the whole process of building The Final Whistle. When the site was completed I then went onto testing the site with third-party applications and any errors that flagged have been corrected. The issues I found during production are listed below

### HTML tags rendering in cards on the home page

This was due to Summernote not being compatible with Materilize and the HTML tags where showing in the front end. To fix this I removed summernote from my site and just used the built in Django admin area.

### Pagination links not working

The pagination links at the bottom of the screen were not working correctly. During de-bugging I found this to be an issue within the HTML code and it not being typed correctly also there was a spelling mistake. These issues were rectified.

### Post detail page not rendering

The post detail page was not rendering in the front end due to a spelling mistake in the views.py code this was fixed and the issue was no more.

There has been extensive testing to ensure that no issues to my knowledge remain.

## Validation tests

### W3C HTML

I checked the HTML of the site using the [W3C HTML validation](https://validator.w3.org/) I checked each page individually with the images below

Home page HTML

![Home page html check](./assets/code-check-images/index-html-check.png)

Post detail HTML

![Post detail html check](./assets/code-check-images/post-detail-html-check.png)

My posts HTML

![My posts html check](./assets/code-check-images/my-posts-html-check.png)

Edit post HTML

![Edit post html check](./assets/code-check-images/edit-post-html-check.png)

Delete post HTML

![Delete post html check](./assets/code-check-images/delete-post-html-check.png)

Create post HTML

![Create post html check](./assets/code-check-images/create-post-html-check.png)

Login HTML

![login html check](./assets/code-check-images/login-html-check.png)

Logout HTML

![logout html check](./assets/code-check-images/logout-html-check.png)

Register HTML

![register html check](./assets/code-check-images/regitser-html-check.png)

404 HTML

![404 page html check](./assets/code-check-images/404-html-check.png)

### W3C CSS

I checked the CSS of the site using [W3C CSS](https://jigsaw.w3.org/css-validator/) no errors where shown that had to be corrected.

![CSS check](./assets/code-check-images/css-validated.png)

### JavaScript

I tested the javascript code using [jshint](assets/code-check-images/views-py-check.png) woth any errors found corrected the errors that were found was a few missing semicolons

![javascript check](./assets/code-check-images/jshint-screenshot.png)

### Python 

I used [The Code Institute](https://pep8ci.herokuapp.com/) python linter to check the python code within my site with any errors shown fixed.

Admin file

![admin.py check](./assets/code-check-images/admin-py-check.png)

Forms file

![forms.py check](./assets/code-check-images/forms-py-check.png)

Models file

![models.py check](./assets/code-check-images/models-py-check.png)

Views file

![views.py check](./assets/code-check-images/views-py-check.png)

## Lighthouse testing 

I used the lighthouse testing in Chrome dev tools to test my site also. When testing the site using lighthouse I found my page had a slow load time so I implemented changes to the site code regarding this. Firstly I moved any script elements that were in the head of my HTMl file to the bottom of the page and secondly I removed jQuery from my site as this was causing a lot of speed issues and updated the javascript code to ensure the same functionality was available.



# Deployment

# Credits and acknowledgements

The main image at the top of the readme is created on [Am I responsive](https://ui.dev/amiresponsive)

# Acknowledgements