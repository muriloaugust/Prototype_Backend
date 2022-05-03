#!/usr/bin/env python
import grpc

from augusto_prototype_backend_protobuf import common_pb2, augusto_prototype_backend_pb2_grpc


channel = grpc.insecure_channel('localhost:51051')
stub = augusto_prototype_backend_pb2_grpc.AugustusServiceStub(channel)


request = common_pb2.IdRequest(id=1)

response = stub.GetFoo(request)

print(response)
