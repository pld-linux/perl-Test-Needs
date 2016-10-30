#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Needs
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Needs - Skip tests when modules not available
Name:		perl-Test-Needs
Version:	0.002005
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	356634a56c99282e8059f290f5d534c8
URL:		http://search.cpan.org/dist/Test-Needs/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skip test scripts if modules are not available. The requested modules
will be loaded, and optionally have their versions checked. If the
module is missing, the test script will be skipped. Modules that are
found but fail to compile will exit with an error rather than skip.

If used in a subtest, the remainder of the subtest will be skipped.

Skipping will work even if some tests have already been run, or if a
plan has been declared.

Versions are checked via a $module->VERSION($wanted_version) call.
Versions must be provided in a format that will be accepted. No extra
processing is done on them.

If perl is used as a module, the version is checked against the
running perl version ($]). The version can be specified as a number,
dotted-decimal string, v-string, or version object.

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
