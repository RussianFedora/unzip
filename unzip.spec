Summary: A utility for unpacking zip files.
Name: unzip
Version: 5.50
Release: 33
License: BSD
Group: Applications/Archiving
Source: ftp://ftp.info-zip.org/pub/infozip/src/unzip550.tar.gz
Patch0: unzip542-rpmoptflags.patch
Patch1: unzip-5.50-dotdot.patch
URL: http://www.info-zip.org/pub/infozip/UnZip.html
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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
%patch0 -p1
%patch1 -p1
ln -s unix/Makefile Makefile

%build
make linux_noasm LF2=""

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 install LF2=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS LICENSE INSTALL
/usr/bin/*
%{_mandir}/*/*

%changelog
* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-33
- Rebuild for 9 errata

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-32
- Rebuild for 8.0 errata

* Fri Aug 01 2003 Lon Hohberger <lhh@redhat.com> 5.50-31
- Rebuild for 7.3 errata

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-30
- SECURITY Round 3: Fix up original patch (from 5.50-9) to fix
^V/ exploit, but still allow '-:', which the other patch (5.50-18)
does not allow.  Never allow explicit writing to the root
directory; force users to change there and extract it manually.

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-29
- Rebuild for Severn

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-28
- Rebuild

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-27
- Rebuild for 9

* Wed Jul 30 2003 Lon Hohberger <lhh@redhat.com> 5.50-26
- Rebuild for 8.0

* Tue Jul 22 2003 Lon Hohberger <lhh@redhat.com> 5.50-23
- Rebuild for 7.3

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-22
- Rebuild for Severn

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-21
- Rebuild

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-20
- Rebuild for 9

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-19
- Rebuild for 8.0

* Mon Jul 21 2003 Lon Hohberger <lhh@redhat.com> 5.50-18
- SECURITY: Incorporate far cleaner patch from Ben Laurie
<ben@algroup.co.uk> which also fixes ^V/ (quote-slash).
Patch checks post-decode as opposed to inline as previous
patch does.

* Mon Jun 16 2003 Lon Hohberger <lhh@redhat.com> 5.50-17
- Rebuilt per request

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-16
- Rebuilt

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-15
- Rebuilt

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-14
- Rebuilt: Red Hat Linux 9

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-13
- Rebuilt: Red Hat Enterprise Linux 2.1

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-12
- Rebuilt Red Hat Linux 8.0

* Thu Jun 12 2003 Lon Hohberger <lhh@redhat.com> 5.50-11
- Rebuilt Red Hat Linux 7.3

* Wed Jun 11 2003 Lon Hohberger <lhh@redhat.com> 5.50-10
- Rebuilt

* Wed Jun 11 2003 Lon Hohberger <lhh@redhat.com> 5.50-9
- SECURITY: Scour start of filename for ../ patterns which
include quote and/or control characters.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.50-3
- Rebuild

* Tue Apr  2 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.50-2
- Make it not strip

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.50-1
- 5.50

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.42-3
- Rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 5.42
- Don't strip binaries explicitly
- build without assembly, it doesn't seem to increase performance 
- make it respect RPM_OPT_FLAGS, define _GNU_SOURCE
- use %%{_tmppath}
- "License:" replaces "Copyright:"
- Update URL
- include zipgrep
- COPYING doesn't exist anymore, include LICENSE instead

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
