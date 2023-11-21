Add a README to your GitHub (or update it if you already have one) that
contains your communication contract. (Once you define it, don't change it!
Your partner is relying on you.) README must contain...

## How to request data:

Once you have a user ID, you can call this script with a user id as the first parameter.

    $ python parseCal.py user_kxZN5GQfp8YaixypXoAe8MYU44NVaDJ7XV8b5dCA

## How to recieve data

After it has correctly parsed a .ics file, `parseCal.py` writes to
`<user_id>.csv` in the form

    COURSE INFO,1970-01-01
    COURSE INFO,1970-01-01
    COURSE INFO,1970-01-01

If it fails, the script will exit with code 1.
