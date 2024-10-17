Name:           sreadahead
Version:        1.0
Release:        5
Summary:        Read ahead pagecontent at boot
Group:          System/Base
URL:            https://code.google.com/p/sreadahead/
License:        GPLv2
Source0:        http://sreadahead.googlecode.com/files/sreadahead-1.0.tar.gz
# (fc) 1.0-1mdv allow to change default timeout (SVN)
Patch0:		sreadahead-1.0-timeout.patch
# (fc) 1.0-1mdv enable ftrace_printk for monitoring
Patch1:		sreadahead-1.0-ftrace_printk.patch
# (fc) 1.0-1mdv ignore file from debugfs
Patch2:		sreadahead-1.0-debugfsmnt.patch
# (fc) 1.0-2mdv fix for 2.6.29 kernel
Patch3:		sreadahead-1.0-2629.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Sreadahead is a read ahead pagecontent at boot.


%prep
%setup -q
%patch0 -p1 -b .timeout
%patch1 -p1 -b .ftrace_printk
%patch2 -p1 -b .debugfsmnt
%patch3 -p1 -b .2629

%build
%make CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/sreadahead/debugfs


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
/sbin/sreadahead
%{_var}/lib/sreadahead


%changelog
* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 1.0-4mdv2012.0
+ Revision: 701633
- rebuild

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2011.0
+ Revision: 445229
- rebuild

* Fri Feb 20 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0-2mdv2009.1
+ Revision: 343374
- Patch3: fix for 2.6.29 kernel

* Thu Feb 05 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0-1mdv2009.1
+ Revision: 337894
- Release 1.0 (name changed)
- Patch0 (SVN): allow to change timeout
- Patch1: enable ftrace_printk
- Patch2: ignore file from debugfs
- Upstream project changed name

* Mon Nov 17 2008 Thierry Vignaud <tv@mandriva.org> 0.01-1mdv2009.1
+ Revision: 304008
- import superreadahead

