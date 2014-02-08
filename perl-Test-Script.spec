%define upstream_name    Test-Script
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Cross-platform basic tests for scripts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Probe::Perl)

BuildArch:	noarch

%description
The intent of this module is to provide a series of basic tests for scripts in
the bin directory of your Perl distribution.

Further, it aims to provide them with perfect platform-compatibility and in a
way that is as unobtrusive as possible.

That is, if the program works on a platform, then Test::Script should also work
on that platform.

In doing so, it is hoped that Test::Script can become a module that you can
safely make a dependency of your module, without risking your module not
working on some platform because of the dependency.

Where a clash exists between wanting more functionality and maintaining
platform safety, this module will err on the side of platform safety.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.70.0-4mdv2012.0
+ Revision: 765748
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.70.0-3
+ Revision: 764253
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.70.0-2
+ Revision: 667365
- mass rebuild

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 470461
- update to 1.07

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 444245
- update to 1.06

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 442699
- adding missing buildrequires:
- update to 1.05

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 405593
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.03-4mdv2009.0
+ Revision: 258579
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.03-3mdv2009.0
+ Revision: 246550
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 1.03-1mdv2008.1
+ Revision: 177289
- update to new version 1.03

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.0
+ Revision: 64422
- import perl-Test-Script


* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.0
- first mdv release
