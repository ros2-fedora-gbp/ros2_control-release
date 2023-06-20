%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ros2controlcli
Version:        3.14.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros2controlcli package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-pygraphviz
Requires:       ros-rolling-controller-manager
Requires:       ros-rolling-controller-manager-msgs
Requires:       ros-rolling-rcl-interfaces
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-ros2cli
Requires:       ros-rolling-ros2node
Requires:       ros-rolling-ros2param
Requires:       ros-rolling-rosidl-runtime-py
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-rolling-controller-manager
BuildRequires:  ros-rolling-controller-manager-msgs
BuildRequires:  ros-rolling-rcl-interfaces
BuildRequires:  ros-rolling-rclpy
BuildRequires:  ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ros2cli
BuildRequires:  ros-rolling-ros2node
BuildRequires:  ros-rolling-ros2param
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
BuildRequires:  ros-rolling-ament-xmllint
%endif

%description
The ROS 2 command line tools for ROS2 Control.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Jun 20 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 3.14.0-1
- Autogenerated by Bloom

