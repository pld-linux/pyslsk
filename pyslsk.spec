%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		pyslsk
Version:	1.1.2
Release:	1	
Source0:	http://www.sensi.org/~ak/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
License:	GPL
Group:		Development/Libraries
Vendor:         Alexander Kanavin <ak@sensi.org>
Url:            http://www.sensi.org/~ak/pyslsk/
BuildRequires:  rpm-pythonprov
BuildRequires:	python-devel > 2.2
BuildArch:	noarch
Requires:	python-wxPython > 2.3
Requires:	python-pyvorbis
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root,755)
%doc CHANGELOG COPYING INSTALL KNOWN_BUGS MAINTAINERS README README.import-winconfig TODO
%{_applnkdir}/Utilities/%{name}.desktop
