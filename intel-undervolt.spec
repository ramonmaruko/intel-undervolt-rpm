Name: intel-undervolt
Version: 1.7
Release: 2%{?dist}
Summary: A tool for undervolting and throttling limits alteration for Intel CPUs
License: GPLv3
ExclusiveArch: x86_64

BuildRequires: gcc systemd-rpm-macros
%{?systemd_requires}

Source0:  https://github.com/kitsunyan/%{name}/archive/%{version}.tar.gz  

%description
intel-undervolt is a tool for undervolting and throttling limits alteration for
Intel CPUs.

Undervolting works on Haswell and newer CPUs and based on the content of [this
article](https://github.com/mihic/linux-intel-undervolt).

%prep
%autosetup -n %{name}-%{version}

%build
%configure --enable-systemd --unitdir=%{_unitdir}
%make_build CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" 

%install
%make_install

%files
%{_bindir}/intel-undervolt
%{_unitdir}/intel-undervolt.service
%{_unitdir}/intel-undervolt-loop.service

%config(noreplace) %{_sysconfdir}/intel-undervolt.conf

%changelog
* Wed Oct 30 2019 Ramon Marco Layam Navarro <marco@ramonmarco.codes> 1.7-2
- Use make_build and make_install macros
- Add unitdir to configure

* Wed Oct 30 2019 Ramon Marco Layam Navarro <marco@ramonmarco.codes> 1.7-1
- Add configure call
- Add intel-undervolt.conf as config file
- Add description

* Wed Apr 17 2019 Ramon Marco Layam Navarro <marco@ramonmarco.codes> 0-1.2019047.gitc0fb98d
- Initial package
