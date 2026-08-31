# AI models

A simple python project that sends user prompt to the Nova AI API and returns a response from Qwen 3.8-Max model.

## Reqirements

- Python 3.12+
- uv
- A Nova API key 

## setup

1. Clone the repository:

```bash
git clone git@github.com:bitmax585/Ai_models.git
cd Ai_models
```

2. install the dependencies:

```bash
uv sync
```
3. Create a `.env` file in the root directory of the project.

4. Add your Nova AI API key to the `.env` file.

NOVAI_API_KEY=your_api_key


### Do not share your API key or commit the `.env` file to GitHub.

## Run 

Run the application with:

```bash
uv run python src/ai_models/main.py
```
