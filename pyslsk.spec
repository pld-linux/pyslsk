#
# Conditional build
# _with_hyriand - use patch from hydrian
#
%define		_rel	4
%include        /usr/lib/rpm/macros.python
Summary:	Client for SoulSeek filesharing system
Summary(pl):	Klient sieci SoulSeek
Name:		pyslsk
version:	1.2.2
Release:	%{?_with_hyriand:hyriand.}%{_rel}
License:	GPL
Vendor:		Alexander Kanavin <ak@sensi.org>
Group:		X11/Applications
Source0:	http://www.sensi.org/~ak/pyslsk/%{name}-%{version}.tar.gz
# Source0-md5:	1dc4e164c908be21c06a8858047d949e
Source1:	%{name}.desktop
Patch0:		http://thegraveyard.org/pyslsk/%{name}-%{version}-hyriand-7.patch
URL:		http://www.sensi.org/~ak/pyslsk/
BuildRequires:	python-devel > 2.2
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
Requires:	python-wxPython >= 2.3.4
Requires:	python-pyvorbis
%{?_with_hyriand:Conflicts: %{name} = %{version}-%{_rel}}
%{!?_with_hyriand:Conflicts: %{name} = %{version}-hyriand.%{_rel}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
