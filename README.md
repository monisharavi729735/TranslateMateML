# TranslateMate

TranslateMate is a language translation application that leverages machine learning models to provide accurate translations between English and multiple languages. The Python app is built using [Anvil](https://anvil.works) for the frontend and [Google Colab](https://colab.research.google.com/) for the backend.

## Features

- **Language Translation:** Translate text from English to French, German, Spanish, Italian, Russian, and Dutch.
- **Transliteration:** Convert Russian text to its phonetic equivalent in Latin script.
- **Text-to-Speech:** Convert translated text to speech with a single button click.

## Getting Started

### Prerequisites

- An Anvil account
- A Google Colab account
- Python environment with the following libraries installed:
  - `virtualenv`
  - `anvil-uplink`
  - `transformers`
  - `torch`
  - `torchvision`
  - `torchaudio`
  - `sacremoses`
  - `transliterate`

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/monisharavi729735/TranslateMateML.git
   cd TranslateMateML

2. **Set Up Google Colab**
- Open the .ipynb file in Google Colab.
- Install the required packages by running the setup cells.
- Connect to the Anvil Uplink by replacing the placeholder with your Anvil Uplink key.

  ```python
  import anvil.server
  anvil.server.connect("your-anvil-uplink-key")

3. Run the Application

- Run all cells in the Google Colab notebook to start the server.

## Using the Application
- Open the Anvil app in your browser.
- Enter the text you want to translate and select the target language.
- Click the "Translate" button to get the translated text.
- For Russian, the transliterated text will also be provided.
- Click the "Text-to-Speech" button to hear the translation spoken aloud.

## Project Structure
- `TranslateMateML.ipynb`: Main Google Colab notebook containing the backend code.
- `anvil_app`: Folder containing the Anvil app files.

## Models Used
- `English to French`: [Helsinki-NLP/opus-mt-en-fr](Helsinki-NLP/opus-mt-en-fr)
- `English to German`: [Helsinki-NLP/opus-mt-en-de](Helsinki-NLP/opus-mt-en-de)
- `English to Spanish`: [Helsinki-NLP/opus-mt-tc-big-en-es](Helsinki-NLP/opus-mt-tc-big-en-es)
- `English to Italian`: [Helsinki-NLP/opus-mt-en-it](Helsinki-NLP/opus-mt-en-it)
- `English to Russian`: [Helsinki-NLP/opus-mt-en-ru](Helsinki-NLP/opus-mt-en-ru)
- `English to Dutch`: [Helsinki-NLP/opus-mt-en-nl](Helsinki-NLP/opus-mt-en-nl)

## BLEU Score Evaluation
The BLEU (Bilingual Evaluation Understudy) score is used to evaluate the quality of the translations. The scores for each language pair are calculated in the notebook using sample sentences and human-generated reference translations.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your suggestions and improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- The Helsinki-NLP team for the translation models.
- The Anvil team for the web app platform.
- The Hugging Face team for the Transformers library.

<br />

# About This [Anvil](https://anvil.works/?utm_source=github:app_README) App

### Build web apps with nothing but Python.

The app in this repository is built with [Anvil](https://anvil.works?utm_source=github:app_README), the framework for building web apps with nothing but Python. You can clone this app into your own Anvil account to use and modify.

Below, you will find:
- [How to open this app](#opening-this-app-in-anvil-and-getting-it-online) in Anvil and deploy it online
- Information [about Anvil](#about-anvil)
- And links to some handy [documentation and tutorials](#tutorials-and-documentation)

## Opening this app in Anvil and getting it online

### Cloning the app

Go to the [Anvil Editor](https://anvil.works/build?utm_source=github:app_README) (you might need to sign up for a free account) and click on “Clone from GitHub” (underneath the “Blank App” option):

<img src="https://anvil.works/docs/version-control-new-ide/img/git/clone-from-github.png" alt="Clone from GitHub"/>

Enter the URL of this GitHub repository. If you're not yet logged in, choose "GitHub credentials" as the authentication method and click "Connect to GitHub".

<img src="https://anvil.works/docs/version-control-new-ide/img/git/clone-app-from-git.png" alt="Clone App from Git modal"/>

Finally, click "Clone App".

This app will then be in your Anvil account, ready for you to run it or start editing it! **Any changes you make will be automatically pushed back to this repository, if you have permission!** You might want to [make a new branch](https://anvil.works/docs/version-control-new-ide?utm_source=github:app_README).

### Running the app yourself:

Find the **Run** button at the top-right of the Anvil editor:

<img src="https://anvil.works/docs/img/run-button-new-ide.png"/>


### Publishing the app on your own URL

Now you've cloned the app, you can [deploy it on the internet with two clicks](https://anvil.works/docs/deployment/quickstart?utm_source=github:app_README)! Find the **Publish** button at the top-right of the editor:

<img src="https://anvil.works/docs/deployment-new-ide/img/environments/publish-button.png"/>

When you click it, you will see the Publish dialog:

<img src="https://anvil.works/docs/deployment-new-ide/img/quickstart/empty-environments-dialog.png"/>

Click **Publish This App**, and you will see that your app has been deployed at a new, public URL:

<img src="https://anvil.works/docs/deployment-new-ide/img/quickstart/default-public-environment.png"/>

That's it - **your app is now online**. Click the link and try it!

## About Anvil

If you’re new to Anvil, welcome! Anvil is a platform for building full-stack web apps with nothing but Python. No need to wrestle with JS, HTML, CSS, Python, SQL and all their frameworks – just build it all in Python.

<figure>
<figcaption><h3>Learn About Anvil In 80 Seconds👇</h3></figcaption>
<a href="https://www.youtube.com/watch?v=3V-3g1mQ5GY" target="_blank">
<img
  src="https://anvil-website-static.s3.eu-west-2.amazonaws.com/anvil-in-80-seconds-YouTube.png"
  alt="Anvil In 80 Seconds"
/>
</a>
</figure>
<br><br>

[![Try Anvil Free](https://anvil-website-static.s3.eu-west-2.amazonaws.com/mark-complete.png)](https://anvil.works?utm_source=github:app_README)

To learn more about Anvil, visit [https://anvil.works](https://anvil.works?utm_source=github:app_README).

## Tutorials and documentation

### Tutorials

If you are just starting out with Anvil, why not **[try the 10-minute Feedback Form tutorial](https://anvil.works/learn/tutorials/feedback-form?utm_source=github:app_README)**? It features step-by-step tutorials that will introduce you to the most important parts of Anvil.

Anvil has tutorials on:
- [Building Dashboards](https://anvil.works/learn/tutorials/data-science#dashboarding?utm_source=github:app_README)
- [Multi-User Applications](https://anvil.works/learn/tutorials/multi-user-apps?utm_source=github:app_README)
- [Building Web Apps with an External Database](https://anvil.works/learn/tutorials/external-database?utm_source=github:app_README)
- [Deploying Machine Learning Models](https://anvil.works/learn/tutorials/deploy-machine-learning-model?utm_source=github:app_README)
- [Taking Payments with Stripe](https://anvil.works/learn/tutorials/stripe?utm_source=github:app_README)
- And [much more....](https://anvil.works/learn/tutorials?utm_source=github:app_README)

### Reference Documentation

The Anvil reference documentation provides comprehensive information on how to use Anvil to build web applications. You can find the documentation [here](https://anvil.works/docs/overview?utm_source=github:app_README).

If you want to get to the basics as quickly as possible, each section of this documentation features a [Quick-Start Guide](https://anvil.works/docs/overview/quickstarts?utm_source=github:app_README).
