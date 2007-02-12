Summary:	A program which splits your terminal into two resizable windows
Summary(pl.UTF-8):   Program który dzieli konsole na dwa okna
Name:		splitvt
Version:	1.6.5
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://metalab.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
# Source0-md5:	f93974daa4f39945b3d5b9cc39bb1b0f
Patch0:		split-pld.patch
URL:		http://www.devolution.com/~slouken/projects/splitvt/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Well, this program just splits your screen into two windows, each
running a shell, so you can do two things at once.
At the moment, only vt100 compatible terminals
(such as xterm, decterm, linux console, etc) will run splitvt.

%description -l pl.UTF-8
Ten program dzieli ekran na dwa okna dzięki czemu możesz uruchomić dwa
programy na jednej konsoli. W tym momencie program obsługuje terminal
vt100 i z nim kompatybilne (takie jak xterm, decterm, konsola
linuksowa).

%prep
%setup -q
%patch0 -p1

%build
# NOTE: it's not autoconf-generated script - don't use macro
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install splitvt $RPM_BUILD_ROOT%{_bindir}
install splitvt.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES NOTES TODO ANNOUNCE
%attr(755,root,root) %{_bindir}/splitvt
%{_mandir}/man1/splitvt.1*
