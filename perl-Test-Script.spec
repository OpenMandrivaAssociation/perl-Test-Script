%define upstream_name    Test-Script
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Cross-platform basic tests for scripts
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(IPC::Run3)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/*/*
