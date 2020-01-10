Name: hunspell-nds
Summary: Lowlands Saxon hunspell dictionaries
Version: 0.1
Release: 8%{?dist}
Source: http://downloads.sourceforge.net/aspell-nds/hunspell-nds-0.1.zip
Group: Applications/Text
URL: http://aspell-nds.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Lowlands Saxon hunspell dictionaries.

%prep
%setup -q -n hunspell-nds

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p nds.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/nds_DE.aff
cp -p nds.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/nds_DE.dic
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
nds_DE_aliases="nds_NL"
for lang in $nds_DE_aliases; do
        ln -s nds_DE.aff $lang.aff
        ln -s nds_DE.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README_nds.txt Copyright COPYING
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.1-8
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 3 2008 Caolan McNamara <caolanm@redhat.com> - 0.1-1
- initial version
