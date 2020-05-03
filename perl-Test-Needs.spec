#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Needs
Summary:	Test::Needs - skip tests when modules not available
Summary(pl.UTF-8):	Test::Needs - pomijanie testów, jeśli moduły nie są dostępne
Name:		perl-Test-Needs
Version:	0.002006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d5c96d51d8d5510f7c0b7f354c49af1c
URL:		https://metacpan.org/release/Test-Needs
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skip test scripts if modules are not available. The requested modules
will be loaded, and optionally have their versions checked. If the
module is missing, the test script will be skipped. Modules that are
found but fail to compile will exit with an error rather than skip.

%description -l pl.UTF-8
Moduł pozwalający na pomijanie skryptów testowych, jeśli moduły nie są
dostępne. Żądane moduły są ładowane, a ich wersje opcjonalnie
sprawdzane. Jeśli modułu brakuje, skrypt testowy jest pomijany; moduły
znalezione, ale nie kompilujące się powodują zakończenie testu z
błędem zamiast pominięcia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Needs.pm
%{_mandir}/man3/Test::Needs.3*
