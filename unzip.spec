Summary: A utility for unpacking zip files.
Name: unzip
Version: 5.41
Release: 3
Copyright: BSD
Group: Applications/Archiving
Source: ftp://ftp.info-zip.org/pub/infozip/src/unzip541.tar.gz
URL: ftp://ftp.info-zip.org/pub/infozip/UnZip.html
BuildRoot: /var/tmp/unzip-root

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%setup -q 
ln -s unix/Makefile Makefile

%build
%ifarch i386
make linux
%else
make linux_noasm
%endif

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 install

strip $RPM_BUILD_ROOT/usr/bin/{unzip,funzip,unzipsfx}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS COPYING INSTALL
/usr/bin/unzip
/usr/bin/funzip
/usr/bin/unzipsfx
/usr/bin/zipinfo
%{_mandir}/man1/*

%changelog
* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 11 2000 BIll Nottingham <notting@redhat.com>
- rebuild in new env.; FHS fixes.

* Tue Apr 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 4.51 (an acceptable license at last...)

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 5.40

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- builds on non i386 platforms

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
