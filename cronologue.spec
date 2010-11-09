
Summary: cronologue is a cron job logger capturing output to a central server
Name: cronologue
Version: 0.1
Release: 1%{org_tag}%{dist}
URL: https://github.com/gavincarr/%{name}
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Application/System
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
cronologue is a cron job logger. That is, it is a wrapper that executes a 
command, capturing the stdout and stderr streams produced, and logs a job 
record and these output streams back to a central server. Job records and 
output files are recorded as plain text files, and pushed to an apache web 
server via HTTP PUT.

%prep
%setup

%build

%install
test "%{buildroot}" != "/" && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
install -m0755 %{name} %{buildroot}%{_bindir}
install -m0755 %{name}.conf %{buildroot}%{_sysconfdir}

%clean
test "%{buildroot}" != "/" && rm -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%doc README COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Tue Nov 09 2010 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial package, version 0.1.

