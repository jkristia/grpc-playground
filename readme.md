## pb2 to python class generator
`generator/generator.py` generates 'plain' python classes from the protobuf `pb2` generated classes.  
The generated pb2 classes has a few shortcomings, which is why I felt the need for writing this generator.  

This generator will create typed properties and will create constans for all field names. There should not be any hard coded field name in the code, instead the generated constants should be used. To benefit from  this, linting must be enabled to show type errors.

All properties are of `Optional[]` type, so rather than checking for `my_msg.HasField['foo_field']`, simply check for `my_msg.fooField is not None`

To convert back and forth use 
```python
		# protobuf instance
		pb_msg = module_a_pb2.MsgWithTimestamp(
			list_timestamp=[
				Timestamp(seconds=10203040, nanos=456),
				Timestamp(seconds=40302010, nanos=654),
			]
		)
		# convert pb message to py object
		msg = ModuleA_MsgWithTimestamp.from_pb_msg(pb_msg)
		# convert py obj to pb objectg
		pb_msg_2 = ParseDict(msg.to_dict(), module_a_pb2.MsgWithTimestamp())
```

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