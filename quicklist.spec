Name:		quicklist
Summary:	Keep track of "things"
Version:	0.8.6
Release:	5mdk

Source:		%{name}-%{version}.tar.bz2
Group:		Office
URL:		http://www.quicklist.org/
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	GPL
BuildRequires: gtk-devel

%description
QuickList is a free (GPL) gtk+ program for any un*x system with 
gtk+ 1.2 or better that allows novice and experienced users to 
keep track of "things" without any help from a system 
administrator.

"Things" can be anything, including bug lists, phone lists, 
restaurants, team members, calendars, cool urls, checkbooks, 
fishing holes, CDs, bunjee jumping cool sites, etc. It is 
completely flexible.

QuickList can list "things" in column format, much as they 
would appear in a spreadsheet. It is planned to show 
"things" in a one per page in "forms" format. The data can 
be edited in either list form or "form" form.

QuickList can sort lists of "things," search from them and 
print reports from them.

The file format is non-relational, non-SQL.

%prep

%setup -q

%build
%configure
%make

%install
rm -fr %buildroot
%makeinstall

# Menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/quicklist" \
needs="X11" \
section="Office/Tasks Management" \
title="Quicklist" \
longtitle="Keep track of things" \
icon="taskmanagement_section.png"
EOF

cd gtksheet; make clean; cd ..
rm -rf $RPM_BUILD_ROOT/%_prefix/doc

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc ABOUT-NLS INSTALL NEWS README TODO
%doc AUTHORS COPYING 
%doc doc/f* gtksheet
%{_bindir}/*
%_menudir/*

