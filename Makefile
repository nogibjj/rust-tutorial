install:
	cargo install mdbook

build:
	mdbook build small-rust-tutorial

serve:
	mdbook serve -p 8000 -n 127.0.0.1 small-rust-tutorial 

format:
	cargo fmt --quiet

lint:
	cargo clippy --quiet

test:
	cargo test --quiet

run:
	cargo run

release:
	cargo build --release

all: format lint test run
