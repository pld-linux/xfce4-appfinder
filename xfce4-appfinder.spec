Summary:	Appfinder for the Xfce Desktop Environment
Summary(pl.UTF-8):	Wyszukiwarka aplikacji dla środowiska Xfce
Name:		xfce4-appfinder
Version:	4.13.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce4-appfinder/4.13/%{name}-%{version}.tar.bz2
# Source0-md5:	c2069a14c85c8a3e537b2d4c552d36d2
URL:		http://www.xfce.org/projects/xfce4-appfinder
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	garcon-devel >= 0.4.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.12.0
BuildRequires:	libxfce4util-devel >= 4.12.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfconf-devel >= 4.12.0
Requires:	garcon >= 0.4.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfconf >= 4.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-appfinder shows system wide installed applications.

%description -l pl.UTF-8
xfce4-appfinder pokazuje aplikacje zainstalowane w systemie.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-appfinder
%attr(755,root,root) %{_bindir}/xfrun4
%{_desktopdir}/xfce4-appfinder.desktop
%{_desktopdir}/xfce4-run.desktop
%{_datadir}/metainfo/org.xfce.xfce4-appfinder.appdata.xml
