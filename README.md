# Intro

Hello and welcome to the JUPUS coding challenge. Ideally, we'd love to give you a real task to work on in 
JUPUS production codebase but something like this just isn't possible given your & our 
time constraints. That's why we chose the next best thing: get you started on a fresh codebase.

We try to make this coding challenge comparable between candidates, that's why we've set
a time limit of 2 hours. Given the time constraints, you probably need to
rush through certain parts of the code: We know that and we will account for that. We don't
expect you to write 100% production grade code in this challange. If you need to take 
shortcuts where you'd ideally not want to take shortcuts, add a comment to the corresponding 
line. We try to assess your line of thinking and the way how you tackle tasks in this challenge.

Depending on your prior work expierence and your skill level, you are either finding this 
challange hard or maybe easy. Don't worry, we take your expierence and skill
level into consideration. From someone who is very expierenced, we certainly expect more
than from someone who is just getting started.


### Timeline
- Take your time to watch the video and to read and fully understand each task. 
- If there's something unclear, make a quick call to `0170 3800 460` to get everything sorted
out.
- Get yourself a timer and set it to 2 hours.
- Complete the tasks 1 & 2, zip the code and send it to `jannis.gebauer@jupus.de`.
- We will follow up with you to make an appointment for a code review. This is where we
discuss your implementation.

*Note: The email with your zipped code should arrive approx 2 hours and 30 minutes after you've
received the challenge. That gives you ~30 minutes to understand the tasks and to zip & send
everything. If you finish sooner, don't send it right away. Take your time to add rich
comments on every part of your code. This way we know that you've finished sooner but also
took the time for us to understand you better. If there's absolutely nothing left to say and
you still have time left, send it!*

### The stack

You'll find a fully working Django based project in this repository. The stack runs in Docker
containers, all held together by Docker Compose. You'll find a `base.html` template in the
root `templates/` folder that already includes basic styling provided by bootstrap. 

To get up and running, you'll first need to build the stack and start the database:

```shell
cd jupus-coding-challenge
docker-compose build
docker-compose up -d postgres
```

Give the database a couple of seconds to initialize, then do the initial migrations by 
running:

```shell
docker-compose run app python manage.py migrate
```

Done!

You should now be able to run the full stack by running:

```shell
docker-compose up
```

Go to [http://localhost:8000/](http://localhost:8000/) 

### Task

We need a way for users to register & authenticate with JUPUS but we hadn't had time to
implement this until now. We don't want to use any off the shelf libraries for this,
can you help us?

We need a way for:

**1) Users to register for a new account.**
- During registration, they should be able to set their first & last name, email address and password. 
- Make sure to make email addresses unique so that only one account exists per email address.
- Implement a way for users to confirm that they have access to the email address during registration.
You could send them an email which contains a magic link that confirms it, or you might want to send them
a code that they need to fill in. Choose what works best for you.
- Implement all the views you need to accomplish this task and then add a link to the page
that allows users to register for a new account.

**2) Users to log into their account.**
 - Registering is great, but we also need a way for users to authenticate with their newly created account (they need to be able to log in).
 - Implement all the views you need to accomplish this task and then add a link to the page
that allows users to log into their account.

**3) Users to log out of their account.**
- Now that we have registration and authentication out of our way, we need a way for users to
log out of their account.
- Implement all the views you need to accomplish this task and then add a link to the page
that allows users that are currently logged in to log out of their account.

**4) Users to reset their password.**
- There's a golden rule: Users always forget their passwords. Can you help them by providing
a way to reset their passwords?
- Implement all the views you need to accomplish this task and then add a link to the login
page for users to reset their password.

#### Follow up
*Note: Do this after you've completed all the tasks above and have submitted your results. 
This is not a part of the 2 hours tasks. Take it as a preparation for the followup call.* 

This is your time to shine! Sit down a couple of minutes and reflect on the code you just 
wrote.

Is this something you'd push to production? If not, what's missing? Would you rather use
a third party library for this? What are the benefits, what could go wrong? Are there better
way to implement this? If so, which one would you choose? Do you see any security issues
in the way you implemented it? What could go wrong?

Make a couple of notes on the questions above and use them as a preparation  for the follow 
up call where we review your code together and talk about those.