CREATE DATABASE "Election"
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'de_DE.UTF-8'
       LC_CTYPE = 'de_DE.UTF-8'
       CONNECTION LIMIT = -1;


﻿-- Table: public."usertweet"

-- DROP TABLE public."usertweet";

CREATE TABLE public."usertweet"
(
  "handle" name NOT NULL,
  "time" timestamp with time zone NOT NULL,
  original_author name,
  retweet_count integer NOT NULL,
  "text" text NOT NULL,
  favourite_count integer NOT NULL,
  "index" integer[] NOT NULL,
  CONSTRAINT "PK" PRIMARY KEY ("Index")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."usertweet"
  OWNER TO postgres;

  CREATE TABLE public."hashtag"
(
  "Hash_Name" name NOT NULL,
  "Tweet_indices" integer[] NOT NULL,
  "Hash_count" integer NOT NULL,
  CONSTRAINT "hashPK" PRIMARY KEY ("hashname"),
  CONSTRAINT "FK" FOREIGN KEY ("tweetindices")
      REFERENCES public."usertweet" ("Index") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."hashtag"
  OWNER TO postgres;

