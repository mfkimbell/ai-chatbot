
# ai-chatbot

## Tools Used

* `LangChain` - Library for building language model chains and managing conversation memory.
* `ChatBedrock` - LangChain module for integrating with AWS Bedrock for LLM interactions.
* `Streamlit` - Framework for building interactive web applications (particularly in data science)
* `Docker` - Containerization platform used for running the application locally.

## Setup and Usage

### Opening VSCode

You need to open VSCode through Anaconda or Streamlit will not function properly.

### AI Prompting Parameters

In the context of AI prompting, the following parameters are important:

* **p (Probability)** - This parameter controls the probability of the next token being generated. In some AI models, it is used to ensure that the generated text aligns with a certain probability distribution, making the output more predictable.

* **k (Top-K Sampling)** - This parameter limits the number of possible next tokens to the top `k` most probable ones. For example, if `k` is set to 50, the model will consider only the top 50 tokens for generating the next word. This helps in producing more coherent and contextually relevant responses.

* **Temperature** - The temperature parameter controls the randomness of the output. A lower temperature (e.g., 0.1) makes the output more deterministic and less diverse, while a higher temperature (e.g., 1.0) increases the randomness, allowing for more diverse and creative responses. Adjusting the temperature helps in balancing between creativity and coherence in the AI’s responses.

### Local Testing

To test the application locally, follow these steps:

1. **Clone the repo**
```bash
git clone https://github.com/mfkimbell/ai-chatbot.git
```

2. **Pull the Docker Image:**

    ```bash
    docker pull mfkimbell/ai-chatbot:newversion
    ```

2. **Run the Docker Container:**

    ```bash
    docker run --env-file .env -p 8501:8501 mfkimbell/ai-chatbot:newversion
    ```

    Ensure that you have a `.env` file with the necessary environment variables.

`AWS_ACCESS_KEY_ID`
`AWS_SECRET_ACCESS_KEY`
`AWS_DEFAULT_REGION`

3. **Access Webapp**

   ```http://0.0.0.0:8501/```
   or
   ```http://localhost:8501/```


