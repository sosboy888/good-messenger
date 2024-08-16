## How to setup the server

Note: If you are only looking to try the messaging functionality, you do not need to set up this server on your system. Simply run client.py using python3 and get started!
Follow this guide if you are willing to set the server up on your system!

### Requirements
- Python3
- Postgres 16 with pgAdmin


Create a .env file in the server directory with the correct postgres config and a jwt secret key for OAuth2. 
Use this example:
```
database=goodmessenger
host=localhost
user=postgres
password=root
port=5432
jwt_secret_key=samplekey123456
```
Execute these queries in your Postgres database using pgAdmin(NOTE: ensure that the database you execute these queries in is the same database you have added in the .env file)

```
CREATE TABLE IF NOT EXISTS public."user"
(
    uuid uuid NOT NULL,
    username text COLLATE pg_catalog."default" NOT NULL,
    password_hash text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (uuid)
);

ALTER TABLE IF EXISTS public."user"
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.messages
(
    uuid uuid NOT NULL,
    user_id text COLLATE pg_catalog."default" NOT NULL,
    to_id text COLLATE pg_catalog."default" NOT NULL,
    text text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT message_pkey PRIMARY KEY (uuid)
);

ALTER TABLE IF EXISTS public.messages
    OWNER to sosboy888;


CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

Finally, we need to install the required Python libraries using this command:
```
$pip3 install -r requirements/requirements.txt
```

Once all of these steps are completed, you can execute this command in the server directory to run the server!

```
uvicorn main:app --reload
```

Currently client.py is configured to hit my ngrok hosted version of the messaging server, if you want to use the client with your own local server, ensure 