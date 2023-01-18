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

deploy:
	@echo "====> deploying to github"
	git worktree add /tmp/book gh-pages
	mdbook build small-rust-tutorial
	rm -rf /tmp/book/*
	cp -rp small-rust-tutorial/book/* /tmp/book/
	cd /tmp/book && \
		git add -A && \
		git commit -m "deployed on $(shell date) by ${USER}" && \
		git push origin gh-pages
		git update-ref -d refs/heads/gh-pages

all: format lint test run
