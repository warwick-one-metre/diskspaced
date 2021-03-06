Name:      observatory-diskspace-client
Version:   20210608
Release:   0
Url:       https://github.com/warwick-one-metre/diskspaced
Summary:   Disk space client.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-diskspace, python3-warwick-observatory-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/diskspace %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/diskspace %{buildroot}/etc/bash_completion.d/diskspace

%files
%defattr(0755,root,root,-)
%{_bindir}/diskspace
/etc/bash_completion.d/diskspace

%changelog
