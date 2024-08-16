import requests
import json
import uuid
import time
import getpass
import threading

BASE_URL = "https://sosboy888.ngrok.pro"
"""
For local server comment the line above and uncomment the line below
"""
#BASE_URL = "http://127.0.0.1:8000"
username = ""
messages_set = set([])
def register_user():
    global username
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    data = {"username": username, "password_hash": password}
    response = requests.post(f"{BASE_URL}/users/", json=data)
    if response.status_code == 200:
        print("User created successfully")
    else:
        print("User creation failed")

def receive_messages_thread(token, to_username):
    while True:
        receive_messages(token, to_username)
        time.sleep(2)

def login_user():
    global username
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    data = {'username': username, 'password': password}
    response = requests.post(f"{BASE_URL}/token", data=data)
    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        print("Login failed")
        return None


def send_message(token, to_username, message):
    global username
    headers = {"Authorization": f"Bearer {token}"}
    data = {"user_id":username,"to_id": to_username, "text": message}
    response = requests.post(f"{BASE_URL}/messages", headers=headers, json=data)
    

def receive_messages(token, to_username):
    global username
    headers = {"Authorization": f"Bearer {token}"}
    data = {'from_id':username, 'to':to_username}
    response = requests.post(f"{BASE_URL}/messages/fetch/", headers=headers, json=data)
    if response.status_code == 200:
        messages = response.json()["messages"]
        #print(messages)
        for message in messages:
            if message['uuid'] not in messages_set:
                print(f"{message['user_id']}: {message['text']}")
            messages_set.add(message['uuid'])
    else:
        print("Error fetching messages")

def main():
    global username
    while True:
        choice = input("1. Register\n2. Login\nq. Quit\n")
        if choice == "1":
            register_user()
        elif choice == "2":
            token = login_user()
            if token:
                to_username = input("Enter recipient username: ")
                receive_thread = threading.Thread(target=receive_messages_thread, args=(token, to_username), daemon=True)
                receive_thread.start()
                while True:
                    message = input()
                    send_message(token, to_username, message)
                    receive_messages(token, to_username)  
                    time.sleep(2) 
        elif choice == "q":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()