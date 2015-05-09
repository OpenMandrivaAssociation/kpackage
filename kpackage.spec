%define major 5
%define libname %mklibname KF5Package %{major}
%define devname %mklibname KF5Package -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define snapshot %{nil}

Name: kpackage
Version: 5.10.0
Release: 1.%{snapshot}.1
%if "%{snapshot}" != ""
# git clone git://anongit.kde.org/kpackage
Source0: %{name}-%{snapshot}.tar.xz
%else
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
%endif
Patch0: kpackage-compile.patch
Summary: Library to load and install packages of non binary files as they were a plugin
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake >= 2.8.12.2-3
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(PythonInterp)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

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

%prep
%setup -q
%apply_patches
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install
%find_lang lib%{name}5

%files -f lib%{name}5.lang
%{_bindir}/kpackagetool5
%{_datadir}/kservicetypes5/kpackage-packagestructure.desktop
%{_mandir}/man1/kpackagetool5.1.xz
%lang(de) %{_mandir}/de/man1/kpackagetool5.1.xz
%lang(nl) %{_mandir}/nl/man1/kpackagetool5.1.xz
%lang(pt_BR) %{_mandir}/pt_BR/man1/kpackagetool5.1.xz
%lang(sv) %{_mandir}/sv/man1/kpackagetool5.1.xz
%lang(uk) %{_mandir}/uk/man1/kpackagetool5.1.xz

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Package
