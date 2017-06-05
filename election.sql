-- Table: public.usertweet

-- DROP TABLE public.usertweet;

CREATE TABLE public.usertweet
(
  index text NOT NULL,
  handle name NOT NULL,
  text text NOT NULL,
  original_author name,
  "time" timestamp with time zone NOT NULL,
  retweet_count integer NOT NULL,
  favorite_count integer NOT NULL,
  CONSTRAINT "indPK" PRIMARY KEY (index)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.usertweet
  OWNER TO postgres;
GRANT ALL ON TABLE public.usertweet TO public;
GRANT ALL ON TABLE public.usertweet TO postgres;

-- Table: public.hashtag

-- DROP TABLE public.hashtag;

CREATE TABLE public.hashtag
(
  hashtag text NOT NULL,
  tweet_indices text NOT NULL,
  CONSTRAINT "hashPK" PRIMARY KEY (hashtag)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.hashtag
  OWNER TO postgres;
GRANT ALL ON TABLE public.hashtag TO public;
GRANT ALL ON TABLE public.hashtag TO postgres;


