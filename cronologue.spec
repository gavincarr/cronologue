
Summary: cronologue is a cron logger capturing output to a central server
Name: cronologue
Version: 0.6
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
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/cron.d
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}/config
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}/data
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}/plugins
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}/state
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}/themes/default
mkdir -p %{buildroot}%{_localstatedir}/www/%{name}/themes/images
# Client
install -m0755 %{name} %{buildroot}%{_bindir}
install -m0644 %{name}.conf %{buildroot}%{_sysconfdir}
pod2man %{name} > %{buildroot}%{_mandir}/man1/%{name}.1
# Server
install -m0644 server/config/apache.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -m0644 server/config/cronologue.cron %{buildroot}%{_sysconfdir}/cron.d/cronologue
install -m0644 server/config/statik.conf %{buildroot}%{_localstatedir}/www/%{name}/config
install -m0644 server/config/plugins.conf %{buildroot}%{_localstatedir}/www/%{name}/config
install -m0644 server/plugins/* %{buildroot}%{_localstatedir}/www/%{name}/plugins
install -m0644 server/themes/*.css %{buildroot}%{_localstatedir}/www/%{name}/themes
install -m0644 server/themes/default/page.* %{buildroot}%{_localstatedir}/www/%{name}/themes/default
install -m0644 server/themes/images/* %{buildroot}%{_localstatedir}/www/%{name}/themes/images

%clean
test "%{buildroot}" != "/" && rm -rf %{buildroot}

%post

%files
%defattr(-,root,root)
%doc README COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}*

%files server
%defattr(-,root,apache)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%dir %attr(2755,root,apache) %{_localstatedir}/www/%{name}
%dir %attr(2755,apache,apache) %{_localstatedir}/www/%{name}/data
%dir %attr(2755,apache,apache) %{_localstatedir}/www/%{name}/state
%dir %{_localstatedir}/www/%{name}/config
%config(noreplace) %{_localstatedir}/www/%{name}/config/*
%{_localstatedir}/www/%{name}/plugins
%{_localstatedir}/www/%{name}/themes

%changelog
* Wed Jun 29 2011 Gavin Carr <gavin@openfusion.com.au> 0.6-1
- Migrate to statik-based frontend, bump to 0.6.

* Mon Jan 17 2011 Gavin Carr <gavin@openfusion.com.au> 0.5.3-2
- Add %dist tag back again, since rhel6 can't build for centos{4,5}.

* Fri Jan 14 2011 Gavin Carr <gavin@openfusion.com.au> 0.5.3-1
- Remove %dist tag from spec file (not dist-specific).

* Fri Dec 03 2010 Gavin Carr <gavin@openfusion.com.au> 0.5.2-1
- Add a --error|-e option to cronologue.

* Wed Nov 24 2010 Gavin Carr <gavin@openfusion.com.au> 0.5.1-1
- Add a --passthru|-p option to cronologue.

* Fri Nov 19 2010 Gavin Carr <gavin@openfusion.com.au> 0.5-1
- Add report=always|stream to config, and -a|-s options to cronologue.
- Add --config|-c <config_file> option to cronologue.
- Fill out cronologue perldocs a bit more.
- Add a man page to the spec file.

* Tue Nov 16 2010 Gavin Carr <gavin@openfusion.com.au> 0.4-1
- Get RSS feeds working, and add links to page template.
- Make tables more explicit and tweak styling.
- Fix buglet with cronologue return code not being >> 8.

* Thu Nov 11 2010 Gavin Carr <gavin@openfusion.com.au> 0.3.1-1
- Migrate cronologue from IPC::Run to IPC::Run3 for exec $scalar support.
- Fix buglet with cronologue MKCOL url.
- Minor gui tweakages.

* Thu Nov 11 2010 Gavin Carr <gavin@openfusion.com.au> 0.3-1
- Initial gui version, included in server package.

* Thu Nov 11 2010 Gavin Carr <gavin@openfusion.com.au> 0.2.1-1
- Bugfix for final job record PUT in cronologue.

* Wed Nov 10 2010 Gavin Carr <gavin@openfusion.com.au> 0.2-1
- Lots of tweaks to cronologue client, further filling out job record.

* Tue Nov 09 2010 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial package, version 0.1.

