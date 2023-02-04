# Chapter 4 - Week 4:  Containerized Rust

* Refer to [Web Applications and Command-Line Tools for Data Engineering](https://www.coursera.org/learn/web-app-command-line-tools-for-data-engineering-duke) with a specific focus on Week 3: Python (and .NET) Microservices and Week 4: Python Packaging and Command Line Tools and the lessons focused on containerization.

## Building A Tiny Rust Container for a Command-Line Tool

## Containerized Actix Microservice

* [Containerized Actix Microservice GitHub Project](https://github.com/noahgift/rust-mlops-template/tree/main/webdocker)

`Dockerfile`

```bash
FROM rust:latest as builder
ENV APP webdocker
WORKDIR /usr/src/$APP
COPY . .
RUN cargo install --path .
 
FROM debian:buster-slim
RUN apt-get update && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/cargo/bin/$APP /usr/local/bin/$APP
#export this actix web service to port 8080 and 0.0.0.0
EXPOSE 8080
CMD ["webdocker"]
```

`Cargo.toml`

```toml
[package]
name = "webdocker"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
actix-web = "4"
rand = "0.8"
```

`lib.rs`

```rust
/*A library that returns back random fruit */

use rand::Rng;

//create an const array of 10 fruits
pub const FRUITS: [&str; 10] = [
    "Apple",
    "Banana",
    "Orange",
    "Pineapple",
    "Strawberry",
    "Watermelon",
    "Grapes",
    "Mango",
    "Papaya",
    "Kiwi",
];

//create a function that returns a random fruit
pub fn random_fruit() -> &'static str {
    let mut rng = rand::thread_rng();
    let random_index = rng.gen_range(0..FRUITS.len());
    FRUITS[random_index]
}
```

`main.rs`

```rust
/*An actix Microservice that has multiple routes:
A.  / that turns a hello world
B. /fruit that returns a random fruit
C. /health that returns a 200 status code
D. /version that returns the version of the service
*/

use actix_web::{get, App, HttpResponse, HttpServer, Responder};
//import the random fruit function from the lib.rs file
use webdocker::random_fruit;

//create a function that returns a hello world
#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello World Random Fruit!")
}

//create a function that returns a random fruit
#[get("/fruit")]
async fn fruit() -> impl Responder {
    //print the random fruit
    println!("Random Fruit: {}", random_fruit());
    HttpResponse::Ok().body(random_fruit())
}

//create a function that returns a 200 status code
#[get("/health")]
async fn health() -> impl Responder {
    HttpResponse::Ok()
}

//create a function that returns the version of the service
#[get("/version")]
async fn version() -> impl Responder {
    //print the version of the service
    println!("Version: {}", env!("CARGO_PKG_VERSION"));
    HttpResponse::Ok().body(env!("CARGO_PKG_VERSION"))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    //add a print message to the console that the service is running
    println!("Running the service");
    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(fruit)
            .service(health)
            .service(version)
    })
    .bind("0.0.0.0:8080")?
    .run()
    .await
}
```

Deployed to AWS App Runner via ECR
![Screenshot 2023-01-31 at 1 47 32 PM](https://user-images.githubusercontent.com/58792/215854389-e9f5fc50-1607-4b4d-9d82-180f81c44c01.png)


1. cd into `webdocker`
2. build and run container (can do via `Makefile`) or

`docker build -t fruit .`
`docker run -it --rm -p 8080:8080 fruit`

3. push to ECR
4. Tell AWS App Runner to autodeploy




## Related Demos

