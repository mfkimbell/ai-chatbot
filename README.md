
# ai-chatbot

## Architecture

<img src="https://github.com/user-attachments/assets/39e486dd-45d0-4140-a7b3-407c903bd235" alt="Chatbot Architecture" width="800">



## Tools Used

* `LangChain` - Library for building language model chains and managing conversation memory.
* `ChatBedrock` - LangChain module for integrating with AWS Bedrock for LLM interactions.
* `Streamlit` - Framework for building interactive web applications (particularly in data science)
* `Docker` - Containerization platform used for running the application locally.
* `Claude-3-haiku` - Large language model used

## Prompt Demo

![2-ezgif com-speed](https://github.com/user-attachments/assets/1238726b-141d-422b-8416-9bf1e5ecc360)

## Memory Demo

![Memoryexample-ezgif com-speed](https://github.com/user-attachments/assets/cb43815c-72d9-458d-91e0-bfd2bc088b4e)


### AI Prompting Parameters

In the context of AI prompting, the following parameters are important:

* **p (Probability)** - This parameter controls the probability of the next token being generated. In some AI models, it is used to ensure that the generated text aligns with a certain probability distribution, making the output more predictable.

* **k (Top-K Sampling)** - This parameter limits the number of possible next tokens to the top `k` most probable ones. For example, if `k` is set to 50, the model will consider only the top 50 tokens for generating the next word. This helps in producing more coherent and contextually relevant responses.

* **Temperature** - The temperature parameter controls the randomness of the output. A lower temperature (e.g., 0.1) makes the output more deterministic and less diverse, while a higher temperature (e.g., 1.0) increases the randomness, allowing for more diverse and creative responses. Adjusting the temperature helps in balancing between creativity and coherence in the AI’s responses.

* **Stop Sequence** - In chatbots and AI text generation, a stop sequence or stop word marks a point in the conversation where the AI pauses and awaits user input, ensuring interactive and user-driven dialogue flow. In this case, our stop sequence is `["\n\nHuman:"]` since we want the user to fill in that part of the conversation.

### Local Testing

To test the application locally, follow these steps:

1. **Clone the repo:**
   
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


