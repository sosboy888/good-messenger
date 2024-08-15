# The Good Messenger
##  A Python messenger Proof of concept using FastAPI and Postgres.

## Description
This is a complete backend for a real-time messaging system. It has a centralized architecture and relies on a central server that hosts all messages(like Instagram and Facebook Messenger).  It has been built with a vision to handle high load, but it is worth noting that I did not get the time to stress test it yet.
My prime goal was adding as many features as possible, hence I could not allot enough time to dockerize the project.

## Features
 - User registration including password security
 - Oauth2 session authentication for a trusted messaging experience
 - Real time messaging
 - Can text multiple people and have multiple chats(sky is the limit!)

## Future scope
 - More focus on privacy(end-to-end encryption)
 - Dockerize the project for better setup experience
 - Server-sent events for better real-time experience(currently the client will poll the server repeatedly for new messages)

## How to use
There is no need to set up the backend on your end to test out the code as I have already set it up on my end, you only need to run client.py on python3 and get started!