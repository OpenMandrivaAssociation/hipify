# CUDA-to-HIP translators. TheRock 10.0.

Name:		hipify
Version:	10.0.0
Release:	1
Summary:	CUDA to HIP source translators
License:	MIT
Group:		Development/Tools
URL:		https://github.com/ROCm/HIPIFY
Source0:	https://github.com/ROCm/HIPIFY/archive/refs/tags/therock-10.0.tar.gz#/HIPIFY-therock-10.0.tar.gz

BuildRequires:	rocm-rpm-macros
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	clang-devel >= %{rocm_llvm_maj_ver}
BuildRequires:	llvm-devel >= %{rocm_llvm_maj_ver}
BuildRequires:	llvm-static-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	perl

%description
hipify-clang and hipify-perl convert CUDA sources to HIP. RCCL and
other TheRock components hipify NCCL-shaped trees at build time.

%prep
%autosetup -n HIPIFY-therock-10.0 -p1
sed -i '1s|#!.*python3|#!%{_bindir}/python|' bin/*.sh 2>/dev/null || true

%build
%cmake %{rocm_cmake_fhs} \
	-DCMAKE_BUILD_TYPE=Release \
	-DHIPIFY_CLANG_TESTS=OFF \
	-DHIPIFY_INSTALL_CLANG_HEADERS=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/hipify-clang
%{_bindir}/hipify-perl
%{_bindir}/hipconvertinplace.sh
%{_bindir}/hipconvertinplace-perl.sh
%{_bindir}/hipexamine.sh
%{_bindir}/hipexamine-perl.sh
%{_bindir}/findcode.sh
%{_bindir}/findcode_*.sh
%{_bindir}/finduncodep.sh
