%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.10-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Marathi
%define languagecode mr
%define lc_ctype mr_IN

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.10.0
Release:       %mkrel 11
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
Patch1:        marathi-specific-chars-426943.patch
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}
%patch1 -p0
mv u-deva.cset u-deva-mr.cset
mv u-deva.cmap u-deva-mr.cmap

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright README*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-11mdv2011.0
+ Revision: 662851
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-10mdv2011.0
+ Revision: 603434
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-9mdv2010.1
+ Revision: 518944
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-8mdv2010.0
+ Revision: 413087
- rebuild

* Mon Mar 30 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.10.0-7mdv2009.1
+ Revision: 362265
- Add Fedora patch to make aspell-mr and aspell-hi installable at the same time

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.10.0-6mdv2009.1
+ Revision: 350076
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.10.0-5mdv2009.0
+ Revision: 220420
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.10.0-4mdv2008.1
+ Revision: 182490
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.10.0-3mdv2008.1
+ Revision: 148823
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2mdv2007.0
+ Revision: 123323
- Import aspell-mr

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Nov 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.10.0-1mdk
- new release

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.01.0-1mdk
- first version

