%global tl_name bchart
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.3
Release:	%{tl_revision}.1
Summary:	Draw simple bar charts in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bchart
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bchart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bchart.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides horizontal bar charts, drawn using TikZ on a
numeric X-axis. The focus of the package is simplicity and aesthetics.

