# llm-dev

<br>

## Requirements

- `docker`

---

## How to use

### 1. How to build

- From the source folder, run:

```shell
docker build -t llm-dev .
```

### 2. How to run

- From the source folder, run:

```shell
docker run --rm -it -v $(pwd)/output:/app/output llm-dev
```

- This command will save the files from the container's `output` folder into the local `output` folder.
