#!/usr/bin/python

#-------------------------------------------------------------------------------
# Name:         Available Modules
# Purpose:      Use Python to query your web host environment and return a list of all Python modules
#               your web host makes available to you.
#
# Author:       Chris Nielsen
#
# Created:      11/25/2017
# Copyright:    (c) Chris Nielsen 2018
#-------------------------------------------------------------------------------

import os

print "Content-type: text/html\n\n";
print "<html><head>"

css = """
<link rel='stylesheet' id='dashicons-css'  href='http://bluegalaxy.info/codewalk/wp-includes/css/dashicons.min.css?ver=4.8.2' type='text/css' media='all' />
<link rel='stylesheet' id='admin-bar-css'  href='http://bluegalaxy.info/codewalk/wp-includes/css/admin-bar.min.css?ver=4.8.2' type='text/css' media='all' />
<link rel='stylesheet' id='cntctfrm_form_style-css'  href='http://bluegalaxy.info/codewalk/wp-content/plugins/contact-form-plugin/css/form_style.css?ver=4.0.7' type='text/css' media='all' />
<link rel='stylesheet' id='cool-tag-cloud-css'  href='http://bluegalaxy.info/codewalk/wp-content/plugins/cool-tag-cloud/inc/cool-tag-cloud.css?ver=4.8.2' type='text/css' media='all' />
<link rel='stylesheet' id='googlefonts-css'  href='http://fonts.googleapis.com/css?family=Roboto:400|Off:400&subset=latin' type='text/css' media='all' />
<link rel='stylesheet' id='hemingway-rewritten-fonts-css'  href='https://fonts.googleapis.com/css?family=Raleway%3A400%2C300%2C700%7CLato%3A400%2C700%2C400italic%2C700italic&#038;subset=latin%2Clatin-ext' type='text/css' media='all' />
<link rel='stylesheet' id='hemingway-rewritten-style-css'  href='http://bluegalaxy.info/codewalk/wp-content/themes/hemingway-rewritten-wpcom/style.css?ver=4.8.2' type='text/css' media='all' />
<link rel='stylesheet' id='genericons-css'  href='http://bluegalaxy.info/codewalk/wp-content/themes/hemingway-rewritten-wpcom/genericons/genericons.css?ver=4.8.2' type='text/css' media='all' />
<link rel='stylesheet' id='enlighter-local-css'  href='http://bluegalaxy.info/codewalk/wp-content/plugins/enlighter/resources/EnlighterJS.min.css?ver=3.5' type='text/css' media='all' />
<link rel='stylesheet' id='enlighter-external-chris-css'  href='http://bluegalaxy.info/codewalk/wp-content/themes/hemingway-rewritten-wpcom/enlighter/chris.css?ver=aa4c87dc64' type='text/css' media='all' />
<script type='text/javascript' src='http://bluegalaxy.info/codewalk/wp-includes/js/jquery/jquery.js?ver=1.12.4'></script>
<script type='text/javascript' src='http://bluegalaxy.info/codewalk/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1'></script>

<style type='text/css' media='screen'>
	body{ font-family:"Roboto", arial, sans-serif;}
	h1{ font-family:"Roboto", arial, sans-serif;}
	h2{ font-family:"Roboto", arial, sans-serif;}
	h3{ font-family:"Roboto", arial, sans-serif;}
	h4{ font-family:"Roboto", arial, sans-serif;}
	h5{ font-family:"Roboto", arial, sans-serif;}
	h6{ font-family:"Roboto", arial, sans-serif;}
</style>
<!-- fonts delivered by Wordpress Google Fonts, a plugin by Adrian3.com -->		<style type="text/css">.recentcomments a{display:inline !important;padding:0 !important;margin:0 !important;}</style>
		<script type="text/javascript">/* <![CDATA[ */EnlighterJS_EditorConfig = {"languages":{"Generic Highlighting":"generic","CSS (Cascading Style Sheets)":"css","HTML (Hypertext Markup Language)":"html","Java":"java","Javascript":"js","JSON":"json","Markdown":"md","PHP":"php","Python":"python","Ruby":"ruby","Shell Script":"shell","SQL":"sql","XML":"xml","C":"c","C++":"cpp","C#":"csharp","RUST":"rust","LUA":"lua","Matlab":"matlab","NSIS":"nsis","Diff":"diff","VHDL":"vhdl","Avr Assembly":"avrasm","Generic Assembly":"asm","Kotlin":"kotlin","Squirrel":"squirrel","Ini\/Conf Syntax":"ini","RAW Code":"raw","No Highlighting":"no-highlight"},"themes":{"WPCustom":"wpcustom","Enlighter":"enlighter","Godzilla":"godzilla","Beyond":"beyond","Classic":"classic","MooTwo":"mootwo","Eclipse":"eclipse","Droide":"droide","Minimal":"minimal","Atomic":"atomic","Rowhammer":"rowhammer","Git":"git","Mocha":"mocha","MooTools":"mootools","Panic":"panic","Tutti":"tutti","Twilight":"twilight","chris\/ext":"chris"},"config":{"theme":"enlighter","language":"python","linenumbers":true,"indent":-1,"tabIndentation":false,"quicktagMode":"html","languageShortcode":true}};/* ]]> */</script>	<style type="text/css">
			.site-title a,
		.site-description {
			color: #ffffff;
		}
				.site-header-image {
			background-image: url(http://bluegalaxy.info/codewalk/wp-content/uploads/2017/07/geom4.jpg);
		}
		</style>
	<style type="text/css" media="print">#wpadminbar { display:none; }</style>
<style type="text/css" media="screen">
	html { margin-top: 32px !important; }
	* html body { margin-top: 32px !important; }
	@media screen and ( max-width: 782px ) {
		html { margin-top: 46px !important; }
		* html body { margin-top: 46px !important; }
	}
</style>
"""
print css

print "</head><body bgcolor='#ffffff'>"

print "\n<b>Available Modules:</b><BR><BR>"

# List all installed packages
print '<ul>'
dist_list = []
for dist in __import__('pkg_resources').working_set:
    dist_list.append(dist.project_name.replace('Python', '').strip())

dist_list = list(filter(None, dist_list))
for dist in dist_list:
    print "\n<li>", dist, '</li>'
print '</ul>'

print "</body></html>"


