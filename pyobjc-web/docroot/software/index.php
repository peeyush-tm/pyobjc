<?
$title = "Documentation";
$cvs_author = '$Author: ronaldoussoren $';
$cvs_date = '$Date: 2003/10/19 19:23:59 $';

include "header.inc";
?>

<h1>Downloads</h1>

<ul>
<li><a href="http://prdownloads.sourceforge.net/pyobjc/pyobjc-1.0.dmg?download">PyObjC 1.0 installer package for Apple's Python</a>
<li><a href="http://prdownloads.sourceforge.net/pyobjc/pyobjc-1.0.tar.gz?download">PyObjC 1.0 source release (a compressed tar archive)</a>
</ul>

<p>Users of MacPython can use the PyObjC PackageManager database to install 
   PyObjC: select ``File/open URL...`` in Package Manager and select 
   "<CODE>http://pyobjc.sf.net/packman/pyobjc-stable-6.6-Power_Macintosh.plist</CODE>" as the URL. 

 <p>Users of MacPython on MacOS X 10.3 can use "<CODE>"http://pyobjc.sf.net/packman/pyobjc-stable-7.0-Power_Macintosh.plist</CODE>" as the database location. 
 There is no MacOS X 10.3 installer at the moment.

<p>Older releases are available in the <a href="http://sourceforge.net/project/showfiles.php?group_id=14534">Files section of our SourceForge project</a>.

<p>If you want to install PyObjC from CVS you'll have to download the latest 
archive with libFFI <a href="http://prdownloads.sourceforge.net/pyobjc/libffi-src-20030921.tar.gz?download">here</a>. This is not an official libffi release, it contains a (small) number of changes to make it work correctly with PyObjC.

<p>You can also download a snapshot of the CVS <a href="/cvs-snapshots">here</a>.

<h2>Misc. other downloads</h2>

<p>
These downloads are not really related to PyObjC, but are available from
this location until they find another home.

<ul>
<li><a href="readline-0.0.0.tar.gz">Readline support for Apple python</a>
<li><a href="pyssl-0.0.0.tar.gz">SSL support for Apple python</a>
<li><a href="dump-methods.py">dump-methods: Script to dump XML-RPC interfaces</a>
</ul>

<?
include "footer.inc";
?>
