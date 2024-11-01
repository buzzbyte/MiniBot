# MiniBot

Simple dockerized bot with only a `/ping` command for now. Written in Python using PyCord library.

To run:
1.  Clone the repo and cd to it
    ```bash
    git clone https://github.com/buzzbyte/MiniBot.git
    cd ./MiniBot
    ```
2.  Create a file called `secrets.env` with the following content
    ```env
    DISCORD_BOT_TOKEN=YOUR_DISCORD_TOKEN
    ```
    Replace `YOUR_DISCORD_TOKEN` with your actual bot token

3. Build and run with Docker compose:
    ```bash
    docker compose up
    ```
    Add `-d` to run in the background

4. ???
5. Profit.