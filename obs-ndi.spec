#
# spec file for package obs-ndi
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

%global debug_package %{nil}
# 
#define _legacy_common_support 1

Name:           obs-ndi
Version:        4.9.1
Release:        2%{dist}
Summary:        Network A/V in OBS Studio with NewTek's NDI technology
License:        GPLv2
Group:		Applications/Multimedia
URL:            https://github.com/Palakis/obs-ndi

Source0:	https://github.com/Palakis/obs-ndi/archive/%{version}.tar.gz
Patch:		ndi-sdk_path.patch
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:	obs-studio-devel >= 26.0.0
	
BuildRequires:  gcc-c++
BuildRequires:  cmake
Requires:	libndi-sdk

%description
Network A/V in OBS Studio with NewTek's NDI technology.


%prep
%autosetup -p1


%build
mkdir -p %{_target_platform}; pushd %{_target_platform}
%cmake \
	-DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DOBS_MULTIARCH_SUFFIX="%(echo %{_lib} | sed -e 's/lib//')" \
	-DLIBOBS_INCLUDE_DIR=%{_includedir}/obs \
	-DLIBOBS_LIB=%{_libdir} \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
	-DBUILD_TESTING=OFF -Wno-dev ..

%make_build 

%install
pushd %{_target_platform}
%make_install


%files 
%license LICENSE
%doc README.md
%{_libdir}/obs-plugins/obs-ndi.so
%{_datadir}/obs/obs-plugins/obs-ndi/


%changelog

* Sat Sep 05 2020 David Va <davidva AT tuta DOT io> 4.9.1-2
- Requires libndi-sdk
- Multilib changes

* Thu Aug 27 2020 David Va <davidva AT tuta DOT io> 4.9.1-1
- Initial build
