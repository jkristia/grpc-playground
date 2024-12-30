
## dev environment using docker 

Example of creating a dev environmet using a docker container for any necessary toolchains.  

Rather than using vscode's dev-container environment, this allows you to stay in the local host and only run the container when a build is required, e.g. a protobuf build.  

A personal preference of mine is to:
- use .venv for python
- use nvm for node
- dev / run /debug in vscode on localhost
- only run `./devenv.sh` when a build require tools that I do not want to install on the local host.

Run `make` to see available options

```
$ make
make build-dev-image        - Build dev environment Docker image
make build-run-dev          - Build and run dev image
```


Install npm on ubuntu https://tecadmin.net/how-to-install-nvm-on-ubuntu-20-04/
```
sudo apt install curl 
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.bashrc
```