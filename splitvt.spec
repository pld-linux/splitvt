Summary:	A program which splits your terminal into two resizable windows
Summary(pl.UTF-8):	Program który dzieli konsole na dwa okna
Name:		splitvt
Version:	1.6.6
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.devolution.com/~slouken/projects/splitvt/%{name}-%{version}.tar.gz
# Source0-md5:	ca886884f53c529c149f8945568411ed
Patch0:		split-pld.patch
URL:		http://www.devolution.com/~slouken/projects/splitvt/
BuildRequires:	sed >= 4.0
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
sed -i -e 's/-O2/%{rpmcflags}/' config.c

%build
rm -f Makefile
# NOTE: it's not autoconf-generated script - don't use macro
./configure %{?debug:-d}
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
%doc ANNOUNCE BLURB CHANGES NOTES README TODO escapes examples
%attr(755,root,root) %{_bindir}/splitvt
%{_mandir}/man1/splitvt.1*
