# Chapter 2-Week 2

Goal:  Up and running with Cloud Computing technology

## Part 1:  Getting Started with Cloud Computing Foundations

* [Review Foundations of AWS Cloud Computings Slides](https://docs.google.com/presentation/d/1lOuZsW7SQstJyBeavXTHwBco4OIoQRkI/edit#slide=id.p1)


### High Level Summary

* Three ways to interact with AWS:  Console, Terminal and SDK (Rust, C#, Python, etc)

#### Demo

* Demo console, cli, sdk

[Setup Rust in AWS Cloud 9 Direct Link](https://www.youtube.com/watch?v=R8JnZ4sY4ks)

<iframe width="560" height="315" src="https://www.youtube.com/embed/R8JnZ4sY4ks" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


#### Related videos

* [Install Rust Cloud9](https://learning.oreilly.com/videos/52-weeks-of/080232022VIDEOPAIML/080232022VIDEOPAIML-c1_s17/)
* [Learn AWS CloudShell](https://learning.oreilly.com/videos/52-weeks-of/080232022VIDEOPAIML/080232022VIDEOPAIML-c1_s1/)
* [Powershell EC2 AWS CloudShell](https://learning.oreilly.com/videos/52-weeks-of/080232022VIDEOPAIML/080232022VIDEOPAIML-c1_s2/)

## Part 2: Developing Effective Technical Communication

* Remote work isn't going away ability to work async is critical to success
* Some tips on [Effective Technical Communication](https://paiml.com/docs/home/books/cloud-computing-for-data/chapter01-getting-started/#effective-async-technical-discussions)

### High Level Summary

If someone cannot reproduce what you did, why would they hire you???

* Build 100% reproduceable code: **If not automated it is broken**
    * Automatically tested via GitHub
    * Automatically linted via GitHub
    * Automatically formatted (check for compliance) via GitHub
    * Automatically deployed via GitHub (packages, containers, Microservice)
    * Automatically interactive (people can extend) with GitHub [.devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
    * Incredible `README.md` that shows clearly what you are doing and an architectural diagram.
    * Optional video demo 3-7 minutes (that shows what you did)
    * Include portfolio 
    * Consider using `rust` [mdbook](https://rust-lang.github.io/mdBook/) (what I built this tutorial in) for an extra-special touch.

## Part 3: Using AWS Cloud and Azure Cloud with SDK

### Demo

#### AWS Lambda Rust Marco Polo

* [AWS Lambda Build and Deploy with Rust-Direct Link](https://www.youtube.com/watch?v=jUTiHUTfGYo)

<iframe width="560" height="315" src="https://www.youtube.com/embed/jUTiHUTfGYo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

* [Source for Marco Polo Rust Lambda](https://github.com/nogibjj/rust-mlops-template/tree/main/marco-polo-lambda)

`main.rs` [direct link](https://github.com/nogibjj/rust-mlops-template/blob/main/marco-polo-lambda/src/main.rs).

```rust
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct Request {
    name: String,
}

#[derive(Serialize)]
struct Response {
    req_id: String,
    msg: String,
}

async fn function_handler(event: LambdaEvent<Request>) -> Result<Response, Error> {
    // Extract some useful info from the request
    let name = event.payload.name;
    let logic = match name.as_str() {
        "Marco" => "Polo",
        _ => "Who?",
    };

    // Prepare the response
    let resp = Response {
        req_id: event.context.request_id,
        msg: format!("{} says {}", name, logic),
    };

    // Return `Response` (it will be serialized to JSON automatically by the runtime)
    Ok(resp)
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::INFO)
        // disable printing the name of the module in every log line.
        .with_target(false)
        // disabling time is handy because CloudWatch will add the ingestion time.
        .without_time()
        .init();

    run(service_fn(function_handler)).await
}

```

`Cargo.toml` [direct link](https://github.com/nogibjj/rust-mlops-template/blob/main/marco-polo-lambda/Cargo.toml)

```toml
[package]
name = "marco-polo-lambda"
version = "0.1.0"
edition = "2021"

# Starting in Rust 1.62 you can use `cargo add` to add dependencies 
# to your project.
#
# If you're using an older Rust version,
# download cargo-edit(https://github.com/killercup/cargo-edit#installation) 
# to install the `add` subcommand.
#
# Running `cargo add DEPENDENCY_NAME` will
# add the latest version of a dependency to the list,
# and it will keep the alphabetic ordering for you.

[dependencies]

lambda_runtime = "0.7"
serde = "1.0.136"
tokio = { version = "1", features = ["macros"] }
tracing = { version = "0.1", features = ["log"] }
tracing-subscriber = { version = "0.3", default-features = false, features = ["fmt"] }
```

##### Steps to run

* `make format` to format code
* `make lint` to lint
* `make release-arm` to build for arm which is: `cargo lambda build --release --arm64`
* `make deploy` which is this`cargo lambda deploy`

```Working demo
(.venv) @noahgift ➜ /workspaces/rust-mlops-template/marco-polo-lambda (main) $ make invoke
cargo lambda invoke --remote \
                --data-ascii '{"name": "Marco"}' \
                --output-format json \
                marco-polo-lambda
{
  "msg": "Marco says Polo",
  "req_id": "abc67e2b-a3aa-47fa-98fb-d07eb627577e"
}
```

#### AWS S3 Account Summarizer with Rust

* [Source code for AWS S3 Summarizer](https://github.com/nogibjj/rust-mlops-template/tree/main/awsmetas3)

`lib.rs` [direct link]
```rust
//Information about the AWS S3 service
use aws_config::meta::region::RegionProviderChain;
use aws_sdk_s3::{Client, Error};

// Create a new AWS S3 client
pub async fn client() -> Result<Client, Error> {
    let region_provider = RegionProviderChain::first_try(None)
        .or_default_provider()
        .or_else("us-east-1");
    let shared_config = aws_config::from_env().region(region_provider).load().await;
    let client = Client::new(&shared_config);
    Ok(client)
}

/* return a list of all buckets in an AWS S3 account
*/

pub async fn list_buckets(client: &Client) -> Result<Vec<String>, Error> {
    //create vector to store bucket names
    let mut bucket_names: Vec<String> = Vec::new();
    let resp = client.list_buckets().send().await?;
    let buckets = resp.buckets().unwrap_or_default();
    //store bucket names in vector
    for bucket in buckets {
        bucket_names.push(bucket.name().unwrap().to_string());
    }
    Ok(bucket_names)
}

// Get the size of an AWS S3 bucket by summing all the objects in the bucket
// return the size in bytes
async fn bucket_size(client: &Client, bucket: &str) -> Result<i64, Error> {
    let resp = client.list_objects_v2().bucket(bucket).send().await?;
    let contents = resp.contents().unwrap_or_default();
    //store in a vector
    let mut sizes: Vec<i64> = Vec::new();
    for object in contents {
        sizes.push(object.size());
    }
    let total_size: i64 = sizes.iter().sum();
    println!("Total size of bucket {} is {} bytes", bucket, total_size);
    Ok(total_size)
}

/* Use list_buckets to get a list of all buckets in an AWS S3 account
return a vector of all bucket sizes.
If there is an error continue to the next bucket only print if verbose is true
Return the vector
*/
pub async fn list_bucket_sizes(client: &Client, verbose: Option<bool>) -> Result<Vec<i64>, Error> {
    let verbose = verbose.unwrap_or(false);
    let buckets = list_buckets(client).await.unwrap();
    let mut bucket_sizes: Vec<i64> = Vec::new();
    for bucket in buckets {
        match bucket_size(client, &bucket).await {
            Ok(size) => bucket_sizes.push(size),
            Err(e) => {
                if verbose {
                    println!("Error: {}", e);
                }
            }
        }
    }
    Ok(bucket_sizes)
}
```


`main.rs` [direct link]

```rust
(/*A Command-line tool to Interrogate AWS S3.
Determines information about AWS S3 buckets and objects.
*/
use clap::Parser;
use humansize::{format_size, DECIMAL};

#[derive(Parser)]
//add extended help
#[clap(
    version = "1.0",
    author = "Noah Gift",
    about = "Finds out information about AWS S3",
    after_help = "Example: awsmetas3 account-size"
)]
struct Cli {
    #[clap(subcommand)]
    command: Option<Commands>,
}

#[derive(Parser)]
enum Commands {
    Buckets {},
    AccountSize {
        #[clap(short, long)]
        verbose: Option<bool>,
    },
}

#[tokio::main]
async fn main() {
    let args = Cli::parse();
    let client = awsmetas3::client().await.unwrap();
    match args.command {
        Some(Commands::Buckets {}) => {
            let buckets = awsmetas3::list_buckets(&client).await.unwrap();
            //print count of buckets
            println!("Found {} buckets", buckets.len());
            println!("Buckets: {:?}", buckets);
        }
        /*print total size of all buckets in human readable format
        Use list_bucket_sizes to get a list of all buckets in an AWS S3 account
        */
        Some(Commands::AccountSize { verbose }) => {
            let bucket_sizes = awsmetas3::list_bucket_sizes(&client, verbose)
                .await
                .unwrap();
            let total_size: i64 = bucket_sizes.iter().sum();
            println!(
                "Total size of all buckets is {}",
                format_size(total_size as u64, DECIMAL)
            );
        }
        None => println!("No command specified"),
    }
})
```

`Cargo.toml` [direct link](https://github.com/nogibjj/rust-mlops-template/blob/main/awsmetas3/Cargo.toml)

```toml
[package]
name = "awsmetas3"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
aws-config = "0.52.0"
aws-sdk-s3 = "0.22.0"
tokio = { version = "1", features = ["full"] }
clap = {version="4.0.32", features=["derive"]}
humansize = "2.0.0"
```

#### Related videos

* [Install Rust Cloud9](https://learning.oreilly.com/videos/52-weeks-of/080232022VIDEOPAIML/080232022VIDEOPAIML-c1_s17/)
* [Build Aws Rust S3 Size Calculator](https://learning.oreilly.com/videos/52-weeks-of/080232022VIDEOPAIML/080232022VIDEOPAIML-c1_s18/)

### References

* [Developing on AWS with C# Free PDF O'Reilly book](https://d1.awsstatic.com/developer-center/Developing-on-AWS-with-CSharp.pdf)
* [52 Weeks of AWS-The Complete Series](https://learning.oreilly.com/videos/52-weeks-of/080232022VIDEOPAIML/)
* [Microsoft Azure Fundamentals (AZ-900) Certification](https://learning.oreilly.com/videos/microsoft-azure-fundamentals/27702422VIDEOPAIML/)
* [A Graduate Level Three to Five Week Bootcamp on AWS. Go from ZERO to FIVE Certifications.](https://github.com/noahgift/aws-bootcamp)
* [Duke Coursera Cloud Computing Foundations](https://www.coursera.org/learn/cloud-computing-foundations-duke?specialization=building-cloud-computing-solutions-at-scale)