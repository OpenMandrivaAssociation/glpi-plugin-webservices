%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
%endif

Summary: Web Services plugin
Name: glpi-plugin-webservices
Version: 1.2.0
Release: %{release}
License: GPL
Group: Monitoring
URL: https://forge.indepnet.net/projects/webservices
Source0: https://forge.indepnet.net/attachments/download/980/glpi-webservices-%{version}.tar.gz
Requires: php-soap
Requires: php-xmlrpc
BuildArch: noarch

%description
This plugin provides a server for Web Services which allow an external
application to check and control GLPI.

%prep

%setup -q -n webservices

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/webservices
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/webservices

%files
%{_datadir}/glpi/plugins/webservices


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2012.0
+ Revision: 771133
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1
+ Revision: 771093
- 1.2.0

* Tue Aug 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-2mdv2011.0
+ Revision: 565525
- fix dependencies

* Tue Aug 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 565488
- import glpi-plugin-webservices


