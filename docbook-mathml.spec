Summary:	DocBook MathML Module 1.0
Summary(pl):	Specyfikacja DocBook MathML Module 1.0
Name:		docbook-mathml
Version:	1.0
Release:	1
Vendor:		OASIS
License:	Free
Group:		Applications/Publishing/XML
URL:		http://www.oasis-open.org/docbook/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	401aae1f74a43644d37479f4453be247
BuildRequires:	rpm-build >= 4.0.2-94
BuildRequires:	/usr/bin/xmlcatalog
PreReq:		libxml2
Requires(post,preun):	/usr/bin/xmlcatalog
Requires:	libxml2-progs >= 2.4.17-6
Requires:	w3-dtd-mathml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define dtd_path	%{_datadir}/xml/docbook-mathml-dtd-%{version}
%define	xmlcat_file	%{dtd_path}/catalog.xml

%description
DocBook MathML Module 1.0.

%description -l pl
Specyfikacja DocBook MathML Module 1.0.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{dtd_path}

install dbmathml.dtd $RPM_BUILD_ROOT%{dtd_path}

%xmlcat_create $RPM_BUILD_ROOT%{xmlcat_file}

%xmlcat_add_rewrite \
	http://www.oasis-open.org/docbook/xml/mathml/%{version} \
	file://%{dtd_path} \
	$RPM_BUILD_ROOT%{xmlcat_file}

%clean
rm -rf $RPM_BUILD_ROOT

# NOTE: empty lines after %%xmlcat_* are needed by rpm macro with parameters
%post
if ! grep -q %{xmlcat_file} /etc/xml/catalog ; then
    %xmlcat_add %{xmlcat_file}

fi

%preun
if [ "$1" = "0" ] ; then
    %xmlcat_del %{xmlcat_file}

fi

%files
%defattr(644,root,root,755)
%doc testmath.xml
%{dtd_path}
