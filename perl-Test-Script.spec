%define modname	Test-Script
%define modver	1.07

Summary:	Cross-platform basic tests for scripts
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Probe::Perl)

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
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

