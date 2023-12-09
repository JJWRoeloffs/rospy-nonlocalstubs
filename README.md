# rospy-nonlocalstubs

A hack to get your editor to recognize rospy functions without installing ros or rospy on your system. This is for people like me, who run their ROS nodes inside a docker container and therefore don't have ROS installed on the environment they run their editor in.

This makes use of the fact that most editors/LSPs will also check for the PEP 561 -stubs package, even when the base package is not installed, and the fact that type stubs are still valid, even when all arguments are `Any` and `Incomplete`. To reiterate: this is an ugly hack that just happens to work awfully conveniently.

Please do not install this package in any environment that also has ros installed. That might break stuff.

To install, simply run `pip install rospy-nonlocalstubs` in the same environment as the one your editor lives in.

This package can be automatically updated to the latest version of rospy by anyone who has mypy (more specifically, its submodule stubgen) installed:
```sh
# Update the git submodule in which rospy lives
git submodule init && git submodule update

# Generate the stubs with stubgen
./build.sh
```
