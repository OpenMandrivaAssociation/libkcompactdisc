%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkcompactdisc
Version:	15.08.0
Release:	1
Epoch:		3
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcompactdisc
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(alsa)

%description
KDE library for playing & ripping CDs.

#------------------------------------------------------------------------------
%define kcompactdisc_major 4
%define libkcompactdisc %mklibname kcompactdisc %{kcompactdisc_major}

%package -n %{libkcompactdisc}
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries

%description -n %{libkcompactdisc}
KDE library for playing & ripping CDs.

%files -n %{libkcompactdisc}
%{_libdir}/libkcompactdisc.so.%{kcompactdisc_major}
%{_libdir}/libkcompactdisc.so.%{kcompactdisc_major}.*

#------------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcompactdisc} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.95

%description devel
KDE library for playing & ripping CDs.

This package contains header files needed if you wish to build applications
based on libkcompactdisc.

%files devel
%{_libdir}/libkcompactdisc.so
%{_libdir}/cmake/libkcompactdisc
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

