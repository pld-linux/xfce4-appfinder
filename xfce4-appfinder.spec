Summary:	Appfinder for the Xfce Desktop Environment
Summary(pl):	Wyszukiwarka aplikacji dla ¶rodowiska Xfce
Name: 		xfce4-appfinder
Version: 	4.2.3
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	fa6b9dd74114cb28c7352dd0e4592ce2
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= 4.2.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools
Requires:	libxfcegui4 >= 4.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-appfinder shows system wide installed applications.

%description -l pl
xfce4-appfinder pokazuje aplikacje zainstalowane w systemie.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-appfinder
%{_desktopdir}/xfce4-appfinder.desktop
%{_pixmapsdir}/xfce4-appfinder.png
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(he) %{_datadir}/xfce4/doc/he/*
