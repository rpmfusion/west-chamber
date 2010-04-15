%define kernel_rel 2.6.32.9-70.fc12.x86_64

Name:           west-chamber
Version:        0.0.1
Release:        1%{?dist}
Summary:        iptables extension named after Romance of the West Chamber

Group:          System Environment/Base
License:        GPLv2+
URL:            http://code.google.com/p/scholarzhang/
Source0:        http://scholarzhang.googlecode.com/files/west-chamber-0.0.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  iptables-devel >= 1.4.3
Requires:       iptables >= 1.4.3

Requires: %{name}-kmod >= %{version}
Provides: %{name}-kmod-common = %{version}

%description
This is the package of %{name}, an iptables extension named after the famous Chinese 
ancient friction - Romance of the West Chamber.

%prep
%setup -q


%build
./autogen.sh --prefix=%{_prefix} 
%configure --prefix=%{_prefix}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# kernel modules to be deleted
%define kmodfiles extra/compat_xtables.ko extra/ip_set.ko extra/ip_set_iphash.ko extra/ip_set_ipmap.ko extra/ip_set_ipporthash.ko extra/ip_set_iptree.ko extra/ip_set_iptreemap.ko extra/ip_set_macipmap.ko extra/ip_set_nethash.ko extra/ip_set_portmap.ko extra/ip_set_setlist.ko extra/ipt_SET.ko extra/ipt_set.ko extra/xt_CUI.ko extra/xt_ZHANG.ko extra/xt_gfw.ko modules.alias modules.alias.bin modules.ccwmap modules.dep modules.dep.bin modules.ieee1394map modules.inputmap modules.isapnpmap modules.ofmap modules.pcimap modules.seriomap modules.symbols modules.symbols.bin modules.usbmap 

for kmodfile in %{kmodfiles}
do
  rm -f $RPM_BUILD_ROOT/lib/modules/%{kernel_rel}/$kmodfile
done


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE README USAGE examples/CHINA examples/GOOGLE examples/NOCLIP examples/YOUTUBE
%{_libexecdir}/xtables/libipset_iphash.so
%{_libexecdir}/xtables/libipset_ipmap.so
%{_libexecdir}/xtables/libipset_ipporthash.so
%{_libexecdir}/xtables/libipset_ipportiphash.so
%{_libexecdir}/xtables/libipset_ipportnethash.so
%{_libexecdir}/xtables/libipset_iptree.so
%{_libexecdir}/xtables/libipset_iptreemap.so
%{_libexecdir}/xtables/libipset_macipmap.so
%{_libexecdir}/xtables/libipset_nethash.so
%{_libexecdir}/xtables/libipset_portmap.so
%{_libexecdir}/xtables/libipset_setlist.so
%{_libexecdir}/xtables/libxt_CUI.so
%{_libexecdir}/xtables/libxt_ZHANG.so
%{_libexecdir}/xtables/libxt_gfw.so
%{_sbindir}/ipset
%{_mandir}/man8/ipset.8.gz
%{_mandir}/man8/xtables-addons.8.gz

%changelog
* Wed Mar 17 2010 Caius 'kaio' Chance <kaio at fedoraproject.org> - 0.0.1-3
- Remove kernel modules into -kmod package.

* Tue Mar 16 2010 Caius 'kaio' Chance <kaio at fedoraproject.org> - 0.0.1-2
- Split into userland and kernel-module package.

* Tue Mar 16 2010 Caius 'kaio' Chance <kaio at fedoraproject.org> - 0.0.1-1
- Initial introduction.
