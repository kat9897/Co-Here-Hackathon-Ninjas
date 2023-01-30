# Co-Here-Hackathon

## Starting off
1. Clone Github Repo: `git clone https://github.com/Adibvafa/Co-Here-Hackathon.git`
2. Run `pip install cohere umap-learn altair annoy datasets tqdm python-dotenv numpy` to install necessary dependencies
3. Download train.jsonl.gz from [Emotions|https://huggingface.co/datasets/emotion/tree/main/data]

## Working with Python virtual env.
1. Create a folder to create your virtual environment in
2. Run `python -m venv venv`
3. Run `venv\Scripts\activate`. Note: You should see terminal line change to (venv)
4. Create `app.py` file inside venv folder and add default text from Flask tutorial
5. Go into venv folder and run `flask --app app run`
Note: Make sure you have all the dependencies installed. Sometimes you need to install them separately

**Update!!** If you want to install all the dependencies I was using, run `pip install -r requirements.txt`

## Run normally
1. cd into `venv` folder
2. Run `Scripts\activate`
3. Run `flask --app app run`
4. Open localhost link using Ctrl + click