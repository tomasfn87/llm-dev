# google-genai

<br>

---

## Description

- How to prompt [`Google Gemini`](https://gemini.google.com) to generate out-of-the-box functional code using a [`Google AI Studio API key`](https://aistudio.google.com/api-keys);
- The folder `isValidEmailPhoneOrSocialMediaUrl` is an usage of the main **Python code**, a simple template to generate a **JavaScript function**, save it to a file and check if it works with some kind of test or validation script.

---

## Download

```shell
git clone \
  --depth 1 \
  --no-checkout https://github.com/tomasfn87/llm-dev ./google-genai \
  && cd google-genai \
  && git sparse-checkout set google-genai \
  && git checkout \
  && mv google-genai/* . \
  && rm -rf {google-genai,.git}
```

- This command will download only this folder from [`llm-dev`](https://github.com/tomasfn87/llm-dev)

---

## Setup

- Copy file `env_template` and rename it to `.env`:
  - Insert your [API key from Google AI Studio](https://aistudio.google.com/api-keys).
- Run the `.sh` files in order to:
  - 1) Create a virtual environment;
  - 2) Start the virtual environment;
  - 3) Install Python dependencies.

---

## How to use

- From the source folder, run:

```shell
./4_ask_gemini_to_generate_code.sh \
  "$(cat ./isValidEmailPhoneOrSocialMediaUrl/prompt.md)" \
  ./isValidEmailPhoneOrSocialMediaUrl/isValidEmailPhoneOrSocialMediaUrl.js
```

- This command will save the output of the prompt to the file `isValidEmailPhoneOrSocialMediaUrl/isValidEmailPhoneOrSocialMediaUrl.js`;
- It must be specified in the prompt that the output must be **only JavaScript code**, and, more specifically, a **function** defined as **default export**:
  - This way we will only have write tests to make sure the function works;
  - The iteration cycle is to change the prompt until all the tests pass, and never touch the code itself, only test code;
    - This means that if new functionalities must be added, then only the prompt must be changed.

---

- From `isValidEmailPhoneOrSocialMediaUrl` folder, run:

```shell
npm test
```

- This command will run the `main.js` file which is made of test-like statements;
- A real test framework should be used here.