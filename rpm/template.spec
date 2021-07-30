%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-sensor-filters
Version:        1.0.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS sensor_filters package

License:        BSD
URL:            https://github.com/ctu-vras/sensor_filters
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-filters
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-filters
BuildRequires:  ros-noetic-nodelet
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Simple sensor filter chain nodes and nodelets

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Jul 30 2021 Martin Pecka <peckama2@fel.cvut.cz> - 1.0.5-1
- Autogenerated by Bloom

* Thu Jun 24 2021 Martin Pecka <peckama2@fel.cvut.cz> - 1.0.4-1
- Autogenerated by Bloom

* Thu May 20 2021 Martin Pecka <peckama2@fel.cvut.cz> - 1.0.3-1
- Autogenerated by Bloom

* Thu May 20 2021 Martin Pecka <peckama2@fel.cvut.cz> - 1.0.2-1
- Autogenerated by Bloom

* Wed May 19 2021 Martin Pecka <peckama2@fel.cvut.cz> - 1.0.1-1
- Autogenerated by Bloom

