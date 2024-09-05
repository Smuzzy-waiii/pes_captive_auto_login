# PES Captive Auto-Login
An application to keep your in-campus servers always logged in to the captive portal :D
# Installation

1. Download the `docker-compose.yaml` file:
   ```shell
   wget https://raw.githubusercontent.com/Smuzzy-waiii/pes_captive_auto_login/main/docker-compose.yaml
   ```
2. Replace the PES captive portal username and password in the `docker-compose.yaml` file.
   ```yaml
   ...
       environment:
      - CAPTIVE_USERNAME=<username> #replace your captive username here
      - CAPTIVE_PASSWORD=<password> #replace your captive password here
   ...
   ```
   **Make sure you use valid username and password, check manually once from the same machine before using**
3. Run the tool using docker compose
   ```
   $ sudo docker compose up -d
   [+] Building 0.0s (0/0)                                                                                                 
   [+] Running 3/3
    ✔ Network pes-captive_default              Created                                                                                     0.8s 
    ✔ Container pes-captive-auto-login-1       Started                                                                                     5.7s 
    ✔ Container pes-captive-selenium-chrome-1  Started                                                                                     6.7s 
   ```
   _Note: your exact container names may differ_
4. Make sure the auto-login and selenium-chrome containers are running
   ```
   $ sudo docker ps
   CONTAINER ID   IMAGE                                   COMMAND                  CREATED         STATUS         PORTS                                                 NAMES
   4be5e6ca7e87   selenium/standalone-chrome              "/opt/bin/entry_poin…"   2 minutes ago   Up 2 minutes   0.0.0.0:4444->4444/tcp, :::4444->4444/tcp, 5900/tcp   pes-captive-selenium-chrome-1
   527f256badd3   smaranjawalkar/pes-captive-auto-login   "python -u main.py"      2 minutes ago   Up 2 minutes                                                         pes-captive-auto-login-1
   ```
5. Test that the auto-login is working
   ```
   $ sudo docker exec pes-captive-auto-login-1 python3 captive.py
   Using username: internship13 and password: internship13 @ http://selenium-chrome:4444
   Opening Chrome
   Opened Remote
   Opened connection
   Successfully logged in to captive 
   ```
   Replace `pes-captive-auto-login-1` with you exact container name (as seen in Step 3 and Step 4)
   
