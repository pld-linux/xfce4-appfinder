Summary:	Appfinder for the XFce Desktop Environment
Summary(pl):	Wyszukiwarka aplikacji dla ¶rodowiska XFce
Name: 		xfce4-appfinder
Version: 	4.1.90
Release: 	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4f71dbbd538c07276bd01d5e9c963bf2
URL:		http://www.xfce.org/
BuildRequires: 	libxfcegui4-devel >= 4.1.0
Requires:	libxfcegui4 >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-appfinder shows system wide installed applications.

%description -l pl
xfce4-appfinder pokazuje aplikacji zainstalowane w systemie.

%prep
%setup -q

%build
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
