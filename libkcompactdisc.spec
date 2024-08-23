#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define kf5compactdisc_major 5
%define libkf5compactdisc %mklibname kf5compactdisc %{kf5compactdisc_major}
%define libkcompactdisc6 %mklibname KCompactDisc6

%bcond_without qt5

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		libkcompactdisc
Version:	24.08.0
Release:	%{?git:0.%{git}.}1
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/libkcompactdisc
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/libkcompactdisc/-/archive/%{gitbranch}/libkcompactdisc-%{gitbranchd}.tar.bz2#/libkcompactdisc-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	ninja
BuildRequires:	pkgconfig(alsa)
BuildRequires:	cmake(ECM)
%if %{with qt5}
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Phonon4Qt5)
%endif
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Phonon4Qt6)
Obsoletes:	plasma6-libkcompactdisc < %{EVRD}

%description
KDE library for playing & ripping CDs.

%files -f libkcompactdisc.lang

#------------------------------------------------------------------------------
%package -n %{libkcompactdisc6}
Summary:        KDE library for playing & ripping CDs
Group:          System/Libraries
Requires:       %{name} = %{EVRD}

%description -n %{libkcompactdisc6}
KDE library for playing & ripping CDs.

%files -n %{libkcompactdisc6}
%{_libdir}/libKCompactDisc6.so.*

#------------------------------------------------------------------------------
%package -n %{libkf5compactdisc}
Summary:	KDE library for playing & ripping CDs
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libkf5compactdisc}
KDE library for playing & ripping CDs.

%if %{with qt5}
%files -n %{libkf5compactdisc}
%{_libdir}/libKF5CompactDisc.so.%{kf5compactdisc_major}
%{_libdir}/libKF5CompactDisc.so.%{kf5compactdisc_major}.*
%endif

#------------------------------------------------------------------------------
%define dev5name %mklibname kf5compactdisc -d

%package -n %{dev5name}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkf5compactdisc} = %{EVRD}

%description -n %{dev5name}
KDE library for playing & ripping CDs.

This package contains header files needed if you wish to build applications
based on libkcompactdisc.

%if %{with qt5}
%files -n %{dev5name}
%{_libdir}/libKF5CompactDisc.so
%{_libdir}/cmake/KF5CompactDisc
%{_includedir}/KF5/KCompactDisc
%{_libdir}/qt5/mkspecs/modules/qt_KCompactDisc.pri
%endif

#------------------------------------------------------------------------------
%define devname %mklibname KCompactDisc6 -d

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkcompactdisc6} = %{EVRD}

%description -n %{devname}
KDE library for playing & ripping CDs.

This package contains header files needed if you wish to build applications
based on libkcompactdisc.

%files -n %{devname}
%{_libdir}/libKCompactDisc6.so
%{_libdir}/cmake/KCompactDisc6
%{_includedir}/KCompactDisc6
%{_libdir}/qt6/mkspecs/modules/qt_KCompactDisc.pri

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DQT_MAJOR_VERSION=6 \
	-G Ninja

%if %{with qt5}
cd ..
export CMAKE_BUILD_DIR=build-qt5
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DQT_MAJOR_VERSION=5 \
	-G Ninja
%endif

%build
%ninja_build -C build
%if %{with qt5}
%ninja_build -C build-qt5
%endif

%install
%if %{with qt5}
%ninja_install -C build-qt5
%endif
%ninja_install -C build

%find_lang libkcompactdisc
