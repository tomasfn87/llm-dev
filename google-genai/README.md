# google-genai

## Description

- How to prompt [`Google Gemini`](https://gemini.google.com) to generate out-of-the-box functional code using a [`Google AI Studio API key`](https://aistudio.google.com/api-keys);
- The folder `isValidEmailPhoneOrSocialMediaUrl` is an usage of the main **Python code**, a simple template to generate a **JavaScript function**, save it to a file and check if it works with some kind of test or validation script.

## Download

```shell
git clone --depth 1 --no-checkout https://github.com/tomasfn87/llm-dev ./google-genai && cd google-genai && git sparse-checkout set google-genai && git checkout && mv google-genai/* . && rm -rf {google-genai,.git}
```

- This command will download only this folder from [`llm-dev`](https://github.com/tomasfn87/llm-dev)

## How to use

- From the source folder, run:

```shell
python3 gemini_chat_prompt.py "Output a JavaScript ES5 function code that validates if a string is: 1) an email link, 2) a telephone number link or 3) a social media link (URL) that may or **not** have either protocol section (https:// or http://) or the default/main subdomain (www.); social media must inclue WhatsApp (api.whatsapp.com/send?phone= or wa.me/ URLs) - optimize social regular expression -> don't repeat the '.com' particle - do not skip lines or add any comments of any kind; add 'export default ' before 'function'; function name = 'isValidEmailPhoneOrSocialMediaURL'; max characters per line = 79." > isValidEmailPhoneOrSocialMediaUrl/isValidEmailPhoneOrSocialMediaUrl.js
```

- This command will save the output of the prompt to the file `isValidEmailPhoneOrSocialMediaUrl/isValidEmailPhoneOrSocialMediaUrl.js`;
- It was be specified in the promp that the output must be only **JavaScript code**, and, more specifically, a **function** defined as **default export**:
  - This way we will only have write tests to make sure it works.

---

- From `isValidEmailPhoneOrSocialMediaUrl` folder, run:

```shell
npm test
```

- This command will run the `main.js` file which is made of test-like statements;
- A real test framework should be used here.