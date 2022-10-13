# Chat Application

This is a chat application made using Python Flask (and Flask_SocketIO), HTML, CSS, some JS and MongoDB, which is also used in popular chat applications such as Discord.

## Basic Overview Functionalities

The image below is the actual chat itself (The first one shows when you're logged out and the second is when you're logged in). This uses MongoDB where I have inserted the data whenever it is entered into the site.
#### When logged out:
![image](https://user-images.githubusercontent.com/49610482/195600435-bffee01b-7fc2-4d68-95bf-5659a1cd525a.png)

#### When logged in:
![image](https://user-images.githubusercontent.com/49610482/195600917-ce256d6f-2fa9-432b-8329-f939b671426a.png)


Additionally, the image below shows the register and login page.
#### Register Page:
![image](https://user-images.githubusercontent.com/49610482/195601216-9c49cf7b-3db1-42ce-994c-7a4f960649e9.png)

#### Login Page (Design will be changed later, scroll to [Future Plans](#future-plans):
![image](https://user-images.githubusercontent.com/49610482/195601591-2882ff78-bb58-4280-9522-6849a51c0e8c.png)

## Relatively advanced backend functionalities

The program is encrypted using the SHA256 Cryptographic Encryption Hash, making it impossible for hackers to decrypt the passwords, and is also such that the database admins cannot access the passwords (protecting the users' privacies).

On top of this, the website uses Flask's sessions to ensure that users who have logged in already cannot access the login and register page (as it unnecesary). This is often seen on many large-scale websites as it also reduces traffic to webpages.

As for the live-time updates, I am using SocketIO, a commonly used module for live updates in the chat (while also having to use javascript to update it on the user's page)


## Future Plans

In the future, I plan to add this onto a portfolio website template that I am working on. This means I will also be cleaning up on the design so that anybody could basically copy-paste this code (of course, with rights from me).

In addition to simple CSS updates, I also plan to add in recaptcha and possibly a multiple group chats sort of thing for easier communication (as this is currently accessible to all).

Lastly, I am planning to add a swear word filter so that we can keep it PG-13.
