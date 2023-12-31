# Varberg MtG and boardgaming Network

## About
You can head to the live website here -----> [VGB Games](https://vareberg-games-a44cb52aa87b.herokuapp.com/) <br>
The VBG Games site is a Magic the Gathering and boardgaming network, connecting players in the area in and around Varberg city on the west coast of Sweden. The main goal is to give different playgroups a common site to plan events, sell or buy games, cards and accessories, communicate with eacother. Since the gameshop in Varberg closed down there is no place for people who loves games to connect and meet with likeminded people who are engaged in the same hobby.
![Indexpage screenshot](static/images/index-screenshot.png)
## Table of Contents

- [Varberg MtG and Boardgaming Network](#varberg-mtg-and-boardgaming-network)
  - [About](#about)
  - [User Experience Design](#user-experience-design)
    - [Strategy](#strategy)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
  - [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Databases](#databases)
    - [Other tools](#other-tools)
  - [Features](#features)
    - [Landing page/Homepage](#landing-pagehomepage)
    - [Login](#login)
    - [Register new user](#register-new-user)
    - [Logged-in welcome](#logged-in-welcome)
    - [Log-out](#log-out)
    - [Browse events](#browse-events)
    - [Events communication](#events-communication)
    - [Create event](#create-event)
    - [Joined events](#joined-events)
    - [Messages Inbox](#messages-inbox)
    - [Sent messages box](#sent-messages-box)
    - [Deleted messages box](#deleted-messages-box)
    - [Archived messages box](#archived-messages-box)
    - [Write new message](#write-new-message)
    - [Message conversation](#message-conversation)
    - [Marketplace all products for sale](#marketplace-all-products-for-sale)
    - [Create a new product for sale](#create-a-new-product-for-sale)
    - [Your products for sale overview](#your-products-for-sale-overview)
  - [Future Improvements and Features](#future-improvements-and-features)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
    - [Database](#database)
    - [Data Modeling](#data-modeling)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Create Database on ElephantSQL](#create-database-on-elephantsql)
    - [Local Deployment](#local-deployment)
  - [Credits](#credits)
  - [Acknowledgments](#acknowledgments)

## User Experience Design
---
### Strategy
It was developed to help connect poeple in Varberg with likeminded players. The main coal was to allow users to join/create events, sell or buy products, and communicate about everything MtG and boardgames with the messaging service.
### Target Audience
This Django project is made for those that:
- Live in Varberg or Halland County and love Magic the Gathering and/or boardgames.
- Don't have a playgroup and is looking for players to play with.
- Have a playgroup that would like to grow and play with new players/playgroups.

### Responsiveness

![Responsiveness screenshot](static/images/responsiveness-screenshot.png)

### User Stories

#### First Time Visitor Goals
- **Understand the Purpose**: A first-time visitor should quickly grasp the purpose of your project. We've included a clear, concise introduction on the home page to immediately communicate what the site is about.
- **Navigate Easily**: The site should be intuitive to navigate. We've designed a straightforward navigation bar and included a site map in the footer to assist with this.
- **Engage With Content**: Visitors should find it easy to interact with your site. Whether they're playing a game, reading about the team, or sending a message through the contact form, the user journey has been designed to be as seamless as possible.
- **Find Help**: If visitors encounter any issues or have questions, they should be able to find help quickly. We've included a comprehensive FAQ page and easy-to-find contact information to ensure user queries are promptly addressed.

#### Frequent Visitor Goals
- **Discover Public Events**: Frequent visitors should be able to easily find and learn about public events.
- **Join Public Events**: Once they've discovered an event they're interested in, users should be able to join these public events with ease.
- **Get Access Codes for Private Events**: Regular users should have a clear process to get access codes for private events.
- **Join Private Events**: With an access code, users should be able to join private events smoothly.
- **Engage in Discussions**: Users should be able to actively participate in discussions, ask questions and communicate on event pages.
- **Browse Products**: Visitors should be able to easily browse Magic the Gathering products, board games, and accessories listed for sale.
- **Purchase Products**: Once a product is selected, the purchase process should be clear and straightforward.
- **Create Product Listings**: Sellers should be able to list their products in the marketplace efficiently.
- **Edit Product Listings**: Sellers should be able to update their product listings as needed, such as changing price or description.
- **Mark Products as Sold**: Once a product is sold, sellers should be able to easily mark it as such in the marketplace.
- **Use MTG Card Database**: Users should be able to connect their product listings to the card in the MTG card database in a user-friendly manner.
- **Send Messages to Other Users**: Frequent visitors should be able to easily initiate and maintain communication with other users.
- **Plan Events with Other Users**: The platform should facilitate users planning events with each other through the messaging system.

---

## Technologies used
---
- ### Languages:
    - **Python:** Powers the server-side logic.
    - **HTML 5:** Structures the website content.
    - **CSS 3:** Styles and beautifies the website.
    - **JavaScript:** Drives website interactivity.
    
- ### Frameworks and Libraries:
    - **Django:** The core web framework.
    - **Django Allauth:** Manages user authentication.
    - **JQuery & JQuery UI:** Simplifies JavaScript operations and UI interactions.
    - **JQuery UI Datepicker + timepicker:** Handles date and time selections.
    - **Django Autocomplete Light:** Enables user search autocomplete functionality.
    - **Psycopg-2:** Interfaces with the PostgreSQL database.
    
- ### Databases:
    - **PostgreSQL:** Stores application data.

- ### Tools:
    - **Adobe Illustrator:** Creates custom graphics.
    - **VS Code:** The chosen Integrated Development Environment (IDE).
    - **Chrome DevTools:** Debugs and profiles code.
    - **Pip3:** Manages Python package dependencies.
    - **Git:** Controls version history.
    - **GitHub:** Hosts the project's source code.
    - **GitHub Projects:** Tracks project progress and user stories.
    - **Heroku:** is used for deployment of the project.
    - **FontAwesome:** Supplies the website's icons.
    - **Google Fonts:** Provides the website's typography.
    - **Postman:** Facilitates internal messaging service.

## Features
The whole page is responsive for different screensizes AND browser based zoom, wich makes the site very smooth to operate no matter how big or small you like the text and content.
---
**Landing page/Homepage** <br>
A straightforward landing page with a short welcome-message, links to register or sign in right next to the welcome-message. There is also a nav-bar that only contains the options login or register before you sign in.
![Indexpage screenshot](static/images/index-screenshot.png)

**Login**<br>
The login asks the user to input their username and password, there is also a button if you forgot your passwrod to allow the user to reset it with their email address. Error/success messages pop-in to give the user feedback if the login was successful or if there was an error.
![Signin page screenshot](static/images/signin-screenshot.png)

**Register new user**<br>
Allows new visitors to register as users of the site, they need to type in: Username(required), Email(required), Password and confirm password(required), First Name and Last Name.
![Signup page screenshot](static/images/signup-screenshot.png)

**Logged-in welcome**<br>
Message that says 'Welcome, you're successfully signed in'. and a automatic Django message that confirms your login. Now that you're signed in as a authenticated user the nav-bar chenges and gives you access to all parts of the site: Events, Messaging, Marketplace and Logout.
![Signed in page screenshot](static/images/signedin-screenshot.png)

**Log-out**<br>
When the logged in user clicks the logout button in the nav bar the get redirected to a confirmation page that asks if the user is sure they want to sign out and the signout button to confirm. The nav-bar is there for the user regret their logout descion and head to another part of the site.
![Sign out page screenshot](static/images/sign-out-screenshot.png)

**Browse events**<br>
This page lists all the available public events. at the top there is also a button for creating new events and a input field to type in a access-code if another user have giiven you access to one of their private events. If you type a correct code you're automatically added as a participant and you get a django message confirming, if it is not a correct access code you get a django error message explaining that.
Each event lists the event title, description, host, time and date, how many participants and 3 buttons: Communicate(opens a message-board for the specific event), join button(if you already have joined its a gray joined "button"), and if you are the creator of the event you have a delete button so you can delete the event. All events are sorted so the events that are happing soonest is displayed at the top if the list and sorted in descending order. There is also a code running in heroku everyday at midnight that deletes all events that happened during the day.
![upcoming events screenshot](static/images/upcoming-events-screenshot.png)

**Events communication**<br>
When the communicate button for an event is clicked you're brought to a chat-like messaging page for the specific event, all users that have access to the event(for public-events all signed in users, for private events everyone with the access-code) can read and write messages in the communicate page. This feature makes it great for potential perticipants and particapants alike to ask questions to the creator or eachother, so that Q&A's that perhaps more than one user is wondering is answered and available in a logical place. The creator of each message has the opportunity to delete their own messages.
The communicate page also displays the event-information at the top of the page so that it's easily accessible.
![Event conversation screenshot](static/images/event-conversation-screenshot.png)

**Create event**<br>
The create-event page consists of a Title input-field, Description textarea input, datetime-picker and a checkbox to make a private event.
If you check the private event box, you as the creator of a private event will see the access-code for the specific event in the event when you head to your joined events section and this is the code you share with users you would like to join your event.
![Create event screenshot](static/images/create-event-screenshot.png)

**Joined events**<br>
This page lists all the events you have oined/created.
Each event lists the event title, description, host, time and date, how many participants and 3 buttons: Communicate(opens a message-board for the specific event), a gray joined "button", and if you are the creator of the event you have a delete button so you can delete the event. All events are sorted so the events that are happing soonest is displayed at the top if the list and sorted in descending order. There is also a code running in heroku everyday at midnight that deletes all events that happened during the day.
![Joined events screenshot](static/images/joined-events-screenshot.png)

**Edit events**<br>
This part of the event app implements a robust and intuitive event editing functionality specifically designed for the event creators. This allows you to have full control over the event details and make adjustments as necessary.
![Edit event screenshot](static/images/edit-event-screenshot.png)

**Messages Inbox**<br>
The inbox feature in the project provides a centralized location for users to manage and view their received messages. It allows registered users to communicate with each other within the site, facilitating efficient and convenient communication.
![Inbox screenshot](static/images/inbox-screenshot.png)

**Sent messages box**<br>
The sent message box feature in the project allows users to keep track of the messages they have sent to other users within the site. It provides a convenient way to view and manage sent messages, ensuring that users have a complete record of their communication history.
![Sentbox screenshot](static/images/sentbox-screenshot.png)

**Deleted messages box**<br>
The deleted messages box feature in the project provides a dedicated space for users to store and manage their deleted messages. It offers a convenient way to recover accidentally deleted messages or permanently remove unwanted messages from the system.
![delete box screenshot](static/images/deleted-msg-screenshot.png)

**Archived messages box**<br>
The archived messages box feature in the project offers users a dedicated space to store and manage their archived messages. It provides a convenient way to declutter the main inbox while still retaining access to important or historical conversations.
![Archived box screenshot](static/images/archived-box-screenshot.png)

**Write new message**<br>
The write new message feature in the project allows users to compose and send new messages to other users within the site. It provides a convenient and intuitive interface for initiating and engaging in conversations.
![Write new message screenshot](static/images/write-message-screenshot.png)

**Message conversation**<br>
The message conversation feature in the project allows users to view and manage their conversations with other users in a streamlined and intuitive interface. This feature is designed to facilitate seamless and efficient communication within the site.
![Conversation screenshot](static/images/conversation-screenshot.png)

**Marketplace all products for sale**<br>
The marketplace feature in the project serves as a platform where users can view all available products for sale and display their own products. It provides a seamless and user-friendly interface for exploring, comparing, selling and purchasing products.
![All product for sale screenshot](static/images/products-for-sale-screenshot.png)

**Create a new product for sale**<br>
The create new product for sale feature in the project allows users to list their own products for sale in the Marketplace. It offers an intuitive interface for users to enter product details and create new listings.
![Create new product for sale screenshot](static/images/new-product-screenshot.png)

**Your products for sale overview**<br>
The user's products for sale overview feature in the project provides users with a comprehensive dashboard to manage all their product listings in the marketplace.
![Your products for sale overview screenshot](static/images/your-products-screenshot.png)

---

## Future Improvements and Features
---
**Social media verification (facebook, Google...)** <br>
In future releases I would like to add that you can sign up to the site with google, facebook or similar account.

**Activate and setup email confirmation** <br>
Add email confirmation when user signs up for the site, to make sure the user is a real person.

**Add email notifications** <br>
Add email notifications for new messeges, users joining your events, users show interest in your product for sale.

**Add contact seller functionality** <br>
 Add a 'Contact Seller' button on product listings. This will redirect users to a pre-filled new message form, making communication between buyers and sellers quicker and easier.

**Add on-site notification system** <br>
Add a notification system for new messeges, users joining your events, users show interest in your product for sale.

**Design and make a logo in Adobe Illustrator** <br>
Make a logo in Adobe Illustrator that reflects the brand identity of the site.

**Make the homepage for logged in users** <br>
Make the homepage for logged in users more appealing and attractive, and add functionality like lists of joined events, your products for sale, new messages, etc.

**Sort products in the markedplace by Category** <br>
Add a filter option in the marketplace to sort products by category.

**Sort products in the markedplace by sold/available** <br>
Add a filter option in the marketplace to sort products by sold/available.

**Add a display next to the navbar that shows which user is logged in** <br>
Add a display next to the navbar that makes it easy for the user to make sure he/she is logged in correctly.

---

## Design
The site's design features a calming blue color scheme, accented with playful hues of orange and red. The background illustraion are ment to represent the occean which is a an important part of the coastal city of Varberg, enhancing the visual appeal and providing the "feeling" of the coast. The layout and responsiveness of the site are based on Bootstrap framework

### Color Scheme

The colorscheme was taken from the color-design book Papier Tigre Color Inspiration volume 2, it was chosen for its calm blue colors with the playful orange and red complimenting-colors.
The RGB codes are: <br>
![Colorscheme](static/images/colorscheme.png)

### Typography
From Google Fonts the 'Wellfleet' was chosen for it's playful look and easy readability, and the back up if not supported is standard 'monospace'.

### Imagery
Background image is created by me (Marelius Moen) in Adobe Illustrator, the design of the background is inspired by the occean which is a very important part of the coastal-city Varbergs image. These visuals add visual interest and enhance the user experience, making the site more engaging and visually appealing.

### Wireframes
Before starting the development of the VBG Games site, wireframes were created to plan and visualize the layout and structure of the different pages. These wireframes served as a blueprint for the design process, ensuring a cohesive and user-friendly interface.

<details>

![Wireframe design](static/images/wireframes/20231121_101654.jpg)

![Wireframe design](static/images/wireframes/20231121_101707.jpg)

![Wireframe design](static/images/wireframes/20231121_101721.jpg)

![Wireframe design](static/images/wireframes/20231121_101743.jpg)

![Wireframe design](static/images/wireframes/20231121_101753.jpg)

![Wireframe design](static/images/wireframes/20231121_101812.jpg)

![Wireframe design](static/images/wireframes/20231121_101824.jpg)
</details>
---

## Information Architecture

### Database
Our application uses the PostgreSQL database to handle data persistence. 

### Data Modeling

**Allauth**
We use the Django Allauth package to manage user authentication. It was migrated to PostgreSQL database.

### **POSTMAN MESSAGING**
#### Message

A message between a User and another User or an AnonymousUser.

##### Fields

| Name                 | Database Key         | Field Type              | Validation                                              |
| -------------------- | -------------------- | ----------------------- | ------------------------------------------------------- |
| Sender               | sender               | ForeignKey to User      | on_delete=models.CASCADE                               |
| Recipient            | recipient            | ForeignKey to User      | on_delete=models.CASCADE, related_name='recipient_messages'|
| Subject              | subject              | CharField               | max_length=255                                         |
| Body                 | body                 | TextField               | None                                                    |
| Email                | email                | EmailField              | blank=True                                              |
| Parent               | parent               | ForeignKey to 'self'    | on_delete=models.CASCADE, related_name='next_messages', null=True, blank=True|
| Thread               | thread               | ForeignKey to 'self'    | on_delete=models.CASCADE, related_name='child_messages', null=True, blank=True|
| Sent at              | sent_at              | DateTimeField           | default=now                                             |
| Read at              | read_at              | DateTimeField           | null=True, blank=True                                   |
| Replied at           | replied_at           | DateTimeField           | null=True, blank=True                                   |
| Sender Archived      | sender_archived      | BooleanField            | default=False                                           |
| Recipient Archived   | recipient_archived   | BooleanField            | default=False                                           |
| Sender Deleted At    | sender_deleted_at    | DateTimeField           | null=True, blank=True                                   |
| Recipient Deleted At | recipient_deleted_at | DateTimeField           | null=True, blank=True                                   |
| Moderation Status    | moderation_status    | CharField               | max_length=1, choices=STATUS_CHOICES, default=STATUS_ACCEPTED|
| Moderation By        | moderation_by        | ForeignKey to User      | on_delete=models.CASCADE, related_name='moderated_messages', null=True, blank=True|
| Moderation Date      | moderation_date      | DateTimeField           | null=True, blank=True                                   |
| Moderation Reason    | moderation_reason    | CharField               | max_length=120, blank=True                              |

##### Methods

- `is_pending()`: Tell if the message is in the pending state.
- `is_rejected()`: Tell if the message is in the rejected state.
- `is_accepted()`: Tell if the message is in the accepted state.
- `is_new`: Tell if the recipient has not yet read the message.
- `is_replied`: Tell if the recipient has written a reply to the message.
- `get_absolute_url`: Deprecated. Usage is deprecated since v3.3.0.
- `quote(format_subject, format_body=None)`: Return a dictionary of quote values to initiate a reply.
- `get_replies_count()`: Return the number of accepted responses.
- `clean()`: Check some validity constraints.
- `clean_moderation(initial_status, user=None)`: Adjust automatically some fields, according to the status workflow.
- `clean_for_visitor()`: Do some auto-read and auto-delete, because there is no one to do it (no account).
- `update_parent(initial_status)`: Update the parent to actualize its response state.
- `notify_users(initial_status, site, is_auto_moderated=True)`: Notify the rejection (to sender) or the acceptance (to recipient) of the message.
- `get_dates()`: Get some dates to restore later.
- `set_dates(sender_deleted_at, recipient_deleted_at, read_at)`: Restore some dates.
- `get_moderation()`: Get moderation information to restore later.
- `set_moderation(status, by_id, date, reason)`: Restore moderation information.
- `auto_moderate(moderators)`: Run a chain of auto-moderators.

#### PendingMessage (Proxy Model)

A proxy to Message, focused on pending objects to accept or reject.

##### Fields

Same as Message

##### Methods

- `set_accepted()`: Set the message as accepted.
- `set_rejected()`: Set the message as rejected.

### **MARKETPLACE**

#### Category

Represents a product category.

##### Fields
| Name | Database Key | Field Type | Validation    |
| ---- | ------------ | ---------- | ------------- |
| Name | name         | CharField  | max_length=100|


##### Methods

- `__str__()`: Returns the name of the category.

#### Product

Represents a product in the e-commerce system.

##### Fields
| Name          | Database Key  | Field Type              | Validation                                     |
| ------------- | ------------- | ----------------------- | ---------------------------------------------- |
| Title         | title         | CharField               | max_length=200                                 |
| Description   | description   | TextField               | None                                           |
| Price         | price         | DecimalField            | max_digits=10, decimal_places=2                |
| Category      | category      | ForeignKey to Category  | on_delete=models.CASCADE                       |
| Seller        | seller        | ForeignKey to User      | on_delete=models.CASCADE                       |
| Created At    | created_at    | DateTimeField           | auto_now_add=True                              |
| Card Name     | card_name     | CharField               | max_length=255, null=True, blank=True          |
| Card Image URL| card_image_url| URLField                | null=True, blank=True                          |
| Sold          | sold          | BooleanField            | default=False                                  |

### **EVENTS**

#### Event

Represents an event with details such as title, description, date, and participants.

##### Fields
| Name          | Database Key  | Field Type              | Validation                                |
| ------------- | ------------- | ----------------------- | ----------------------------------------- |
| Title         | title         | CharField               | max_length=100                            |
| Description   | description   | TextField               | None                                      |
| Date          | date          | DateTimeField           | None                                      |
| Is Private    | is_private    | BooleanField            | default=False                             |
| Creator       | creator       | ForeignKey to User      | on_delete=models.CASCADE                  |
| Participants  | participants  | ManyToManyField to User | related_name='events_attending'           |
| Access Code   | access_code   | CharField               | max_length=10, null=True, blank=True      |
| Comments      | comments      | ManyToManyField to Comment | blank=True, related_name='event_comments' |

##### Methods

- `has_already_passed()`: Returns True if the event date has already passed.

#### EventParticipant

Links users to events they are participating in.

##### Fields

| Name  | Database Key | Field Type         | Validation                 |
| ----- | ------------ | ------------------ | -------------------------- |
| Event | event        | ForeignKey to Event | on_delete=models.CASCADE  |
| User  | user         | ForeignKey to User  | on_delete=models.CASCADE  |


#### Comment

Represents a comment on an event.

##### Fields

| Name       | Database Key | Field Type              | Validation              |
| ---------- | ------------ | ----------------------- | ----------------------- |
| Event      | event        | ForeignKey to Event     | on_delete=models.CASCADE|
| User       | user         | ForeignKey to User      | on_delete=models.CASCADE|
| Text       | text         | TextField               | None                    |
| Created At | created_at   | DateTimeField           | auto_now_add=True       |

##### Methods

- `__str__()`: Returns a formatted string representation of the comment.

#### Utility Function

##### `generate_access_code()`

Generates a random access code consisting of 10 digits connected to the specific event.

```
python
def generate_access_code():
    return ''.join(secrets.choice(string.digits) for _ in range(10)) 
```

---
## Testing
### Manual testing
Manual tests where done to make sure all user experience features work as intended.

| Test Case                        | Description | Expected Outcome | Successful |
| -------------------------------- | ----------- | ---------------- | ---------- |
| See Public Events                | User is able to view all the public events. | A list of public events is displayed. | ✅ |
| Join Public Events               | User can join a public event. | User is added to the event's participants. | ✅ |
| Create Public Events             | User can create a new public event. | A new public event is created and visible to all users. | ✅ |
| Create Private Events            | User can create a new private event. | A new private event is created and visible only to invited users. | ✅ |
| Join Private Events with Access Code | User can join a private event with a valid access code. | User is added to the event's participants upon entering a valid access code. | ✅ |
| See Messages Received            | User can view all received messages. | A list of received messages is displayed. | ✅ |
| See Messages Sent                | User can view all sent messages. | A list of sent messages is displayed. | ✅ |
| See Messages Archived            | User can view all archived messages. | A list of archived messages is displayed. | ✅ |
| See Messages Deleted             | User can view all deleted messages. | A list of deleted messages is displayed. | ✅ |
| Send New Messages                | User can send new messages to other users. | The message is successfully sent and appears in the recipient's received messages. | ✅ |
| Reply to Message in Conversation | User can reply to a message within a conversation thread. | The reply is successfully sent and appears in the conversation thread. | ✅ |
| See Products for Sale            | User can view all products for sale. | A list of products for sale is displayed. | ✅ |
| See Which Products Are Sold      | User can view all sold products. | A list of sold products is displayed. | ✅ |
| See the Products You Have Put Up for Sale | User can view all the products they have put up for sale. | A list of the user's products for sale is displayed. | ✅ |
| Create New Product Listing for Sale | User can create a new product listing for sale. | A new product listing is created and visible to all users. | ✅ |
| Register as New User             | User can register a new account. | A new account is successfully created for the user. | ✅ |
| Sign In with Registered User     | User can sign in with their registered account. | User is successfully signed in to their account. | ✅ |
| Sign Out with Registered User    | User can sign out from their registered account. | User is successfully signed out from their account. | ✅ |

### PEP8
To ensure the quality and readability of the Python code in this project, all Python files were checked with the PEP8 linter provided by Code Institute. This tool helps enforce the PEP8 style guide, which is widely accepted in the Python community for coding standards.

The PEP8 linter checks for issues like line lengths, whitespace usage, variable naming conventions, docstrings and more. The code in this project has passed the PEP8 linter test without any errors, which means that it adheres to these standards, making it easier to read and maintain.

You can check the PEP8 linter here: [PEP8 linter](https://pep8ci.herokuapp.com/)

### Validators

#### CSS Validator
The CSS code in this project was tested using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) and passed without any errors.

#### HTML Validator
The HTML code in this project was tested using the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri) and passed without any errors.

#### Dev Tools Lighthouse
The site has been tested using Lighthouse and has achieved the following scores:

- Performance: 94
- Accessibility: 95
- Best Practices: 100
- SEO: 100

These scores indicate the site's high performance, accessibility, adherence to best practices, and search engine optimization. 
![Lighthouse test results screenshot](static/images/Lighthouse-screenshot.png)

### Deployed vs Local
The final version of the Full-Stack application was deployed to Heroku, while the database was deployed to ElephantSQL. This deployed version was thoroughly tested to ensure its functionality matches the version in the development environment.

Both the deployed and local versions were tested across various scenarios and functionalities as documented in this 'Testing' section. The tests confirmed that the deployed version of the application behaves as expected and mirrors the development version.

It's important to note that consistent code quality was maintained throughout the project. This was ensured by adhering to the PEP8 style guide, facilitated by the PEP8 linter provided by Code Institute. 

For further details on the deployment process, refer to the 'Deployment' section below.


## Deployment
You find the deployed app here: LINK
The app is deployed to Heroku and the database to ElephantSQL.
### Heroku
The project was deployed to [Heroku](https://www.heroku.com) using the below procedure:-    
  
- **Log in to Heroku** or create an account if required.
- **click** the button labeled **New** from the dashboard in the top right corner, just below the header.
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

1. Clone the repository.

    - ```git clone https://github.com/Mareliusmoen/varberg-games.git```

2. Go to the ```varberg-games``` directory.

    - ```cd varberg-games``` (or your path to the project)

3. Create a virtual environment.

    - ```python3 -m venv venv```

    - ```source venv/bin/activate```

4. Install all dependencies.

    - ```pip install -r requirements.txt```

5. Create a ```env.py``` file.

    - ```touch env.py```

6. Add the following lines to ```env.py```:

    - ```import os```
    - ```os.environ["SECRET_KEY"]``` = your secret key.
    - ```os.environ["DEBUG"]``` = "True" or "False" depending on whether you are in development or production.
    - ```os.environ["DEVELOPMENT"]``` = "True" or "False" depending on whether you are in development or production.
    - ```os.environ["ALLOWED_HOSTS"]``` = your domain name.
    - ```os.environ["DATABASE_URL"]``` = your database url.

7. Create and migrate the database.

    - ```python manage.py makemigrations```
    - ```python manage.py migrate```

8. Create the superuser.

    - ```python manage.py createsuperuser```

9. Run the server.

    - ```python manage.py runserver```

10. Access the website by the link provided in terminal. Add ```/admin/``` at the end of the link to access the admin panel.

## Bugs

### Unfixed bugs
- Recipient user autocomplete in new message form pushes all content to the left, I set display to none to hide the text but the div still pops in at the right side of the screen.

- Unread message count as a integer in the messages text of the navbar button.

- Undeleting messages after they have been deleted. The postman code provided did not pass the PEP8 linter so I needed to reformat parts of the code to fit the 79 character maximum per line, and I havent found the bug that causes this not function anymore.

- Mark messages as read/unread. The postman code provided did not pass the PEP8 linter so I needed to reformat parts of the code to fit the 79 character maximum per line, and I havent found the bug that causes this not function anymore.

- On certain screensizes the buttons for edit, and delete product are a little bit off vertically.

- The hour and minute sliders of the datetimepicker are in some way hidden, you can click where they are supposed to be shown and it registers your choice, but the bars themselves are not visible.

## Credits
- [Postman](https://django-postman.readthedocs.io/en/latest/) is used to allow registered users to message eachother within the site. Thanks for providing a almost 'out-of-the-box' experience, so most of this code is not written by me only modified to fit the needs of this project.
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) and it's detailed documentation made the frontend part of the programming very smooth and easy.
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html) and it's detailed documentation made the creation of the background very smooth and easy.
- This [Stackoverflow post](https://stackoverflow.com/questions/13932653/increase-displaying-time-of-django-messages) for explaining how to make the Django response messages be auto deleted after a set time.
- [GitHub](https://github.com/) for storing the source code and make the Agile process streamlined and more efficient.
- [Heroku](https://www.heroku.com/) for hosting the project and allowing me to add scheduled tasks to improve user experience.
- [Papier Tigre](https://www.papiertigre.fr/en/books/1743-color-inspiration-volume-2.html) for making the smartest color inspiration books with premade color schemes for ease implementation in projects.
- [FontAwesome](https://fontawesome.com/) for providing the website's icons for free.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) for providing the authentication system for the site.
- [ElephantSQL](https://www.elephantsql.com/) for the free hosting of the database.
- [Jquery](https://jquery.com/) for providing the JavaScript library for the site.
- [JQuery UI](https://jqueryui.com/) for providing the JavaScript tools to make the site more interactive.
- [Google Fonts](https://fonts.google.com/) for providing the free fonts for the site.
- [Microsoft VSCode](https://code.visualstudio.com/) for providing the best IDE I have used and making the creation of this project very enjoyable.
- [Real Favicon Generator](https://realfavicongenerator.net/) for providing the favicon for the site for free in a effortless way.
- [Code Institute](https://codeinstitute.net/) for providing the guidence through different walkthrough projects for setting up a Django project. Some of the base setup for this project is from their walkthroughs.
- [Trent Richardson](https://trentrichardson.com/examples/timepicker/) for providing the timepicker for the site, and giving me the solution to my biggest hurdle of the event application, integrating time to the date picker.


---

## Acknowledgments
- Thanks to my mentor [Alex K.](https://github.com/lexach91), for patiently listening to my plans and helping out when problems arose.
- A special thanks to David Calikes for his time, enthusiasm and support during the development of this project.
- Thanks to my friends and family for patience and support during this project, when I was submerge in the code and needed help with everything else you stepped up.