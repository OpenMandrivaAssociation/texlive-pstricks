# revision 23858
# category Package
# catalog-ctan /graphics/pstricks/base
# catalog-date 2011-09-05 23:26:33 +0200
# catalog-license lppl
# catalog-version 2.23
Name:		texlive-pstricks
Version:	2.23
Release:	1
Summary:	PostScript macros for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An extensive collection of macros for generating PostScript
that is usable with most TeX macro formats, including Plain
TeX, LaTeX, AMS-TeX, and AMS-LaTeX. Included are macros for
colour, graphics, pie charts, rotation, trees and overlays. It
has many special features, including a wide variety of graphics
(picture drawing) macros, with a flexible interface and with
colour support. There are macros for colouring or shading the
cells of tables. The package pstricks-add contains bug-fixes
and additions for pstricks (among other things). PSTricks uses
PostScript \special commands, which are not supported by
PDF(La)TeX. This limitation may be overcome by using either the
pst-pdf or the pdftricks package, to generate a PDF inclusion
from a PSTricks diagram.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pstricks/pst-algparser.pro
%{_texmfdistdir}/dvips/pstricks/pst-dots.pro
%{_texmfdistdir}/dvips/pstricks/pst-dots97.pro
%{_texmfdistdir}/dvips/pstricks/pst-tools.pro
%{_texmfdistdir}/dvips/pstricks/pstricks.pro
%{_texmfdistdir}/dvips/pstricks/pstricks97.pro
%{_texmfdistdir}/tex/generic/pstricks/config/Changes
%{_texmfdistdir}/tex/generic/pstricks/config/README
%{_texmfdistdir}/tex/generic/pstricks/config/distiller.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/dvips.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/dvipsone.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/textures.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/vtex.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/xdvipdfmx.cfg
%{_texmfdistdir}/tex/generic/pstricks/pst-fp.tex
%{_texmfdistdir}/tex/generic/pstricks/pst-key.tex
%{_texmfdistdir}/tex/generic/pstricks/pstPlain.tex
%{_texmfdistdir}/tex/generic/pstricks/pstricks.con
%{_texmfdistdir}/tex/generic/pstricks/pstricks.tex
%{_texmfdistdir}/tex/generic/pstricks/pstricks97.tex
%{_texmfdistdir}/tex/latex/pstricks/pst-all.sty
%{_texmfdistdir}/tex/latex/pstricks/pst-key.sty
%{_texmfdistdir}/tex/latex/pstricks/pstcol.sty
%{_texmfdistdir}/tex/latex/pstricks/pstricks.sty
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes.dvips
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes.generic
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes.latex
%doc %{_texmfdistdir}/doc/generic/pstricks/Makefile
%doc %{_texmfdistdir}/doc/generic/pstricks/PSTricks.bib
%doc %{_texmfdistdir}/doc/generic/pstricks/README
%doc %{_texmfdistdir}/doc/generic/pstricks/ctandir.sty
%doc %{_texmfdistdir}/doc/generic/pstricks/images/flowers.eps
%doc %{_texmfdistdir}/doc/generic/pstricks/images/tiger.eps
%doc %{_texmfdistdir}/doc/generic/pstricks/images/tiger.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-doc.cls
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-doc.ist
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news.sty
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news05.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news05.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news06.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news06.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news08.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news08.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news09.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news09.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news10.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news10.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news11.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news11.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-quickref.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-user.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-user.tgz
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-usrfull.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews1-10.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews1-10.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews1-11.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews1-11.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews1-12.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews1-12.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews97-15.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pstnews97-15.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pstricks-add-data9.data
%doc %{_texmfdistdir}/doc/generic/pstricks/pstricks-bug.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pstricks-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/test-pst.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/test-pst.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
