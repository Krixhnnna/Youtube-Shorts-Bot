# YouTube Shorts Bot

An automated tool that converts Reddit videos into engaging YouTube Shorts. This bot downloads trending videos from specified subreddits, processes them into the vertical format required for YouTube Shorts, and automatically uploads them to your YouTube channel.

## Features

- 🔄 Automatic video downloading from specified subreddits
- 📱 Conversion to YouTube Shorts format (9:16 aspect ratio)
- 🎥 Smart video processing with blur effects and transitions
- 📤 Direct upload to YouTube
- 🔍 Duplicate video detection to avoid reposts
- 📊 Support for multiple subreddits
- 🎯 Customizable video dimensions and effects

## Prerequisites

- Python 3.10 or higher
- Reddit API credentials
- YouTube API credentials
- FFmpeg installed on your system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Krixhnnna/Youtube-Shorts-Bot.git
cd Youtube-Shorts-Bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

### Reddit API Setup
1. Go to https://www.reddit.com/prefs/apps
2. Create a new application
3. Select "script" as the application type
4. Set the redirect URI to http://localhost:8080
5. Note down your client ID and client secret

### YouTube API Setup
1. Go to Google Cloud Console
2. Create a new project
3. Enable YouTube Data API v3
4. Create OAuth 2.0 credentials
5. Download the client_secrets.json file

### Update Configuration
1. Copy `client_secrets.json` to the project root
2. Update `config.py` with your credentials:
```python
reddit_login = {
    'client_id': 'YOUR_REDDIT_CLIENT_ID',
    'client_secret': 'YOUR_REDDIT_CLIENT_SECRET',
    'password': 'YOUR_REDDIT_PASSWORD',
    'user_agent': 'YOUR_USER_AGENT',
    'username': 'YOUR_REDDIT_USERNAME'
}
```

## Usage

1. Activate the virtual environment:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the main script:
```bash
python main.py
```

The script will:
- Download trending videos from specified subreddits
- Process them into YouTube Shorts format
- Upload them to your YouTube channel

## Configuration Options

### Reddit Settings
- Subreddits to monitor
- Post sorting method (hot, new, top)
- Minimum upvote threshold

### YouTube Settings
- Video title format
- Description template
- Tags and category
- Privacy settings

### Video Settings
- Output dimensions (default: 1080x1920)
- Blur effect intensity
- Transition effects

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Reddit API for video content
- YouTube Data API for video uploads
- MoviePy for video processing
- PRAW for Reddit interaction

<img width="750" alt="portfolio_view" src="https://construyenpais.com/wp-content/uploads/YouTube-y-Reddit-las-redes-que-mas-crecieron-en-EE.UU-durante-la-pandemia.png">

# Automatic YouTube Shorts Generator and Uploader

### Background
I had the initial idea that content between platform is very transformative. A lot of Youtube's content could be transformed into TikTok content, Instagram to Facebook, Reddit to YouTube, etc. I decided to start with a slice of this idea. Reddit to Youtube. I chose to make the videos in Youtube shorts format since it's a new field, less established, more likely to gain following.

At the same time, I wanted to work with automated video editing and learning to manage code in a more pythonic way.

---

### Installation
#### Conda:
Conda the easiest way to install the dependencies for this project. If you don't have conda already, follow this tutorial for [Linux/Mac](https://www.youtube.com/watch?v=OH0E7FIHyQo), or this one for [Windows](https://www.youtube.com/watch?v=XCvgyvBFjyM).

If you're unfamiliar, conda allows us manage package dependencies needed in a contained format, thus won't clash with other projects' dependencies.

After you've install conda, create the conda environment needed for this project via:
```
conda env create -f conda_env.yml
```

From there, if successfully installed, you'll be able to access the environment via:
```
conda activate shorts-gen
```

#### Manual pip install:
Alternatively, you can manually download FFmpeg and pip install all the packages needed in your desired virtual environment manager. To install FFmpeg, see [this](https://www.google.com/search?q=how+to+install+ffmpeg+on+mac+%2F+windows+10+%2F+linux). Here are the manual pip installs:
```
pip install -r requirements.txt
```

---

### Set up
1. Edit `config.py` to your desired settings. You'll input your Reddit API information here. Follow this [tutorial](https://youtu.be/NRgfgtzIhBQ?t=50) on how to set up the Reddit's API.

2. Next you'll need to set up the YouTube side of things. Follow [this tutorial](https://youtu.be/aFwZgth790Q) on how to set up YouTube Data 4 API to obtain your unique `client_secrets.json` file. Place this file in the same directory as to `main.py`.

>Note: To get the ability to make your videos public, your program has to go through an audit process. Check out this: https://support.google.com/youtube/contact/yt_api_form 

---

### How to run
You should now be all set to run the script! Simply type `python main.py` into your terminal. It should download a relevant video, edit it, and upload it all in one step.

If you're super new to coding/python, and don't know how to run a script by `python main.py`, then right-clicking on `main.py` file and running it using `open with` and python's launcher should do the trick.

---

### Issues / contributions and pull requests
If you're having any issues: feel free to create an issue request, and/or join this project's discord server.
If you'd like to contribute, feel free to start a pull request! (and maybe join the server so it's easier to communicate :) )

<kbd> <br> Join our [Discord](https://discord.gg/tyxuTJtUKJ) for this project! <br> </kbd>

---

### Updates
2023-06-22:
Added ability to install dependencies  via a conda `.yml` file.
Added ability to uploaded videos as is from Reddit, without rendering.

2023-04-15:
Google's authentication has changed, and now it's much harder to authenticate through the terminal. I recommend using a computer with a user interface to authenticate and run the program! So, imo, don't bother with EC2, and just use an old/spare laptop if you have one.

I wrote this project early in my programming career, and thought I'd come back to it to re-write most of the code to make it much more readable and dynamic. Hope this helps with the issues!

---

### Star History
[![Star History Chart](https://api.star-history.com/svg?repos=zackmawaldi/YouTube-shorts-generator&type=Date)](https://star-history.com/#zackmawaldi/YouTube-shorts-generator&Date)
-
Rights: "Automatic YouTube Shorts Generator and Uploader" is released under an open source MIT License (see LICENSE file). It is free for non-profit, for-profit, and personal use.
