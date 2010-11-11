
Summary: cronologue is a cron logger capturing output to a central server
Name: cronologue
Version: 0.2.1
Release: 1%{org_tag}%{dist}
URL: https://github.com/gavincarr/%{name}
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: Application/System
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
cronologue is a cron job logger i.e. a wrapper that executes a command,
capturing the stdout and stderr streams produced, and logs a job record
and these output streams back to a central server. Job records and
output files are recorded as plain text files, and pushed to an apache
web server via HTTP PUT.

%package server
Summary: cronologue server package
Group: Applications/System
Requires: httpd

%description server
cronologue server, providing apache configs for capturing job records and
output streams from cronologue clients, and a GUI for viewing.

%prep
%setup

%build

%install
test "%{buildroot}" != "/" && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}
install -m0755 %{name} %{buildroot}%{_bindir}
install -m0644 %{name}.conf %{buildroot}%{_sysconfdir}
install -m0644 server/config/apache.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

%clean
test "%{buildroot}" != "/" && rm -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%doc README COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%files server
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%attr(0755,apache,apache) %{_localstatedir}/www/%{name}

%changelog
* Thu Nov 11 2010 Gavin Carr <gavin@openfusion.com.au> 0.2.1-1
- Bugfix for final job record PUT in cronologue.

* Wed Nov 10 2010 Gavin Carr <gavin@openfusion.com.au> 0.2-1
- Lots of tweaks to cronologue client, further filling out job record.

* Tue Nov 09 2010 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial package, version 0.1.

