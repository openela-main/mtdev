%global tarball mtdev
#global gitdate 20110105

Name:           mtdev
Version:        1.1.5
Release:        12%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Multitouch Protocol Translation Library

Group:          System Environment/Libraries
License:        MIT
URL:            http://bitmath.org/code/mtdev/

# upstream doesn't have tarballs

%if 0%{?gitdate}
Source0:        %{tarball}-%{gitdate}.tar.bz2
Source1:        make-git-snapshot.sh
Source2:        commitid
%else
Source0:        http://bitmath.org/code/%{name}/%{name}-%{version}.tar.bz2
%endif

BuildRequires:  autoconf automake libtool gcc

%description
%{name} is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking.

%package devel
Summary:        Multitouch Protocol Translation Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Multitouch protocol translation library development package.

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

%build
autoreconf --force -v --install || exit 1
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/libmtdev.so.*

%files devel
%{_includedir}/mtdev.h
%{_includedir}/mtdev-plumbing.h
%{_includedir}/mtdev-mapping.h
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc
%{_bindir}/mtdev-test

%changelog
* Mon Feb 19 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.1.5-12
- Add gcc to BR

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.5-11
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- remove unnecessary defattr

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Dan Horák <dan[at]danny.cz> 1.1.5-2
- drop ExcludeArch, mtdev becomes the required part of the desktop stack

* Mon Mar 24 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.1.5-1
- mtdev 1.1.5

* Mon Aug 12 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.1.4-1
- mtdev 1.1.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-3
- Less RHEL customization

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-1
- mtdev 1.1.3

* Thu Sep 27 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-4
- fix %%{?dist}

* Mon Aug 13 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-3
- Drop xorg-x11-util-macros build requires, not needed anymore
- Don't build on s390 (or ppc, if on RHEL)
- Force autoreconf to avoid libtool errors

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-1
- mtdev 1.1.2
- upstream provides tarballs now, add the needed spec file changes
 
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3.20110105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2.20110105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.1.0-1.20110105
- Update to release 1.1.0

* Tue Aug 03 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.8-1.20100803
- Update to release 1.0.8

* Thu Jul 08 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.1-2.20100706
- Require util-macros >= 1.5

* Tue Jul 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.1-1.20100706
- Initial package
