Name:		texlive-pgf-pie
Version:	63603
Release:	2
Summary:	Draw pie charts, using PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pgf-pie
License:	gpl2 lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-pie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-pie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to draw pie (and variant)
charts, using PGF/TikZ.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pgf-pie
%doc %{_texmfdistdir}/doc/latex/pgf-pie

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
