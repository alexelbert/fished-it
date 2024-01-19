# Fished It!

![Desktop homepage for Fished it! website](/docs/images/website.png)

[Live Site](https://fished-it-140783680cd5.herokuapp.com/)

## **Introduction**

Fished It is a web application designed for fishing enthusiasts. This application allows users to create an account, record information about fish they catch including add photos and information about their catches, and share these with a community if they want to. Fished It aims be a safe place to record information about catches that can be used later to inform fishing decisions.

This project is developed with a focus on providing a seamless user experience and foster a community for fishing enthusiasts.

---

## **UXD - User Experience Design**

Inspired by the principles of user-centred design, the development of Fished It is guided by the needs and wants of its users. The design process is categorized into five distinct planes:

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

---

## **The Strategy Plane**

### **Creator Goals**
- To create an easy-to-navigate website for fishing enthusiasts.
- To enable users to document and share their fishing experiences with ease.
- To build a platform where users can engage with each other through comments and interactions.

### **User Stories**

#### **Users**
- As a fishing enthusiast, I want to easily record details about my catches, including photos, fish type, weight, and size.
- As a user, I want to view catches shared by others.
- As a community member, I want to engage with other users by commenting on their posts.

#### **New Users**
- As a potential user, I want to understand the purpose of the site quickly.
- As a new visitor, I want the option to register easily and start using the platform.

---

## **The Scope Plane**

Given the complexity and short timeframe to incorparate all the desired functionality, the development process was divided into two parts:

### Phase 1: Basic functionality for the first prototype
- Core functionality including user registration, profile creation, and posting catches.
- Basic community features like viewing and commenting on shared catches.

### Phase 2: Better features for the future  
I want to continue working on this project and plan on incorporating the following functionality:
- Adding more information about a specific catch such as where the fish was caught and what were the weather conditions at the time.
- Automatic fish species recognition using existing detection models.
- Show a use dashboard with useful statistics to inform future fishing decisions.

---

## **The Structure Plane**

### **Colors and Fonts**
The visual design utilizes a color palette and fonts that resonate with the theme of fishing and outdoor activities. I wanted the website to feel modern and relaxed so kept a simple colour palette of whites and greens.

Fonts chosen:
- [Fredoka](https://fonts.google.com/specimen/Fredoka) for the logo: chunky and friendly sans serif to give a sense of a welcoming community
-  [Manrope](https://fonts.google.com/specimen/Manrope?query=Manrope) for the text body: modern and relaxed and subtle enough to not take over while still looking interesting.

### **Database Design**
The database schema is designed to support the core functionality of catches posted by the user, catches details, user profiles, and comments.


## **The Skeleton Plane**

### **Key Features**
- **User Registration and Authentication:** Simple process for new users to join the platform and delete their accounts and data if they wish to.
- **Catches:** Users can record their catches privately or choose to share their catches as public posts details about their catches with photos.
- **Community Engagement:** Features for users to view and comment each others catches.


## **The Surface Plane**

### **Interactive Elements**
The website includes interactive elements like forms for posting catches, comment sections, and user profile functionality.


## **Technologies Used**

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - Basic building block and structure of the content used for the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
    - Used for styling all the content of the website.
- [Bootstrap](https://getbootstrap.com)
    - For responsive frontend design.
- [Python](https://www.python.org) and [Django](https://www.djangoproject.com)
    - For the backend development and website functionality.
- [PostgreSQL](https://www.postgresql.org) in [ElephantSQL](https://www.elephantsql.com)
    - For database management.
- [Heroku](https://www.heroku.com)
    - For deploying and hosting the website.
- [Cloudinary](https://cloudinary.com)
    - Use for hosting images uploaded by the users (catches and profile pictures).
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used for all responsive content of the website, fetching the API and displaying the weather data. 
- [Font Awesome](https://fontawesome.com)
    - Used for icons in the action buttons for clarity and ease of use. 
- [Google Fonts](https://fonts.google.com/)
    - Used to obtain the fonts used across the website.
- [Dev.Opera](https://dev.opera.com/extensions/dev-tools/)
    - Used as a method of testing responsiveness and other issues/bugs with spacing and bugs.
- [GitHub](https://github.com/)
    - Used for storing pushed code.
- [Git](https://git-scm.com/)
    - Used to track changes in the code through  terminal commits and pushing from VS Code to GitHub. 
- [Visual Studio Code](https://code.visualstudio.com)
    - Used as a code editor.
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
    - Extension software used to fix spelling errors across the project.
- [JsHint](https://jshint.com/)
    - Used to check that the Javascript source code is compliant with the standards.   
- [W3C Markup Validation Service](https://validator.w3.org)
    - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - Used to validate CSS code.
- [Am I Responsive](http://ami.responsivedesign.is/)
    - Used to make responsive image for README.md file.
- [PageSpeed Insights](https://pagespeed.web.dev)
    - Used to assess performance of the website.


## **Testing** 

Extensive testing was done during development by checking all functionality in the website. 
HTML, CSS and JavaScript were all validated with (list of tools <TODO>).


## Deployment

This project was deployed using Heroku as a deployment platform and ElephantSQL hosts the postgreSQL database.

Steps for deployment:

### ElephantSQL
1. Create a database with postgres version 12 or higher to work with the django use din this project
2. Use database url to connect the application to the database instance

### Cloudinary
1. Create an account
...
<TODO>

### Heroku

1. Fork or clone this repository
2. Create a new Heroku app
3. Name your App and choose region then click "create app"
4. Go to settings then config vars <TODO>
6. Go to the Deploy tab, select GitHub and confirm by clicking Connect to GitHub.
7. Search for your repository name, when you have found it press connect to link your Heroku app to your repository.
8. Your can choose automatic deployment that rebuilds the app every time you push new code to your repository, or manually deploy which ever you prefer.
9. After it has finished building your project click view to see your project.


*Forking the GitHub Repository*

If you want to make any changes to your project without affecting it, you can make a copy by "forking" your original repository. This ensures the original remains unchanged.

1. Find the repository on Github
2. In the top right corner you can click on the Fork button
3. The repository has now been "Forked" and you now have a copy that you could work on

*Cloning the Github Repository*

Cloning your repository allows you to download a local version of the repository to work on, very useful to backup your work.

1. Navigate to the repository
2. Press the "Code" button
3. Select the "Local" tab in the dropdown menu
4. Copy the HTTPS link provided
5. Type "git clone" and paste your link
6. Press enter and you will now have a local clone of your repository
7. To view the application locally, fill in the required variables in the `env_sample.py` file and rename it to `env.py` (make sure to never share files with sensitive data, such as this one) <REVIEW>

---

## Credits

Producing this website i have used several resources for inspiration and researched for help.

The following websites was used for inspiration and research:
- ...
<TODO>

Used code from these resources, credited as comments code:

- Blog project <TODO>


Other websites i used for the content:

- Credited in the HTML and CSS code is from the blog project which I used as inspiration and as a base for my application.

## Acknowledgements

I want to thank my mentor Harry Dhillon for giving support through the project and my girlfriend Sabrina Fonseca Pereira for her support and feedback.