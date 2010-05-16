Summary:	xslp - XSLT processor written in Java
Summary(pl.UTF-8):	xslp - procesor XSLT napisany w Javie
Name:		xslp
Version:	1.0
Release:	0.1
License:	distributable
Group:		Development/Languages/Java
Source0:	http://web.archive.org/web/20000818070835/www.clc-marketing.com/xslp/distribution/%{name}-1_0src.zip
# Source0-md5:	98a97cc6b92e405b123506297bb5de25
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSL:P is a free, open-source XSLT processor written in Java. Currently
the processor implements the XSLT WD 1.0 19990421 specification.

%description -l pl.UTF-8
XSL:P to darmowy, mający otwarte źródła procesor XSLT napisany w
Javie. Aktualnie implementuje specyfikację XSLT WD 1.0 19990421.

%prep
%setup -qc

%build
%javac -source 1.4 $(find -name '*.java')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt
# TODO
