%define major 5
%define libname %mklibname KF5Package %{major}
%define devname %mklibname KF5Package -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kpackage
Version:	5.113.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Library to load and install packages of non binary files as they were a plugin
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(PythonInterp)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
Requires: appstream

%description
Library to load and install packages of non binary files as they were a plugin.

%package -n %{libname}
Summary: Library to load and install packages of non binary files as they were a plugin
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Library to load and install packages of non binary files as they were a plugin.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang lib%{name}5 --all-name --with-man

%files -f lib%{name}5.lang
%{_bindir}/kpackagetool5
%{_datadir}/kservicetypes5/kpackage-packagestructure.desktop
%{_datadir}/kservicetypes5/kpackage-generic.desktop
%{_datadir}/kservicetypes5/kpackage-genericqml.desktop
%{_datadir}/qlogging-categories5/kpackage.*categories
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Package

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
