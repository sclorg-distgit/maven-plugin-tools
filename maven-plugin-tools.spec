%global pkg_name maven-plugin-tools
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        3.1
Release:        17.14%{?dist}
Epoch:          0
Summary:        Maven Plugin Tools

License:        ASL 2.0
URL:            http://maven.apache.org/plugin-tools/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:      noarch

# Fix NullPointerException in MojoClassVisitor.visit()
# See: rhbz#920042, http://jira.codehaus.org/browse/MPLUGIN-242
Patch0:         %{pkg_name}-rhbz-920042.patch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-parent
BuildRequires:  %{?scl_prefix_java_common}ant
BuildRequires:  maven30-bsh
BuildRequires:  maven30-jtidy
BuildRequires:  maven30-maven-artifact-manager
BuildRequires:  maven30-maven-doxia-sink-api
BuildRequires:  maven30-maven-doxia-sitetools
BuildRequires:  maven30-maven-enforcer-plugin
BuildRequires:  maven30-maven-plugin-annotations
BuildRequires:  maven30-maven-plugin-descriptor
BuildRequires:  maven30-maven-plugin-registry
BuildRequires:  maven30-maven-plugin-tools-annotations
BuildRequires:  maven30-maven-plugin-tools-api
BuildRequires:  maven30-maven-plugin-tools-generators
BuildRequires:  maven30-maven-plugin-tools-java
BuildRequires:  maven30-maven-plugin-tools-model
BuildRequires:  maven30-maven-project
BuildRequires:  maven30-maven-reporting-api
BuildRequires:  maven30-maven-reporting-impl
BuildRequires:  %{?scl_prefix_java_common}objectweb-asm
BuildRequires:  maven30-plexus-ant-factory
BuildRequires:  maven30-plexus-archiver
BuildRequires:  maven30-plexus-bsh-factory
BuildRequires:  maven30-plexus-containers-component-annotations
BuildRequires:  maven30-plexus-containers-component-metadata
BuildRequires:  maven30-plexus-containers-container-default
BuildRequires:  maven30-plexus-utils
BuildRequires:  maven30-plexus-velocity
BuildRequires:  %{?scl_prefix_java_common}qdox
BuildRequires:  maven30-velocity
BuildRequires:  maven30-maven-resources-plugin
# This is parent POM of the plexus-ant-factory. It is not pulled in
# as a dependency of plexus-ant-factory, but we need it, because
# maven-script-ant subpackage fails to build without it.
BuildRequires:  maven30-plexus-component-factories-pom
# Test dependencies:
%if 0
BuildRequires:  %{?scl_prefix_java_common}easymock
BuildRequires:  maven30-fest-assert
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  maven30-maven-plugin-testing-harness
BuildRequires:  maven30-plexus-compiler
BuildRequires:  maven30-xmlunit
%endif


%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n %{?scl_prefix}maven-plugin-annotations
Summary:        Maven Plugin Java 5 Annotations
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{?scl_prefix}maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package -n %{?scl_prefix}maven-plugin-plugin
Summary:        Maven Plugin Plugin
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{?scl_prefix}maven-plugin-plugin
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package annotations
Summary:        Maven Plugin Tool for Annotations
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description annotations
This package provides Java 5 annotation tools for use with Apache Maven.

%package ant
Summary:        Maven Plugin Tool for Ant
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description ant
Descriptor extractor for plugins written in Ant.

%package api
Summary:        Maven Plugin Tools APIs
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package beanshell
Summary:        Maven Plugin Tool for Beanshell
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description beanshell
Descriptor extractor for plugins written in Beanshell.

%package generators
Summary:        Maven Plugin Tools Generators
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package java
Summary:        Maven Plugin Tool for Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description java
Descriptor extractor for plugins written in Java.

# Note that this package contains code, not documentation.
# See comments about "javadocs" subpackage below.
%package javadoc
Summary:        Maven Plugin Tools Javadoc
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description javadoc
The Maven Plugin Tools Javadoc provides several Javadoc taglets to be used when
generating Javadoc.

Java API documentation for %{pkg_name} is contained in
%{pkg_name}-javadocs package. This package does not contain it.

%package model
Summary:        Maven Plugin Metadata Model
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description model
The Maven Plugin Metadata Model provides an API to play with the Metadata
model.

%package -n %{?scl_prefix}maven-script
Summary:        Maven Script Mojo Support
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{?scl_prefix}maven-script
Maven Script Mojo Support lets developer write Maven plugins/goals
with scripting languages instead of compiled Java.

%package -n %{?scl_prefix}maven-script-ant
Summary:        Maven Ant Mojo Support
Requires:       maven30-maven-script = %{epoch}:%{version}-%{release}

%description -n %{?scl_prefix}maven-script-ant
This package provides %{summary}, which write Maven plugins with
Ant scripts.

%package -n %{?scl_prefix}maven-script-beanshell
Summary:        Maven Beanshell Mojo Support
Requires:       maven30-maven-script = %{epoch}:%{version}-%{release}

%description -n %{?scl_prefix}maven-script-beanshell
This package provides %{summary}, which write Maven plugins with
Beanshell scripts.

# This "javadocs" package violates packaging guidelines as of Sep 6 2012. The
# subpackage name "javadocs" instead of "javadoc" is intentional. There was a
# consensus that current naming scheme should be kept, even if it doesn't
# conform to the guidelines.  mizdebsk, September 2012
%package javadocs
Summary:        Javadoc for %{pkg_name}

%description javadocs
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch0 -p1

# For easier installation
ln -s maven-script/maven-script-{ant,beanshell} .

# For com.sun:tools use scope "compile" instead of "system"
%pom_remove_dep com.sun:tools maven-plugin-tools-javadoc
%pom_add_dep com.sun:tools maven-plugin-tools-javadoc

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

# Remove test dependencies because tests are skipped anyways.
%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build -f -s
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles-maven-plugin-tools
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files -n %{?scl_prefix}maven-plugin-annotations -f .mfiles-maven-plugin-annotations

%files -n %{?scl_prefix}maven-plugin-plugin -f .mfiles-maven-plugin-plugin

%files annotations -f .mfiles-maven-plugin-tools-annotations

%files ant -f .mfiles-maven-plugin-tools-ant

%files api -f .mfiles-maven-plugin-tools-api

%files beanshell -f .mfiles-maven-plugin-tools-beanshell

%files generators -f .mfiles-maven-plugin-tools-generators

%files java -f .mfiles-maven-plugin-tools-java

%files javadoc -f .mfiles-maven-plugin-tools-javadoc

%files model -f .mfiles-maven-plugin-tools-model

%files -n %{?scl_prefix}maven-script -f .mfiles-maven-script

%files -n %{?scl_prefix}maven-script-ant -f .mfiles-maven-script-ant

%files -n %{?scl_prefix}maven-script-beanshell -f .mfiles-maven-script-beanshell

%files javadocs -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0:3.1-17.14
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.13
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:3.1-17.12
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 0:3.1-17.11
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:3.1-17.10
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.9
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.8
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Michal Srb <msrb@redhat.com> - 0:3.1-17.7
- Rebuild to fix auto-requires on com.sun:tools

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.6
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.5
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.4
- Add missing BR: maven-parent, plexus-containers-component-metadata

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-17.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 03.1-17
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-16
- Disable test dependencies

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-15
- Fix com.sun:tools dependency

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 0:3.1-14
- Migrate away from mvn-rpmbuild (Resolves: #997516)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-13
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue May  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-12
- Disable resolution of test artifacts

* Thu Apr 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-11
- Remove test dependencies

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-10
- Add patch for MPLUGIN-242
- Resolves: rhbz#920042

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:3.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Dec 21 2012 Michal Srb <msrb@redhat.com> - 0:3.1-7
- Migrated from maven-doxia to doxia subpackage (Resolves: #889147)

* Wed Nov 14 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-6
- Skip running tests because they are failing

* Tue Sep 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-5
- Add missing requires

* Tue Sep 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-4
- Rebuild without bootstrap

* Tue Sep 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-3
- Add obsoletes for maven-plugin-annotations

* Mon Sep 10 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-2
- Bump release

* Fri Sep  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1-1
- Update to upstream version 3.1
- Bootstrap using prebuilt upstream binaries

* Thu Sep  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.7-7
- Remove rpm bug workaround

* Tue Aug 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.7-6
- Wrap descriptions at column 80
- Install LICENSE and NOTICE files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Jaromir Capik <jcapik@redhat.com> -  0:2.7-3
- Missing com.sun.javadoc / com.sun.tools.doclet forced in the POM

* Tue Aug 16 2011 Jaromir Capik <jcapik@redhat.com> -  0:2.7-2
- Removal of plexus-maven-plugin (not needed)
- Migration to maven3
- Removal of unwanted file duplicates
- Minor spec file changes according to the latest guidelines

* Sat Feb 12 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.7-1
- Update to new upstream release.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.6-8
- Remove jtidy depmap (not needed anymore)

* Wed Sep 29 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.6-7
- Add patch for new jtidy
- Add jtidy depmap

* Wed Sep 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.6-6
- BR maven-site-plugin.
- Use javadoc:aggregate for multimodule projects.

* Thu May 27 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.6-5
- Add missing requires.
- Drop modello patches not needed anymore.

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.6-4
- Fix plugin-tools-java obsoletes.

* Tue May 18 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.6-3
- More BRs.

* Tue May 18 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.6-2
- Fix BRs.

* Tue May 18 2010 Alexander Kurtakov <akurtako@redhat.com> 2.6-0
- Update to 2.6.
- Separate modules as subpackages.

* Mon Nov 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.1-6
- BR maven-plugin-tools.

* Mon Aug 31 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.1-5
- Set minimum version for plexus-utils BR.
- BR java-devel.
- Fix javadoc subpackage description.

* Mon Aug 31 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.1-4
- Adapt for Fedora.

* Wed May 20 2009 Fernando Nasser <fnasser@redhat.com> - 0:2.1-3
- Fix license
- Fix URL

* Mon Apr 27 2009 Yong Yang <yyang@redhat.com> - 0:2.1-2
- Add BRs for maven-doxia*
- Rebuild with maven2-2.0.8 built in non-bootstrap mode

* Mon Mar 09 2009 Yong Yang <yyang@redhat.com> - 0:2.1-1
- Import from dbhole's maven2 2.0.8 packages

* Mon Apr 07 2008 Deepak Bhole <dbhole@redhat.com> - 0:2.1-0jpp.1
- Initial build
