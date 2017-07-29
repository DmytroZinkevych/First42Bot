# First42Bot
*My first Telegram bot*<br/><br/>
https://t.me/First42Bot<br/>

First42Bot gives a pseudo-random generated result of flipping a coin, throwing 2 dice and choosing a number from specified interval. Also bot has a function of finding an average value of entered numbers.

<img src="https://user-images.githubusercontent.com/24415165/28586892-e6cf6a52-717d-11e7-895a-11340b57162c.PNG" alt="Screenshot" height="500px">

Bot is written on **Python 3** and requires **pyTelegramBotAPI** (https://github.com/eternnoir/pyTelegramBotAPI).

### Important note

Currently bot prints to console name of the used command, date, time and chat ID. It's done for the purpose to see how many users, how frequently and which commands use. It's impossible to identify person by chat ID, only distinguish from other users. This data isn't permanently stored in memory, isn't visible to anybody except of bot's owner and completely disappears after restarting of bot (it happens regularly). Any other data isn't printed to console and/or collected by bot and it's owner. But anyway for security reasons don't send to bot any private information.
