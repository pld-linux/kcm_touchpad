%define		subver	00370b5
Summary:	A kcontrol module to control Synaptics touchpad
Name:		kcm_touchpad
Version:	0.3.1
Release:	0.1
Vendor:		Michał Żarłok (mishaaq)
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	f355a658d2e9267fdf4e8d8f88038bcf
#Source0:	http://github.com/mishaaq/kcm_touchpad/tarball/kcm_touchpad-0.3.1
URL:		http://kde-apps.org/content/show.php/kcm_touchpad?content=113335
BuildRequires:	kde4-kdelibs-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A kcontrol module that allow you to control touchpad options.

%prep
%setup -q -n mishaaq-%{name}-%{subver}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README LICENSE AUTHORS
%attr(755,root,root) %{_libdir}/kde4/kcm_touchpad.so
%{_datadir}/kde4/services/*.desktop
