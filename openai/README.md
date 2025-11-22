# google-genai

<br>

---

## Description

- How to prompt [`ChatGPT`](https://chat.openai.com) to generate out-of-the-box functional code using a [`Open Router API key`](https://openrouter.ai/settings/keys);
- The folder `isValidEmailPhoneOrSocialMediaUrl` used as example beliw is just a way of testing the main **Python code**, a simple template to generate a **JavaScript function**, save it to a file and check if it works with some kind of test or validation script.

---

## Download

```shell
git clone \
  --depth 1 \
  --no-checkout https://github.com/tomasfn87/llm-dev ./openai \
  && cd google-genai \
  && git sparse-checkout set openai \
  && git checkout \
  && mv openai/* . \
  && rm -rf {openai,.git}
```

- This command will download only this folder from [`llm-dev`](https://github.com/tomasfn87/llm-dev)

---

## Setup

- Rename file `env_template` to `.env`:
  - Insert your [API key from Open Router](https://openrouter.ai/settings/keys).
- Source `setup.sh` in order to:
  - 1) Create a virtual environment;
  - 2) Start the virtual environment;
  - 3) Install Python dependencies with `pip`.

```shell
source ./setup.sh
```

---

## How to use

- From the source folder, run:

```shell
./generate_code_and_save_to_file.sh \
  "$(cat ../isValidEmailPhoneOrSocialMediaUrl/prompt.md)" \
  ../isValidEmailPhoneOrSocialMediaUrl/isValidEmailPhoneOrSocialMediaUrl.js
```

- This command will save the output of the prompt to the file `../isValidEmailPhoneOrSocialMediaUrl/isValidEmailPhoneOrSocialMediaUrl.js`;
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
