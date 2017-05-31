CREATE DATABASE "Election"
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'de_DE.UTF-8'
       LC_CTYPE = 'de_DE.UTF-8'
       CONNECTION LIMIT = -1;


﻿-- Table: public."User-Tweet"

-- DROP TABLE public."User-Tweet";

CREATE TABLE public."User-Tweet"
(
  "handle" name NOT NULL,
  "time" timestamp without time zone NOT NULL,
  original_author name,
  retweet_count integer NOT NULL,
  "text" text NOT NULL,
  favourite_count integer NOT NULL,
  "index" integer[] NOT NULL,
  CONSTRAINT "IndexPK" PRIMARY KEY ("Index")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."User-Tweet"
  OWNER TO postgres;

  CREATE TABLE public."Hashtag"
(
  "Hash_Name" name NOT NULL,
  "Tweet_indices" integer[] NOT NULL,
  "Hash_count" integer NOT NULL,
  CONSTRAINT "HashK" PRIMARY KEY ("Hash_Name"),
  CONSTRAINT "TweetFK" FOREIGN KEY ("Tweet_indices")
      REFERENCES public."User-Tweet" ("Index") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Hashtag"
  OWNER TO postgres;

