%define		_orgname	cult3d
%define		_beta	b1
%define		_rel	0.6
Summary:	A Mozilla plug-in to view Cult3D objects
Summary(pl.UTF-8):	Wtyczka dla przeglądarek opartych na Mozilli do obiektów Cult3D
Name:		browser-plugin-%{_orgname}
Version:	5.2
Release:	0.%{_beta}.%{_rel}
License:	?
Group:		X11/Applications/Multimedia
Source0:	http://host.cycore.net/plugins/linux/netscape4/Cult3D_NS4_%{version}%{_beta}.tar.gz
# NoSource0-md5:	9b559a80ac71d9d9eea75a8bf1769489
NoSource:	0
URL:		http://www.cult3d.com/
BuildRequires:	rpmbuild(macros) >= 1.357
Requires:	browser-plugins >= 2.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Cult3D Viewer pozwala oglądać i pracować z obiektami Cult3D w sieci,
oraz plikach Microsoft Worda, PowerPointa, Excela oraz Adobe Acrobata.

Przeglądarka jest bardzo mała i dająca życie prezentacjom WWW. Pozwala
oglądać dowolne serwisy zawierające obiekty Cult3D i przemieszczać je,
przeglądając ich komponenty. Na przykład mając stronę WWW z samochodem
Cult3D można otwierać drzwi, patrzeć na wnętrze - nawet tylne
siedzenie, otwierać maskę i kufer, a nawet zmieniać kolor samochodu -
wszystko to klikając myszką.

%prep
%setup -q -n %{_orgname}-%{version}-%{_beta}-linux-x86
tar xf %{_orgname}.tar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_browserpluginsdir},%{_classesdir}}
cp -a %{_orgname}/com $RPM_BUILD_ROOT%{_classesdir}
install %{_orgname}/*.so $RPM_BUILD_ROOT%{_browserpluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_browserpluginsdir}/*.so
%{_classesdir}
