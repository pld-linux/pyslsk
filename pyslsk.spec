#
# TODO:
# cleanups (?), pylibogg (?)
#
%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		pyslsk
Version:	1.1.2
Release:	0.1
Source0:	%{name}-%{version}.tar.gz
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
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc CHANGELOG COPYING INSTALL KNOWN_BUGS MAINTAINERS README README.import-winconfig TODO
