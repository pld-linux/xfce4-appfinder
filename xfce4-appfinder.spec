Summary:	Appfinder for the Xfce Desktop Environment
Summary(pl.UTF-8):	Wyszukiwarka aplikacji dla środowiska Xfce
Name:		xfce4-appfinder
Version:	4.7.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce/4.8pre1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	6769edabc4156658aca9422b29c18644
URL:		http://www.xfce.org/projects/xfce4-appfinder/
BuildRequires:	Thunar-devel >= 1.0.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool
BuildRequires:	libtool
#BuildRequires:	libxfce4util-devel >= %{version}
#BuildRequires:	libxfce4ui-devel >= %{version}
BuildRequires:	garcon-devel >= 0.1.3
BuildRequires:	libxfce4util-devel >= 4.7.0
BuildRequires:	libxfce4ui-devel >= 4.7.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.7.0
#BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xfconf-devel >= 4.7.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
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
