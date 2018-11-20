#!/bin/bash
protoc lotus.proto --cpp_out=./ && g++ -Wall -O2 -std=c++17 msg.cpp lotus.pb.cc -o msg -lprotobuf && ./msg | nc localhost 9007
