alter table "user" alter column timestamp type int using (extract(epoch from timestamp::date));
alter table "chat" alter column timestamp type int using (extract(epoch from timestamp::date));
alter table "prompt" alter column timestamp type int using (extract(epoch from timestamp::date));
alter table "chatidtag" alter column timestamp type int using (extract(epoch from timestamp::date));
alter table "document" alter column timestamp type int using (extract(epoch from timestamp::date));
alter table "modelfile" alter column timestamp type int using (extract(epoch from timestamp::date));
ALTER TABLE public."user" ALTER COLUMN profile_image_url TYPE text USING profile_image_url::text;

ALTER TABLE public."auth" ALTER COLUMN active TYPE boolean USING active::int;
