#
# Conditional build
# _with_hyriand - use patch from hydrian
#
%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		pyslsk
Version:	1.1.2
Release:	%{?_with_hyriand:hyriand.}3
License:	GPL
Vendor:         Alexander Kanavin <ak@sensi.org>
Group:		Development/Libraries
Source0:	http://www.sensi.org/~ak/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		http://thegraveyard.org/%{name}/%{name}-%{version}-hyriand-1.7.patch
URL:            http://www.sensi.org/~ak/pyslsk/
BuildRequires:	python-devel > 2.2
BuildRequires:  rpm-pythonprov
BuildArch:	noarch
Requires:	python-wxPython >= 2.3.4
Requires:	python-pyvorbis
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PySoulSeek is a client for SoulSeek filesharing system.

%description -l pl
PySoulSeek jest klientem sieci SoulSeek.

%prep
%setup -q
%{?_with_hyriand:%patch0 -p1}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG KNOWN_BUGS MAINTAINERS README README.import-winconfig TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/pysoulseek
%{_applnkdir}/Network/Misc/%{name}.desktop
