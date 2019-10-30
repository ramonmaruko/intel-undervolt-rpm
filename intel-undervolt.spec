%global commit c0fb98ddc1a4e35207ecb2707a3537fa2f6f9c8c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: intel-undervolt
Version: 0
Release: 1.20190417.git%{shortcommit}%{?dist}
Summary: A tool for undervolting and throttling limits alteration for Intel CPUs.
License: GPLv3
ExclusiveArch: x86_64

BuildRequires: systemd-rpm-macros
%{?systemd_requires}

Source0:  https://github.com/kitsunyan/intel-undervolt/archive/%{commit}/%{name}-%{shortcommit}.tar.gz  
%description
intel-undervolt is a tool for undervolting and throttling limits alteration for
Intel CPUs.

Undervolting works on Haswell and newer CPUs and based on the content of [this
article](https://github.com/mihic/linux-intel-undervolt).

%prep
%autosetup -n intel-undervolt-%{commit}

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} BINDIR=%{_bindir} SYSCONFDIR=%{_sysconfdir} UNITDIR=%{_unitdir} install

%files
%{_bindir}/intel-undervolt
%{_unitdir}/intel-undervolt.service
%{_unitdir}/intel-undervolt-loop.service
%{_sysconfdir}/intel-undervolt.conf

%changelog
* Wed Apr 17 2019 Ramon Marco Layam Navarro <marco@ramonmarco.codes> 0-1.2019047.gitc0fb98d
- Initial package
