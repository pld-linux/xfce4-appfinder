Summary:	Appfinder for the Xfce Desktop Environment
Summary(pl):	Wyszukiwarka aplikacji dla ¶rodowiska Xfce
Name: 		xfce4-appfinder
Version: 	4.1.99.3
Release: 	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e9ed791a6cd5b084c709003bdc298adc
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires: 	libxfcegui4-devel >= 4.1.0
Requires:	libxfcegui4 >= 4.1.0
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
%{__aclocal} -I m4
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
%{_datadir}/xfce4/doc/C/xfce4-appfinder.html
%{_datadir}/xfce4/doc/C/images/*
