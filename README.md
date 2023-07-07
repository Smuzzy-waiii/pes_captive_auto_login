# Installation

1. You will first need to pull and run the selenium standalone-chrome docker container.

   ```shell
   docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
   ```
2. Check if the Selenium Grid UI is running at http://localhost:4444

3. Run the pes-captive-auto-login container

   ```shell
   docker run -d -e CAPTIVE_USERNAME=<username> -e CAPTIVE_PASSWORD=<password> -e SELENIUM_URL=http://localhost:4444 --name pes-captive --network=host smaranjawalkar/pes-captive-auto-login
   ```

   The **--host=network** part is very important. Without this, the captive container wont be able to talk to the selenium container. 

   _Remember to key in your username and password_

   
