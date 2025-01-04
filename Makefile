help:
	@awk -F ':|##' '/^[^\t].+:.*##/ { printf "\033[36mmake %-28s\033[0m -%s\n", $$1, $$NF }' $(MAKEFILE_LIST) | sort

PHONY: build-dev-image
build-dev-image: ## Build dev environment Docker image
	@docker build -f container/Dockerfile -t devenv-image:latest .

PHONY: build-run-dev
build-run-dev: build-dev-image ## Build and run dev image
	./devenv.sh

PHONY: api
api: ## build proto api
	mkdir -p ./proto_out

	python3 -m grpc_tools.protoc -I. \
	--proto_path=./proto \
	--python_out=./proto_out \
	--mypy_out=./proto_out \
	--grpc_python_out=./proto_out \
		fileservice.proto \
		test.proto \
		foo.proto \
		config.proto \
		generator_test/module-a.proto \
		generator_test/module-b.proto \

PHONY: install
install: ## install dependencies
	pip install -r requirements.txt