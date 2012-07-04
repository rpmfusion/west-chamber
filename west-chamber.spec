%define svndate 20101017
%define svnver 105

Name:		west-chamber
Summary:	Extensions named after Romance of the West Chamber for iptables
Version:	0.0.1
Release:	8.%{?svndate}svn%{?dist}
License:	GPLv2+
Group:		System Environment/Base
URL:		http://code.google.com/p/scholarzhang/
#Source0:	http://scholarzhang.googlecode.com/files/%{name}-%{version}.tar.gz
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r %{svnver}  http://scholarzhang.googlecode.com/svn/trunk/west-chamber west-chamber-%{svndate}
#  tar -cjvf west-chamber-%{svndate}.tar.bz2 west-chamber-%{svndate}
Source0:	%{name}-%{svndate}.tar.bz2
Patch0:		%{name}-userspace.patch
Patch1:		%{name}-manpage.patch
BuildRequires:	iptables-devel
BuildRequires:	autoconf automake libtool
Requires:	xtables-addons >= 1.30
Provides:	%{name}-kmod-common = %{version}
Requires:	%{name}-kmod >= %{version}

%description
West-chamber is extensions named after the famous Chinese ancient friction - 
Romance of the West Chamber for iptables.

This package provides the userspace libraries for iptables to use extensions 
in the %{name}-kmod package. You must also install the 
%{name}-kmod package.

%prep
%setup -q -n west-chamber-%{svndate}
%patch0 -p1
%patch1 -p1

# remove bundled files from xtables-addons
rm -rf include extensions/compat* 

#do not build bundled xtables-addons modules
sed -i '/build_ipset=m/d' mconfig

%build
./autogen.sh
%configure -with-xtlibdir=/%{_lib}/xtables
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
mv %{buildroot}%{_mandir}/man8/xtables-addons.8 %{buildroot}%{_mandir}/man8/%{name}.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE USAGE examples
/%{_lib}/xtables/*.so
%{_mandir}/man8/*

%changelog
* Wed Jul 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.0.1-8.20101017svn
- Rebuilt for late F-17 mass-rebuilt

* Sat Oct 29 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.0.1-7.20101017svn
- Update for F-16

* Thu Oct 28 2010 Chen Lei <supercyper@163.com> - 0.0.1-6.20101017svn
- svn 105

* Mon Apr 05 2010 Caius 'kaio' Chance <kaio at fedoraproject.org> - 0.0.1-3.20100405svn
- svn 84

* Mon Mar 29 2010 Caius 'kaio' Chance <kaio at fedoraproject.org> - 0.0.1-2.20100329svn
- svn 76

* Mon Mar 16 2010 Caius 'kaio' Chance <kaio at fedoraproject.org> - 0.0.1-1
- Initial introduction
