#!/bin/bash

PROMPT="$1";
OUTPUT_FILE="$2";

RESULT="$(python3 openai_chat_prompt.py "$PROMPT")";
echo "$RESULT";
echo "$RESULT" > "$OUTPUT_FILE";
