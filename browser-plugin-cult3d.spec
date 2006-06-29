%define		_orgname	cult3d
%define		_beta	b1
Summary:	A Mozilla plug-in to view Cult3D objects
Summary(pl):	Wtyczka dla przegl±darek opartych na Mozilli do obiektów Cult3D
Name:		browser-plugin-%{_orgname}
Version:	5.2
%define		_rel	0.5
Release:	0.%{_beta}.%{_rel}
License:	?
Group:		X11/Applications/Multimedia
Source0:	http://host.cycore.net/plugins/linux/netscape4/Cult3D_NS4_%{version}%{_beta}.tar.gz
# NoSource0-md5:	9b559a80ac71d9d9eea75a8bf1769489
NoSource:	0
URL:		http://www.cult3d.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# directory where you store the plugin
%define		_plugindir	%{_libdir}/browser-plugins
%define		_classesdir	%{_libdir}/netscape/java/classes

%description
The Cult3D Viewer enables you to view and interact with Cult3D objects
on the Web, in Microsoft Word, PowerPoint, and Excel, as well as Adobe
Acrobat files.

The Viewer is an incredibly small download that will bring the Web and
presentations to life. You can visit any site hosting a Cult3D object
and move it around, and play with its components. For example, if you
got a Web site with a Cult3D car, you can open the doors, look at the
interior - even the backseat, open the hood and trunk, you can even
change the color of the car - all with a click of your mouse!

%description -l pl
Cult3D Viewer pozwala ogl±daæ i pracowaæ z obiektami Cult3D w sieci,
oraz plikach Microsoft Worda, PowerPointa, Excela oraz Adobe Acrobata.

Przegl±darka jest bardzo ma³a i daj±ca ¿ycie prezentacjom WWW. Pozwala
ogl±daæ dowolne serwisy zawieraj±ce obiekty Cult3D i przemieszczaæ je,
przegl±daj±c ich komponenty. Na przyk³ad maj±c stronê WWW z samochodem
Cult3D mo¿na otwieraæ drzwi, patrzeæ na wnêtrze - nawet tylne
siedzenie, otwieraæ maskê i kufer, a nawet zmieniaæ kolor samochodu -
wszystko to klikaj±c myszk±.

%prep
%setup -q -n %{_orgname}-%{version}-%{_beta}-linux-x86
tar xf %{_orgname}.tar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_plugindir},%{_classesdir}}
cp -a %{_orgname}/com $RPM_BUILD_ROOT%{_classesdir}
cp -a %{_orgname}/*.so $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- opera
%nsplugin_install -d %{_libdir}/opera/plugins libcult3dplugin.so

%triggerun -- opera
%nsplugin_uninstall -d %{_libdir}/opera/plugins libcult3dplugin.so

%triggerin -- netscape4-common
%nsplugin_install -d %{_libdir}/netscape/plugins libcult3dplugin.so

%triggerun -- netscape4-common
%nsplugin_uninstall -d %{_libdir}/netscape/plugins libcult3dplugin.so

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*.so
%{_classesdir}
