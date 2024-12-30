#!/bin/sh
# set -ex

DOCKER_IMAGE=devenv-image:latest
mkdir -p .home
exec docker run --rm -it \
	--net host \
	--user $(id -u):$(id -g) \
	$(for g in $(id -G) ; do echo "--group-add $g" ; done) \
	-e HOME=/project/.home \
	-v ${PWD}:/project \
	-v /etc/passwd:/etc/passwd:ro \
	-v /etc/group:/etc/group:ro \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-w /project \
	--entrypoint /bin/bash\
	"${DOCKER_IMAGE}" \
	-c 'export PATH=$PATH:/project/.home/.local/bin; bash'
