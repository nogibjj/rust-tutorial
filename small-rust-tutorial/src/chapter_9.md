# Chapter 9:  AI Pair Assisted Programming and Big Data Storage

## Mini-Lecture A:  Using GitHub Copilot CLI

* [github-copilot-cli](https://www.npmjs.com/package/@githubnext/github-copilot-cli)

tldr: these are the commands

```bash
#!/usr/bin/env bash

#some setup stuff for the dev environment
#install nodejs
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\
sudo apt-get install -y nodejs

#install GitHub Copilot CLI
npm install -g @githubnext/github-copilot-cli

#authenticate with GitHub Copilot
github-copilot-cli auth

#Upgrade
#npm install -g @githubnext/github-copilot-cli
```

* [Watch Copilot Video Link](https://youtube.com/live/F67rjOjEQE4)  
<iframe width="560" height="315" src="https://www.youtube.com/embed/F67rjOjEQE4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Suggestion:  Try out commands via `??` and put them into a `cmd.sh` so you can save both prompt and command
Here is an example of a `cmd.sh`

```bash
### GitHub Copilot Commands
## Prompt: ?? find all large rust target folders and get size and location
## CMD:  find . -name "target" -type d -exec du -sh {} \;

## Prompt:  ?? delete all rust build directories to save space
## CMD: find . -name "target" -type d -exec rm -rf {} \;
```

## Mini-Lecture B:  Building Chat Bot with OpenAI while Using ChatGPT4 as an AI Pair Programming Assistant


In this innovative project, we demonstrate the power of AI-driven pair programming tools, such as ChatGPT-4, OpenAI, and GitHub Copilot, by creating a fully-functional chatbot using the Rust programming language. The chatbot connects to the OpenAI API to provide intelligent, dynamic responses to user input. Throughout the development process, ChatGPT-4 assists with code refactoring and optimization, resulting in a high-quality, production-ready chatbot. This project showcases the remarkable capabilities of AI in augmenting human programming skills and improving code quality.

Here's the output of the tree command, displaying the project structure:
```bash
.
├── Cargo.lock
├── Cargo.toml
├── src
│   ├── chatbot.rs
│   ├── lib.rs
│   └── main.rs
└── tests
    └── test.rs

```

This project consists of the following main components:

- `Cargo.lock` and `Cargo.toml`: Rust's package manager files containing dependencies and metadata.
- `src`: The source code directory containing the main application and library files.
  - `chatbot.rs`: The file containing the chatbot logic, including functions for user input, API calls, and AI response handling.
  - `lib.rs`: The file exposing the chatbot module and its contents, as well as the chat loop function.
  - `main.rs`: The main entry point of the application, initializing the environment and invoking the chat loop function.
- `tests`: The directory containing test files.
  - `test.rs`: The file with test cases for the chatbot functions.


* [Watch Live Coding a Chatbot with Rust and OpenAI](https://www.youtube.com/live/rBhMUAlC9TM?feature=share)
<iframe width="560" height="315" src="https://www.youtube.com/embed/rBhMUAlC9TM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

* [Code here](https://github.com/nogibjj/assimilate-openai/tree/main/chatbot)

`main.rs`
```rust
use chatbot::chatbot::run_chat_loop;
use reqwest::Client;

use std::env;

#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {
    let client = Client::new();

    // Use env variable OPENAI_API_KEY
    let api_key = env::var("OPENAI_API_KEY").expect("OPENAI_API_KEY must be set");
    let url = "https://api.openai.com/v1/completions";

    run_chat_loop(&client, &api_key, url).await?;

    Ok(())
}
```

`lib.rs`
```rust
pub mod chatbot;
```

`chatbot.rs`
```rust
use reqwest::{header, Client};
use serde_json::json;
use serde_json::Value;
use std::io;
use std::io::Write;

pub async fn run_chat_loop(
    client: &Client,
    api_key: &str,
    url: &str,
) -> Result<(), reqwest::Error> {
    let mut conversation = String::from("The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n");

    loop {
        print!("Human: ");
        io::stdout().flush().unwrap();

        let user_input = read_user_input();

        if user_input.to_lowercase() == "quit" || user_input.to_lowercase() == "exit" {
            break;
        }

        conversation.push_str("Human: ");
        conversation.push_str(&user_input);
        conversation.push_str("\nAI: ");

        let json = json!({
            "model": "text-davinci-003",
            "prompt": conversation,
            "temperature": 0.9,
            "max_tokens": 150,
            "top_p": 1.0,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.6,
            "stop": [" Human:", " AI:"]
        });

        let body = call_api(client, api_key, url, json).await?;
        let ai_response = get_ai_response(&body);

        println!("AI: {}", ai_response);

        conversation.push_str(ai_response);
        conversation.push('\n');
    }

    Ok(())
}

pub async fn call_api(
    client: &Client,
    api_key: &str,
    url: &str,
    json: serde_json::Value,
) -> Result<Value, reqwest::Error> {
    let response = client
        .post(url)
        .header(header::AUTHORIZATION, format!("Bearer {}", api_key))
        .header(header::CONTENT_TYPE, "application/json")
        .json(&json)
        .send()
        .await?;

    let body: Value = response.json().await?;
    Ok(body)
}

pub fn get_ai_response(body: &Value) -> &str {
    body["choices"][0]["text"].as_str().unwrap().trim()
}

pub fn read_user_input() -> String {
    let mut user_input = String::new();
    io::stdin().read_line(&mut user_input).unwrap();
    user_input.trim().to_string()
}

```

`tests/test.rs`
```rust
use chatbot::chatbot::get_ai_response;
use serde_json::json;

#[test]
fn test_get_ai_response() {
    let body = json!({
        "choices": [
            {
                "text": " Hello! How can I help you today?\n"
            }
        ]
    });

    let response = get_ai_response(&body);
    assert_eq!(response, "Hello! How can I help you today?");
}
```

## Mini-Lecture C:  Using Azure Databricks


* [Follow Tutorials on Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/)


