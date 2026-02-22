# TUC Discord Bot
Built using Pycord

## Features
- Automatically posts a weekly completion log thread to a forum channel

---

## Setup

### Prerequisites
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) installed
- Discord server that you are an admin of.

### 1. Create a Discord Application & Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application** in the top right and give it a name
3. In the left sidebar, click **Bot**
4. Click **Add Bot** and confirm
5. Under the bot's username, click **Reset Token** and copy the token that appears — you will not be able to see it again after closing the page
6. Create a `.env` file in the root of the repo and paste your token:
   ```
   TOKEN=your_token_here
   ```
   > **Never share your token or commit it to git.** Anyone with it can control your bot. Make sure you add `.env` to `.gitignore`. If you cloned this repo, it's already done for you.

### 2. Enable Required Intents

Still on the **Bot** page in the Developer Portal:

1. Scroll down to **Privileged Gateway Intents**
2. Enable **Server Members Intent** and **Message Content Intent**
3. Click **Save Changes**

### 3. Invite the Bot to Your Server

1. In the left sidebar, click **OAuth2 → URL Generator**
2. Under **Scopes**, check `bot` and `applications.commands`
3. Under **Bot Permissions**, check the following:
   - `Read Messages / View Channels`
   - `Send Messages`
   - `Create Public Threads`
   - `Send Messages in Threads`
   - `Manage Threads`
4. Copy the generated URL at the bottom of the page
5. Paste it in your browser, select your server from the dropdown, and verify the permissions are set correctly for your bot. Then click **Authorize** 

### 4. Get Your Forum Channel ID

1. Open Discord and go to your server
2. Go to **User Settings → Advanced** and enable **Developer Mode**
3. Right-click your **forum channel** in the sidebar (not a post inside it) and click **Copy Channel ID**
4. Paste it into `bot.py` as `COMPLETION_LOG_CHANNEL_ID`

### 5. Install Dependencies & Run

```
uv sync
uv run bot.py
```
