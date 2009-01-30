Name:           superreadahead
Version:        0.01
Release:        %mkrel 1
Summary:        Read ahead pagecontent at boot
Group:          System/Base
URL:            http://repo.moblin.org/moblin/development/source/
License:        GPLv2
Source0:        superreadahead-0.01.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Superreadahead is a read ahead pagecontent at boot.


%prep
%setup -q
# (tv) remove hardocded flags:
%ifarch %ix86
perl -pi -e 's!-march=i686!-march=i586!' Makefile
%else
perl -pi -e 's!-O0 -march=i686!-O2!' Makefile
%endif


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%_sbindir/generate_filelist
%_sbindir/sreadahead


