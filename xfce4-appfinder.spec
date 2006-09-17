Summary:	Appfinder for the Xfce Desktop Environment
Summary(pl):	Wyszukiwarka aplikacji dla ¶rodowiska Xfce
Name: 		xfce4-appfinder
Version: 	4.3.99.1
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	576b6af7ed7223cbdbccf7df509b8c9f
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= %{version}
Requires(post,postun):	hicolor-icon-theme
Requires:	libxfcegui4 >= %{version}
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
%{__aclocal}
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

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-appfinder
%{_desktopdir}/xfce4-appfinder.desktop
%{_iconsdir}/hicolor/48x48/apps/xfce4-appfinder.png
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
