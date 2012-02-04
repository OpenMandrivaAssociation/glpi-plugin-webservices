%define plugin webservices
%define name glpi-plugin-%{plugin}
%define version 1.2.0
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Web Services plugin
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/webservices
Source0: https://forge.indepnet.net/attachments/download/980/glpi-webservices-%{version}.tar.gz
BuildArch: noarch
Requires:   php-soap
Requires:   php-xmlrpc
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin provides a server for Web Services which allow an external
application to check and control GLPI.

%prep
%setup -q -n %{plugin}

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/%{plugin}
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/%{plugin}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/glpi/plugins/%{plugin}
