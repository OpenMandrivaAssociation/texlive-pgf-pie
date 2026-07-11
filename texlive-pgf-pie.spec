%global tl_name pgf-pie
%global tl_revision 63603

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Draw pie charts, using PGF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/pgf-pie
License:	gpl2 lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-pie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgf-pie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(carlisle)
Requires:	texlive(latex)
Requires:	texlive(pgf)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to draw pie (and variant) charts, using
PGF/TikZ.

