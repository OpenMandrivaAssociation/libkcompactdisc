%define kf5compactdisc_major 5
%define libkf5compactdisc %mklibname kf5compactdisc %{kf5compactdisc_major}

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkcompactdisc
Version:	20.08.1
Release:	2
Epoch:		3
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcompactdisc
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	ninja
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Phonon4Qt5)
Requires:	%{libkf5compactdisc} = %{EVRD}

%description
KDE library for playing & ripping CDs.

%files -f libkcompactdisc.lang

#------------------------------------------------------------------------------
%package -n %{libkf5compactdisc}
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libkf5compactdisc}
KDE library for playing & ripping CDs.

%files -n %{libkf5compactdisc}
%{_libdir}/libKF5CompactDisc.so.%{kf5compactdisc_major}
%{_libdir}/libKF5CompactDisc.so.%{kf5compactdisc_major}.*

#------------------------------------------------------------------------------
%define devname %mklibname kf5compactdisc -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkf5compactdisc} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.95

%description -n %{devname}
KDE library for playing & ripping CDs.

This package contains header files needed if you wish to build applications
based on libkcompactdisc.

%files -n %{devname}
%{_libdir}/libKF5CompactDisc.so
%{_libdir}/cmake/KF5CompactDisc
%{_libdir}/qt5/mkspecs/modules/qt_KCompactDisc.pri
%{_includedir}/*

#------------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang libkcompactdisc
