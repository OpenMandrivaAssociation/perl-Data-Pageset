%define upstream_name    Data-Pageset
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Page numbering and page sets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Page)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The object produced by Data::Pageset can be used to create page navigation,
it inherits from Data::Page and has access to all methods from this object.

In addition it also provides methods for dealing with set of pages, so that
if there are too many pages you can easily break them into chunks for the
user to browse through.

You can even choose to view page numbers in your set in a 'sliding'
fassion.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2mdv2011.0
+ Revision: 654299
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 624780
- import perl-Data-Pageset

