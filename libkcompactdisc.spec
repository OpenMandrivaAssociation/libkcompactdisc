Name:		libkcompactdisc
Version: 4.9.2
Release: 1
Epoch:		3
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcompactdisc
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
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
%{_kde_libdir}/libkcompactdisc.so.%{kcompactdisc_major}
%{_kde_libdir}/libkcompactdisc.so.%{kcompactdisc_major}.*

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
%{_kde_libdir}/libkcompactdisc.so
%{_kde_libdir}/cmake/libkcompactdisc
%{_kde_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

