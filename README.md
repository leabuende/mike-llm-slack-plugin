<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Mike - Your Project Management Assistant</h3>

  <p align="center">
    An awesome LLM plugin for Slack
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This project has been built in the context of Pathway's LLM Bootcamp. Big kudo's to them for their amazing course !
Here are all the tools I used :

* [Slack API](https://api.slack.com/)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* [Ngrok](https://ngrok.com/)
* [Pathway's LLM App](https://pathway.com/developers/showcases/llm-app-pathway)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

In order to get the project up and running, you need to have a Trello Board, a Slack channel and an OpenAI API key.
Follow the steps to :
- Get an [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)
- Get the [Trello board ID](https://community.atlassian.com/t5/Trello-questions/How-to-get-Trello-Board-ID/qaq-p/1347525), and the [Trello token and key](https://trello.com/app-key)

### Installation

#### Start LLMAppService
1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Copy and fill the .env file with the keys that you recovered

3. Install packages
   ```sh
   pip install requirements.txt
   ```
4. Start the service
   ```sh
   python3 main.py
   ```
#### Start SlackBotService
1. Copy and fill the .env file with the keys that you recovered (set API_URL as the URL of LLMAppService)

3. Install packages
   ```sh
   pip install requirements.txt
   ```
4. Start the service
   ```sh
   python3 main.py
   ```
#### Start Ngrok 
1. Start tunnel to connect to Slack
   ```sh
   ngrok http 3000
   ```

Then, follow the steps in this article starting at [3. Create a new Slack app](https://medium.com/developer-student-clubs-tiet/how-to-build-your-first-slack-bot-in-2020-with-python-flask-using-the-slack-events-api-4b20ae7b4f86) using your ngrok address to plug your app into your Slack channel.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project can be used for you to monitor your Trello board for your team, help them asses their progress and find new tasks to work on that fit with their role/set of skills.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add cronjob to fetch trello cards regularly
- [x] Add open QA for users
- [ ] Fix Dockerfiles
- [ ] Notify Slakc channel when a new Sprint has been completed
- [ ] Generate performance report as pdf file
- [ ] Add a document repository to add complementary info on project roadmap and technical specifications

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Léa Buendé - [@your_twitter](https://twitter.com/your_username) - hello@lea-buende.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



