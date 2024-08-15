## User table
uuid - Primary key
username - TEXT
password_hash - TEXT

### Query - 
CREATE TABLE IF NOT EXISTS public."user"
(
    uuid uuid NOT NULL,
    username text COLLATE pg_catalog."default" NOT NULL,
    password_hash text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT user_pkey PRIMARY KEY (uuid)
);

ALTER TABLE IF EXISTS public."user"
    OWNER to sosboy888;

### Messages table
uuid - Primary Key
user_id - TEXT
to_id - TEXT
text - TEXT

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