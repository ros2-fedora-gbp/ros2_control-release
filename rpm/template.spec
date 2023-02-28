%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-joint-limits
Version:        2.24.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS joint_limits package

License:        Apache License 2.0
URL:            https://github.com/ros-controls/ros2_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-rclcpp
Requires:       ros-humble-rclcpp-lifecycle
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-rclcpp-lifecycle
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-launch-testing-ament-cmake
%endif

%description
Interfaces for handling of joint limits for controllers or hardware.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Feb 28 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.24.0-1
- Autogenerated by Bloom

* Mon Feb 20 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.23.0-1
- Autogenerated by Bloom

* Tue Jan 31 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.22.0-1
- Autogenerated by Bloom

* Tue Jan 24 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.21.0-1
- Autogenerated by Bloom

* Thu Jan 12 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.20.0-1
- Autogenerated by Bloom

* Fri Jan 06 2023 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.19.0-1
- Autogenerated by Bloom

* Sat Dec 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.18.0-1
- Autogenerated by Bloom

* Sun Nov 27 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.17.0-1
- Autogenerated by Bloom

* Mon Oct 17 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.16.0-1
- Autogenerated by Bloom

* Mon Sep 19 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.15.0-1
- Autogenerated by Bloom

* Wed Aug 03 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.13.0-1
- Autogenerated by Bloom

* Thu Jul 14 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.1-1
- Autogenerated by Bloom

* Sat Jul 09 2022 Bence Magyar <bence.magyar.robotics@gmail.com> - 2.12.0-1
- Autogenerated by Bloom

