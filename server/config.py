from google.protobuf.json_format import MessageToJson
from config_pb2 import Config

def config_testing():

    cfg = Config(id='1')
    json_string = MessageToJson(cfg)
    print(json_string)
    pass

if __name__== '__main__':
    config_testing()
    pass