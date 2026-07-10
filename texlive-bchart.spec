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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides horizontal bar charts, drawn using TikZ on a
numeric X-axis. The focus of the package is simplicity and aesthetics.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bchart
%dir %{_datadir}/texmf-dist/tex/latex/bchart
%doc %{_datadir}/texmf-dist/doc/latex/bchart/CHANGES.txt
%doc %{_datadir}/texmf-dist/doc/latex/bchart/LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/latex/bchart/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bchart/bchart.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bchart/bchart.tex
%{_datadir}/texmf-dist/tex/latex/bchart/bchart.sty
