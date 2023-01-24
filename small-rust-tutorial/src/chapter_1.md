# Chapter 1-Week 1

![sd_final (1)](https://user-images.githubusercontent.com/58792/213264730-91ea442f-ec3d-4af2-9975-500c0d9ac7d0.png)

## Demo Video of building a Command-Line Tool in Rust

<iframe width="560" height="315" src="https://www.youtube.com/embed/wl77SW57odA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

* [Link to: Assimilate-Python-For-Rust live demo](https://www.youtube.com/watch?v=wl77SW57odA&t=972s)

## Graduate Cloud Computing for Data w/ Rust first approach

* Heuristic:  Rust if you can, Python if you must
* Refer to these resources when needed:  
    * [Online Book Cloud Computing for Data](https://paiml.com/docs/home/books/cloud-computing-for-data/)
    * [Syllabus](https://noahgift.github.io/cloud-data-analysis-at-scale/syllabus)
    * [Project](https://noahgift.github.io/cloud-data-analysis-at-scale/projects)
    * [New Rust Guide](https://nogibjj.github.io/rust-tutorial/)
    * [GitHub Template Rust New Projects](https://github.com/noahgift/rust-new-project-template)
    * [Rust MLOps Template](https://github.com/nogibjj/rust-mlops-template)
    * [Building Cloud Computing Solutions at Scale Specialization](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale) 

### Key Goals in Semester

* ~1, 500 Rust projects = 100 Students * 15 Weeks
* Build Resume worthy projects
* Projects should be runnable with minimal instructions as command-line tools or microservices deployed to cloud

### How to Accomplish Goals

#### Two different demo channels

* Weekly Learning Demo:  Projects can take 10-60 minutes on average to complete (Text only explanation, screencast optional).  Must show code via link and explain it via `README.md`.
* Weekly Project Progress Demo:  Demo via screencast, required.  Demo should be 3-7 minutes.

#### Two Different Portfolio Styles

##### Weekly Learning Repo Spec 

* Weekly Learning Repo Should Mimic This Style: [https://github.com/nogibjj/rust-mlops-template](https://github.com/nogibjj/rust-mlops-template), as in many tiny projects get automatically built because of the `Makefile`: [https://github.com/nogibjj/rust-mlops-template/blob/main/Makefile](https://github.com/nogibjj/rust-mlops-template/blob/main/Makefile)

##### Big Projects Repo Spec

Each "big" project should have a dedicted repo for it, a good example is the following repo: [https://github.com/noahgift/rdedupe](https://github.com/noahgift/rdedupe).  Please also follow these additional guidelines:

* Each repo needs a well written README.md with an architectural diagram
* Each repo needs a GitHub release (see example here: [https://github.com/rust-lang/mdBook/releases](https://github.com/rust-lang/mdBook/releases)) where a person can run your binary.
* Each repo needs a containerized version of your project where they can build the project and do a `docker pull` to a public container registery like Docker Hub:  [Docker Hub](https://hub.docker.com)
* I would encourage advanced students build a library for one your projects and submit it to crates.io: [https://crates.io](https://crates.io) if it benefits the Rust community (Don't publish junk)
* Each repo needs to publish a benchmark showing performance.  Advanced students may want to consider benchmarking your Rust project against a Python project
* You should default toward building command-line tools with Clap:  [https://crates.io/crates/clap](https://crates.io/crates/clap) and web applications with Actix: [https://crates.io/crates/actix](https://crates.io/crates/actix), unless you have a compelling reason to switch to a new framework.
* Your repo should include the following continuous integration steps: test, format, lint, publish (deploy as a binary, or deploy as a Microservice).
* Microservices should include logging, see rust-mlops-template for example.
* A good starting point is this Rust new project template:  [https://github.com/noahgift/rust-new-project-template](https://github.com/noahgift/rust-new-project-template)  
* Each project should include a reproducable GitHub .devcontainer workflow, see rust-mlops-template for example.

### Structure Each Week

* 3:30-4:45 - Teach
* 4:45-5:00 - Break
* 5:00-6:00 - Teach

#### Projects

##### Team Final Project (Team Size: 3-4): Rust MLOps Microservice

* Build an end-to-end MLOps solution the invokes a model in a cloud platform using only Rust techology (i.e. Pure Rust Code).  Examples could include PyTorch model, or Hugging Face model, or any model packaged with a Microservice. (see guide above about specs)

##### Individual Project #1: Rust CLI

* Build a useful command-line tool in the domain of data engineering or machine learning engineering.  (see guide above about specs)

##### Individual Project #2: Kubernetes (or similar) Microservice in Rust

* Build a useful web microservice in the domain of data engineering or machine learning engineering. (see guide above about specs)

##### Individual Project #3: Interact with Big Data in Rust

* Build a useful web microservice or CLI in the domain of data engineering or machine learning engineering that uses a large data platform. (see guide above about specs)

##### Individual Project #4: Serverless Data Engineering Pipeline with Rust

* Build a useful serverless application in Rust. (see guide above about specs) Also see: [https://noahgift.github.io/cloud-data-analysis-at-scale/projects#project-4](https://noahgift.github.io/cloud-data-analysis-at-scale/projects#project-4). 

##### Optional Advanced Individual Projects 

For advanced students feel free to substitute one of the projects for these domains:

* Web Assembly Rust:  Follow above guidelines, but additionally port your deploy target to Rust Web Assembly.  For example Hugging Face in the browser.

* Build an MLOps platform in Rust that could be a commercial solution (just prototype)

* Build a Rust Game that uses MLOps and runs in the cloud

### Onboarding Day 1

* GitHub Codespaces with Copilot
* AWS Learner Labs
* Azure Free Credits
* More TBD (AWS Credits, etc)

### Getting Started with GitHub Codespaces for Rust

#### rust-new-project-template

All Rust projects can follow this pattern:

1.  Create a new repo using Rust New Project Template:  [https://github.com/noahgift/rust-new-project-template](https://github.com/noahgift/rust-new-project-template)
2.  Create a new Codespaces and use it
3.  Use `main.rs` to call handle CLI and use `lib.rs` to handle logic and import `clap` in `Cargo.toml` as shown in this project.
4.  Use `cargo init --name 'hello' or whatever you want to call your project.
5.  Put your "ideas" in as comments in rust to seed GitHub Copilot, i.e //build add function
6.  Run `make format` i.e. `cargo format`
7.  Run `make lint` i.e. `cargo clippy --quiet`
8.  Run project:  `cargo run -- --help`
9.  Push your changes to allow GitHub Actions to: `format` check, `lint` check, and other actions like binary deploy.


This pattern is a new emerging pattern and is ideal for systems programming in Rust.

![1 1-prompt-engineering](https://user-images.githubusercontent.com/58792/213335664-f459e6ac-018a-4ccf-9563-bbe6d49d72d1.png)

Repo example here: [https://github.com/nogibjj/hello-rust](https://github.com/nogibjj/hello-rust)

#### Reproduce
A good starting point for a new Rust project

To run: `cargo run -- marco --name "Marco"`
Be careful to use the NAME of the project in the `Cargo.toml` to call `lib.rs` as in:

```
[package]
name = "hello"
```

For example, see the name `hello` is invoked alongside `marco_polo` which is in `lib.rs`.

`lib.rs` code:

```rust
/* A Marco Polo game. */

/* Accepts a string with a name.
If the name is "Marco", returns "Polo".
If the name is "any other value", it returns "Marco".
*/
pub fn marco_polo(name: &str) -> String {
    if name == "Marco" {
        "Polo".to_string()
    } else {
        "Marco".to_string()
    }
}
```


`main.rs` code:

```rust
fn main() {
    let args = Cli::parse();
    match args.command {
        Some(Commands::Marco { name }) => {
            println!("{}", hello::marco_polo(&name));
        }
        None => println!("No command was used"),
    }
}
```


##### References

* [rust-cli-template](https://github.com/kbknapp/rust-cli-template)

test