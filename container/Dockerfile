FROM ubuntu:latest

# Install Python 3.11 and Node.js 18
RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update
RUN apt install -y sudo protobuf-compiler golang \
	python3.11 python3.11-dev python3.11-venv nodejs npm
RUN npm install -g typescript protoc-gen-js
# https://github.com/chrusty/protoc-gen-jsonschema
RUN go install github.com/chrusty/protoc-gen-jsonschema/cmd/protoc-gen-jsonschema@latest

ENV PATH=$PATH:/project/.home/go/bin:


# RUN mkdir my-module && \
# 	cd my-module && \
# 	go mod init my-module
	# go install github.com/solo-io/protoc-gen-openapi/cmd/protoc-gen-openapi@latest

# RUN go get -u github.com/solo-io/protoc-gen-openapi/cmd/protoc-gen-openapi

# protoc --openapi_out=yaml:. test.proto