#
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		pyslsk
Version:	1.2.5
Release:	2
License:	GPL
Vendor:		Alexander Kanavin <ak@sensi.org>
Group:		X11/Applications
Source0:	http://www.sensi.org/~ak/pyslsk/%{name}-%{version}.tar.gz
# Source0-md5:	6279775dbef8ef9511950cd0b9a6ee70
Source1:	%{name}.desktop
URL:		http://www.sensi.org/~ak/pyslsk/
BuildRequires:	python-devel > 2.2
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
Requires:	python-wxPython >= 2.4.0
Requires:	python-pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySoulSeek is a client for SoulSeek filesharing system.

%description -l pl
PySoulSeek jest klientem sieci SoulSeek.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install img/bird.jpg $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG KNOWN_BUGS MAINTAINERS README README.import-winconfig TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/pysoulseek
%{_desktopdir}/*
%{_pixmapsdir}/*
