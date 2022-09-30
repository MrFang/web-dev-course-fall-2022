gRPC server which can return files with content from given directory


To compile protobuf files run 
```sh
python -m grpc_tools.protoc --proto_path 'app/proto=proto' --python_out=. proto/messages.proto \
  && python -m grpc_tools.protoc --proto_path 'app/proto=proto' --grpc_python_out=. proto/services.proto
```
`grpc_tools` module will be installed with development dependencies

To run server execute `PYTHONPATH=. python app/server.py <content-root>`. Content root must be relative path and exist
To run client execute `PYTHONPATH=. python app/client.py`

To run tests execute: `python -m unittest discover -s app/ -p "tests*
