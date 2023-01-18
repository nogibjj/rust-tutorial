# Chapter 1-Week 1

## Graduate Cloud Computing for Data w/ Rust first approach

* Heuristic:  Rust if you can, Python if you must
* Refer to this guide when needed:  https://paiml.com/docs/home/books/cloud-computing-for-data/chapter01-getting-started/

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

* Weekly Learning Repo Should Mimic This Style: https://github.com/nogibjj/rust-mlops-template, as in many tiny projects get automatically built because of the `Makefile`: https://github.com/nogibjj/rust-mlops-template/blob/main/Makefile

##### Big Projects Repo Spec

Each "big" project should have a dedicted repo for it, a good example is the following repo: https://github.com/noahgift/rdedupe.  Please also follow these additional guidelines:

* Each repo needs a well written README.md with an architectural diagram
* Each repo needs a GitHub release (see example here: https://github.com/rust-lang/mdBook/releases) where a person can run your binary.
* Each repo needs a containerized version of your project where they can build the project and do a `docker pull` to a public container registery like Docker Hub:  https://hub.docker.com
* I would encourage advanced students build a library for one your projects and submit it to crates.io: https://crates.io if it benefits the Rust community (Don't publish junk)
* Each repo needs to publish a benchmark showing performance.  Advanced students may want to consider benchmarking your Rust project against a Python project
* You should default toward building command-line tools with Clap:  https://crates.io/crates/clap and web applications with Actix: https://crates.io/crates/actix, unless you have a compelling reason to switch to a new framework.
* Your repo should include the following continuous integration steps: test, format, lint, publish (deploy as a binary, or deploy as a Microservice).
* Microservices should include logging, see rust-mlops-template for example.
* A good starting point is this Rust new project template:  https://github.com/noahgift/rust-new-project-template  
* Each project should include a reproducable GitHub .devcontainer workflow, see rust-mlops-template for example.

### Structure Each Week

* 3:30-4:45 - Teach
* 4:45-5:00 - Break
* 5:00-6:00 - Teach


#### Projects



