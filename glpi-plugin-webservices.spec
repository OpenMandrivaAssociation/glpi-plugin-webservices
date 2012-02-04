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
