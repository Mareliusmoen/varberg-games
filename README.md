# Varberg MtG and boardgaming Network

## About
You can head to the live website here -----> LINK
The VBG Games site is a Magic the Gathering and boardgaming network, connecting players in the area in and around Varberg city on the west coast of Sweden. The main goal is to give different playgroups a common site to plan events, sell or buy games, cards and accessories, communicate with eacother. Since the gameshop in Varberg closed down there is no place for people who loves games to connect and meet with likeminded people who are engaged in the same hobby.

## User Experience Design
---
### Strategy
It was developed to help connect poeple in Varberg with likeminded players. The main coal was to allow users to join/create events, sell or buy products, and communicate about everything MtG and boardgames with the messaging service.
### Target Audience
This Django project is made for those that:
- Live in Varberg or Halland County and love Magic the Gathering and/or boardgames.
- Don't have a playgroup and is looking for players to play with.
- Have a playgroup that would like to grow and play with new players/playgroups.

### User Stories

#### First Time Visitor Goals

#### Frequent Visitor Goals

---

## Technologies used
---
- ### Languages:
    - **Python,** used to program the server-side of the project/website.
    - **HTML 5,** used to create the website.
    - **CSS 3,** used to style the website.
    - **JavaScript,** used for interactive elements of the website.
    
- ### Frameworks and libraries:
    - **Django,**
    - **Django Allauth,** 
    - **JQuery,**
    - **JQuery UI,**
- ### Databases:
    - **PostgreSQL,**
- ### Other tools:
    - **Adobe Illustrator,** for creating the background image.
    - **VS Code,** the IDE used to write all the code.
    - **Chrome DevTools,** used to debug issues and code during development.
    - **Pip3,** used as package manager to install all dependencies.
    - **Git,** used as version control system for all code.
    - **GitHub,** used to host projects source code.
    - **GitHub Projects,** used to keep track of User Stories and project progress during the development process.
    - **FontAwesome,** used for all icons in the project.
    - **Google Fonts,** used for the websites font.
    - **Postman,** used as messaging service.
---

## Features
---
**Landing page/Homepage**
A straightforward landing page with a short welcome-message, links to register or sign in right next to the welcome-message. There is also a nav-bar that only contains the options login or register before you sign in.

**Login**
The login asks the user to input their username and password, there is also a button if you forgot your passwrod to allow the user to reset it with their email address. Error/success messages pop-in to give the user feedback if the login was successful or if there was an error.

**Register new user**
Allows new visitors to register as users of the site, they need to type in: Username(required), Email(required), Password and confirm password(required), First Name and Last Name.

**Logged-in welcome**
Message that says 'Welcome, you're successfully signed in'. and a automatic Django message that confirms your login. Now that you're signed in as a authenticated user the nav-bar chenges and gives you access to all parts of the site: Events, Messaging, Marketplace and Logout.

**Log-out**
When the logged in user clicks the logout button in the nav bar the get redirected to a confirmation page that asks if the user is sure they want to sign out and the signout button to confirm. The nav-bar is there for the user regret their logout descion and head to another part of the site.

**Browse events**
This page lists all the available public events. at the top there is also a button for creating new events and a input field to type in a access-code if another user have giiven you access to one of their private events. If you type a correct code you're automatically added as a participant and you get a django message confirming, if it is not a correct access code you get a django error message explaining that.
Each event lists the event title, description, host, time and date, how many participants and 3 buttons: Communicate(opens a message-board for the specific event), join button(if you already have joined its a gray joined "button"), and if you are the creator of the event you have a delete button so you can delete the event. All events are sorted so the events that are happing soonest is displayed at the top if the list and sorted in descending order. There is also a code running in heroku everyday at midnight that deletes all events that happened during the day.

**Events communication**
When the communicate button for an event is clicked you're brought to a chat-like messaging page for the specific event, all users that have access to the event(for public-events all signed in users, for private events everyone with the access-code) can read and write messages in the communicate page. This feature makes it great for potential perticipants and particapants alike to ask questions to the creator or eachother, so that Q&A's that perhaps more than one user is wondering is answered and available in a logical place. The creator of each message has the opportunity to delete their own messages.
The communicate page also displays the event-information at the top of the page so that it's easily accessible.

**Create event**
The create-event page consists of a Title input-field, Description textarea input, datetime-picker and a checkbox to make a private event.
If you check the private event box, you as the creator of a private event will see the access-code for the specific event in the event when you head to your joined events section and this is the code you share with users you would like to join your event.

**Joined events**
This page lists all the events you have joined/created.
Each event lists the event title, description, host, time and date, how many participants and 3 buttons: Communicate(opens a message-board for the specific event), a gray joined "button", and if you are the creator of the event you have a delete button so you can delete the event. All events are sorted so the events that are happing soonest is displayed at the top if the list and sorted in descending order. There is also a code running in heroku everyday at midnight that deletes all events that happened during the day.

**Messages Inbox**

**Sent messages box**

**Deleted messages box**

**Archived messages box**

**Write new message**

**Message conversation**

**Marketplace all products for sale**

**Create a new product for sale**

**Your products for sale overview**



---

## Future Improvements and Features

---

## Design

### Color Scheme

The colorscheme was taken from the color-design book ADDCOLORDESIGNBOOKHERE, it was chosen for its calm blue colors with the playful orange and red complimenting-colors.

### Typography
From Google Fonts the 'Wellfleet' was chosen for it's playful look and easy readability, and the back up if not supported is standard 'monospace'.

### Imagery
Background image is created by me (Marelius Moen) in Adobe Illustrator, the design of the background is inspired by the occean which is a very important part of the coastal-city Varbergs image.

### Wireframes

---

## Information Architecture

### Database


### Data Modeling

**Entity relationship diagram**

---
## Testing

---
## Deployment
You find the deployed app here: LINK
The app is deployed to Heroku and the database to ElephantSQL.
### Heroku
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
- **Log in to Heroku** or create an account if required.
-
**click** the button labeled **New** from the dashboard in the top right corner, just below the header.
- From the drop-down menu **select "Create new app"**.
- **Enter a unique app name**. I combined my GitHub user name and the game's name with a dash between them (dnlbowers-battleship) for this project.
- Once the web portal shows the green tick to confirm the name is original **select the relevant region.** In my case, I chose Europe as I am in Sweden.
- When happy with your choice of name and that the correct region is selected, **click** on the **"Create app" button**.
- This will bring you to the project "Deploy" tab. From here, navigate to the **settings tab** and scroll down to the **"Config Vars" section**. 
- **Click** the button labelled **"Reveal Config Vars"** and **enter** the **"key" as port**, the **"value" as 8000** and **click** the **"add"** button.
- Scroll down to the **buildpacks section of the settings page** and click the button labeled **" add buildpack," select "Python," and click "Save Changes"**.
- **Repeat step 11 but** this time **add "node.js" instead of python**. 
   -  ***IMPORTANT*** The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
- Scroll back to the top of the settings page, and **navigate to the "Deploy" tab.**
- From the deploy tab **select Github as the deployment method**.
- **Confirm** you want to **connect to GitHub**.
- **Search** for the **repository name** and **click** the **connect** button next to the intended repository.
- From the bottom of the deploy page **select your preferred deployment type** by follow one of the below steps:  
   - Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.  
   - Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment. 


#### Create Database on ElephantSQL

1. Go to [ElephantSQL](https://www.elephantsql.com/) and create a new account.

2. Create a new instance of the database.

3. Select a name for your database and select the free plan.

4. Click "Select Region"

5. Select a region close to you.

6. Click "Review"

7. Click "Create Instance"

8. Click on the name of your database to open the dashboard.

9. You will see the dashboard of your database. You will need the URL of your database to connect it to your Django project.


### Local Deployment

## Credits
- Postman messeging service from: https://django-postman.readthedocs.io/en/latest/ is used to allow registered users to message eachother within the site.
- 

---

## Acknowledgments
