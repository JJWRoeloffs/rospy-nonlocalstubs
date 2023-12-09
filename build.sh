#!/bin/bash

set -xe

stubgen ros_comm/clients/rospy -o src/
rm src/*.pyi
mv src/rospy src/rospy-stubs
