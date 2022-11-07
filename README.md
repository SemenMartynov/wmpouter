# Where is my router?

For some reason, my router was taken to Armenia. It is definitely working there, as I receive notifications from the Telegram bot.

I don't know its external IP address, so I decided to go through the whole known range (scan Armenia IP addresses), hoping to discover it.

No luck.

## Deploy without root

If you don't have a root access, it needs to create a virtual environment for installing dependencies.
```sh
$ python3 -m venv .wmrouter
$ source .wmrouter/bin/activate
(.wmrouter) $ python3 -m pip install --upgrade pip
(.wmrouter) $ python3 -m pip install paramiko
```

Now you can launch the application and demonize it.
After that, we can leave the virtual environment.
```sh
(.wmrouter) $ nohup python3 main.py &
(.wmrouter) $ exit
$
```

Debugging information can be found in the file `nohup.out`.
