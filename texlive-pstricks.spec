# revision 32254
# category Package
# catalog-ctan /graphics/pstricks/base
# catalog-date 2013-11-27 08:19:46 +0100
# catalog-license lppl1.3
# catalog-version 2.47
Name:		texlive-pstricks
Version:	2.47
Release:	3
Summary:	PostScript macros for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/base
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PStricks offers an extensive collection of macros for
generating PostScript that is usable with most TeX macro
formats, including Plain TeX, LaTeX, AMS-TeX, and AMS-LaTeX.
Included are macros for colour, graphics, pie charts, rotation,
trees and overlays. It has many special features, including a
wide variety of graphics (picture drawing) macros, with a
flexible interface and with colour support. There are macros
for colouring or shading the cells of tables. The package
pstricks-add contains bug-fixes and additions for pstricks
(among other things). PSTricks uses PostScript \special
commands, which are not supported by PDF(La)TeX. This
limitation may be overcome by using either the pst-pdf or the
pdftricks package, to generate a PDF inclusion from a PSTricks
diagram. Note that this is one of a pair of catalogue entries
for PSTricks; the other one (PSTricks) is acting as a "stub",
while editorial work on catalogue entries for PSTricks
contributed is completed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pstricks/pst-algparser.pro
%{_texmfdistdir}/dvips/pstricks/pst-dots.pro
%{_texmfdistdir}/dvips/pstricks/pst-dots97.pro
%{_texmfdistdir}/dvips/pstricks/pst-ovl.pro
%{_texmfdistdir}/dvips/pstricks/pstricks.pro
%{_texmfdistdir}/dvips/pstricks/pstricks97.pro
%{_texmfdistdir}/tex/generic/pstricks/config/Changes
%{_texmfdistdir}/tex/generic/pstricks/config/README.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/distiller.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/dvips.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/dvipsone.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/gastex.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/textures.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/vtex.cfg
%{_texmfdistdir}/tex/generic/pstricks/config/xdvipdfmx.cfg
%{_texmfdistdir}/tex/generic/pstricks/pst-fp.tex
%{_texmfdistdir}/tex/generic/pstricks/pst-key.tex
%{_texmfdistdir}/tex/generic/pstricks/pst-ovl.tex
%{_texmfdistdir}/tex/generic/pstricks/pstPlain.tex
%{_texmfdistdir}/tex/generic/pstricks/pstricks.con
%{_texmfdistdir}/tex/generic/pstricks/pstricks.tex
%{_texmfdistdir}/tex/generic/pstricks/pstricks97.tex
%{_texmfdistdir}/tex/latex/pstricks/pst-all.sty
%{_texmfdistdir}/tex/latex/pstricks/pst-doc.cls
%{_texmfdistdir}/tex/latex/pstricks/pst-key.sty
%{_texmfdistdir}/tex/latex/pstricks/pst-ovl.sty
%{_texmfdistdir}/tex/latex/pstricks/pstcol.sty
%{_texmfdistdir}/tex/latex/pstricks/pstricks.sty
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes.dvips
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes.generic
%doc %{_texmfdistdir}/doc/generic/pstricks/Changes.latex
%doc %{_texmfdistdir}/doc/generic/pstricks/PSTricks.bib
%doc %{_texmfdistdir}/doc/generic/pstricks/README
%doc %{_texmfdistdir}/doc/generic/pstricks/ctandir.sty
%doc %{_texmfdistdir}/doc/generic/pstricks/images/flowers.eps
%doc %{_texmfdistdir}/doc/generic/pstricks/images/tiger.eps
%doc %{_texmfdistdir}/doc/generic/pstricks/images/tiger.pdf
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
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news12.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news12.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news13.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-news13.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-user.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/pst-user.tgz
%doc %{_texmfdistdir}/doc/generic/pstricks/pstricks-bug.tex
%doc %{_texmfdistdir}/doc/generic/pstricks/pstricks-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/test-pst.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks/test-pst.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
