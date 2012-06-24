%define		rname qca-ossl
#
%define	snap	20070904
# chrpath stripping fails
%define no_install_post_chrpath 1
Summary:	Qt Cryptographic Architecture (QCA) SSL/TLS plugin
Summary(pl.UTF-8):	Wtyczka SSL/TLS dla Qt Cryptographic Architecture (QCA)
Name:		qt4-plugin-%{rname}
Version:	0.1
Release:	0.%{snap}.1
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/download/qca/2.0/test4/qca-ossl-%{version}-%{snap}.tar.bz2
# Source0-md5:	85713bfebcb8ed4fddf6f6bc8dd930a3
URL:		http://delta.affinix.com/qca/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_libdir}/qt4/plugins/crypto

%description
A plugin to provide SSL/TLS capability to programs that utilize the Qt
Cryptographic Architecture (QCA).

%description -l pl.UTF-8
Wtyczka pozwalająca wykorzystać możliwości SSL/TLS w programach
korzystających z Qt Cryptographic Architecture (QCA).

%prep
%setup -qn %{rname}-%{version}-%{snap}

%build
export QTDIR=%{_libdir}/qt4
./configure

%{_libdir}/qt4/bin/qmake %{rname}.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*.so
