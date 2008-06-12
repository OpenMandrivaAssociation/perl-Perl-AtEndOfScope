%define real_name Perl-AtEndOfScope

Summary:	Perl::AtEndOfScope - run some code when a variable goes out of scope
Name:		perl-%{real_name}
Version:	0.02
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
It's often necessary to do some cleanup at the end of a scope. This
module creates a Perl object and executes arbitrary code when the object
goes out of scope.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Perl/AtEndOfScope.pm
%{_mandir}/*/*

