%define upstream_name    Perl-AtEndOfScope
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl::AtEndOfScope - run some code when a variable goes out of scope
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
It's often necessary to do some cleanup at the end of a scope. This
module creates a Perl object and executes arbitrary code when the object
goes out of scope.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Perl/AtEndOfScope.pm
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404289
- rebuild using %%perl_convert_version

* Thu Jun 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 229224
- update to new version 0.03

* Thu Jun 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.0
+ Revision: 218354
- update to new version 0.02

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-2mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-2mdv2008.0
+ Revision: 86792
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdk
- initial Mandriva package

