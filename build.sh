#!/bin/bash

set -xe

rm -r src/

stubgen ros_comm/clients/rospy -o src/
rm src/*.pyi
mv src/rospy src/rospy-stubs
