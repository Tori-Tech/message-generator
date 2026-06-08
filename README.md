## AI Message Generator: Transforming blunt messages into professional, workplace-ready communication.

### Features:

Corporate Translation Engine: Instantly transforms blunt, casual, or informal drafts into polished messages ready for deployment. 

Powered by Llama 3: Leverages the advanced Meta-Llama-3-8B-Instruct model via Hugging Face for high-quality text generation.

Secure API Integration: Designed with security in mind, utilizing Hugging Face Access Tokens and Streamlit's secrets.toml file to ensure safe and authenticated model requests.

A Balance of Utility & Fun: While perfect for adding a bit of humor to your daily workflow, it also serves as a legitimate tool for navigating tricky workplace communications.

### Prerequisites:

In order to use the app, you need to have a HuggingFace access token. To obtain one:
1. Create a HuggingFace account [here](https://huggingface.co/)
2. Navigate to Settings > Access Tokens and generate an access token with **read** permissions only. Anything else is unnecessary. 

### Installation Guide:

-Clone the repository.
-```cd``` into the project folder.
-Install required dependencies by running: ```pip install -r requirements.txt```
Create a folder named `.streamlit` in the root directory (if it doesn't already exist).
- Inside that folder, create a file called `secrets.toml` and add the following content:
```toml
HF_TOKEN="your_huggingface_access_token_here"
APP_PASSWORD="your_chosen_password_here"
```
-Open a terminal in the root folder and run the app with: ```streamlit run app.py```
-Enter in the password and follow the prompts to generate your first message!
-Note: The ```config.toml``` contains color palette information. If you dislike the current colors, feel free to change them (or just revert to default dark/light mode) to your liking.

### Why is there a password?

Although Hugging Face's free-tier rate limits do not incur financial charges, heavy traffic can easily exhaust the limit and render the app unusable.

Because this repository serves as the source code for a publicly deployed Streamlit app, a password layer was implemented to prevent unauthorized users or bots from exhausting the API limits. If you plan to host this app strictly locally, you can safely remove the password verification logic from app.py


