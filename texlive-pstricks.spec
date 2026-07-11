%global tl_name pstricks
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.22a
Release:	%{tl_revision}.1
Summary:	PostScript macros for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/base
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
PSTricks offers an extensive collection of macros for generating
PostScript that is usable with most TeX macro formats, including Plain
TeX, LaTeX, AMS-TeX, and AMS-LaTeX. Included are macros for colour,
graphics, pie charts, rotation, trees and overlays. It has many special
features, including a wide variety of graphics (picture drawing) macros,
with a flexible interface and with colour support. There are macros for
colouring or shading the cells of tables. The package pstricks-add
contains bug-fixes and additions for PSTricks (among other things).
PSTricks ordinarily uses PostScript \special commands, which are not
supported by pdf(La)TeX. This limitation may be overcome by using either
the pst-pdf or the pdftricks package, to generate a PDF inclusion from a
PSTricks diagram. PSTricks macros can also generate PDF output when the
document is processed XeTeX, without the need for other supporting
packages.

