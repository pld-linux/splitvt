Summary:	A program which splits your terminal into two resizable windows.
Summary(pl):    Program który dzieli konsole na dwa okna.
Name:		splitvt
Version:	1.6.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://metalab.unc.edu/pub/Linux/utils/console/%{name}-%{version}.tar.gz
Patch0:		split-pld.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Well, this program just splits your screen into two windows, each
running a shell, so you can do two things at once.
At the moment, only vt100 compatible terminals
(such as xterm, decterm, linux console, etc) will run splitvt.


%description -l pl
Ten program dzieli ekran na dwa okna dzieki czemu mo¿esz uruchomiæ
dwie rzeczy na jednej konsoli.W tym momencie program obs³uguje terminal
vt100 i z nim kompatybilne (takie jak xterm , decterm , konsola linuxowa)

%prep
%setup -q
%patch0 -p1

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_prefix}/man/man1
install -s splitvt $RPM_BUILD_ROOT%{_bindir}
install splitvt.1 $RPM_BUILD_ROOT%{_prefix}/man/man1

gzip -9nf README CHANGES NOTES TODO ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_bindir}/splitvt
%{_prefix}/man/man1/splitvt.1
