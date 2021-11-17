CREATE ROLE django_role WITH CREATEDB LOGIN PASSWORD 'django_pass';
CREATE DATABASE django_dev WITH TEMPLATE = template0 OWNER = 'django_role' ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C';
