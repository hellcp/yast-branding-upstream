#
# spec file for package yast2-branding-upstream
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Stasiek Michalski <hellcp@opensuse.org>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           yast2-branding-upstream
Version:        4.2.0
Release:        0
Summary:        YaST2 - Theme
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-branding-upstream

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  yast2-devtools
BuildRequires:  rubygem(yast-rake)

Provides:       yast2-branding = %{version}
Provides:       yast2_theme = %{version}
Provides:       yast2-theme = %{version}

Conflicts:      otherproviders(yast2-branding)
Conflicts:      otherproviders(yast2-theme)
Conflicts:      otherproviders(yast2_theme)

Obsoletes:      yast2-theme-openSUSE
Obsoletes:      yast2-theme-SLE
Obsoletes:      yast2-theme < %{version}
Obsoletes:      yast2-branding-openSUSE

BuildArch:      noarch

%description
Contains necessary theming resources to use YaST2.

%package -n yast2-qt-branding-upstream
Summary:        Theming for YaST2 Qt
License:        GPL-2.0-only
Group:          System/YaST
Supplements:    ((yast2 and libyui-qt) and branding-upstream)
Conflicts:      otherproviders(yast2-qt-branding)
Provides:       yast2-qt-branding = %{version}
BuildArch:      noarch

%description -n yast2-qt-branding-upstream
Upstream branding for YaST2 Qt, mainly used for installation

%package -n yast2-extra-branding-upstream
Summary:        Theming for YaST2 Qt
License:        GPL-2.0-only
Group:          System/YaST
# Worldmap required by country
Supplements:    ((yast2-country and libyui-qt) and branding-upstream)
# Animations required by apparmor module
Supplements:    ((yast2-apparmor and libyui-qt) and branding-upstream)
Conflicts:      otherproviders(yast2-extra-branding)
Provides:       yast2-extra-branding = %{version}
BuildArch:      noarch

%description -n yast2-upstream-branding-upstream
Upstream branding for YaST2 Qt, mainly used for installation

%prep
%setup -n %{name}-%{version}

%build
#Skip build

%install
%{yast_install}

mkdir -p %{buildroot}/etc/icewm/
cp theme/current/wmconfig/* %{buildroot}/etc/icewm/

# Clean out duplicates
%fdupes %{buildroot}%{yast_themedir}

%pre
# CPIO can't remove links on its own
if test -L %{yast_themedir}/current ; then
  rm %{yast_themedir}/current
fi
# No longer used
if test -L %{yast_themedir}/current/icons ; then
  rm %{yast_themedir}/current/icons
fi

%files
%license COPYING
%doc %{yast_docdir}
%dir %{yast_themedir}
%dir %{yast_themedir}/current
%{yast_themedir}/current/wmconfig
%config %{_sysconfdir}/icewm

%files -n yast2-qt-branding-upstream
%{yast_themedir}/current/wizard

%files -n yast2-extra-branding-upstream
%{yast_themedir}/current/worldmap
%{yast_themedir}/current/animations

%changelog
