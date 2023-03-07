# Chapter 8-More Serverless

## Hour 1:  Rust with Azure Functions

* Guest Lecture [Alfredo Deza](https://www.linkedin.com/in/alfredodeza/)
* [Deploy Rust on Azure Functions](https://learning.oreilly.com/videos/deploy-rust-on/27965683VIDEOPAIML/)


## Hour2: Step Functions with Rust

Marco, Polo Rust Step Function

Code here:  https://github.com/nogibjj/rust-mlops-template/blob/main/step-functions-rust/README.md

* create new marco polo lambda
`cargo lambda new rust-marco`

Then build, deploy and invoke: `make release` `make deploy` and `make invoke`:

```bash
(.venv) @noahgift ➜ /workspaces/rust-mlops-template/step-functions-rust/rust-marco (main) $ make invoke
cargo lambda invoke --remote \
                --data-ascii '{"name": "Marco"}' \
                --output-format json \
                rust-marco
{
  "payload": "Polo",
  "req_id": "20de1794-1055-4731-9488-7c9217ad195d"
}
```


* create new rust polo lambda
`cargo lambda new rust-polo`


![Screenshot 2023-03-07 at 12 06 12 PM](https://user-images.githubusercontent.com/58792/223496628-e6e6e221-68e4-4930-b1bd-001ebbbb4235.png)

![Screenshot 2023-03-07 at 12 08 48 PM](https://user-images.githubusercontent.com/58792/223496705-08ead2cb-70a0-47da-8fad-e558c3769217.png)


## GCP Cloud Functions

* [Using Gcp Cloud Functions](https://learning.oreilly.com/videos/google-professional-cloud/03032022VIDEOPAIML/03032022VIDEOPAIML-c1_s12/)