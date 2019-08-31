# Generated by Django 2.2.4 on 2019-08-31 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('Swig', 'SWIG'), ('abap', 'ABAP'), ('ada', 'Ada'), ('agda', 'Agda'), ('ahk', 'autohotkey'), ('antlr', 'ANTLR'), ('antlr-as', 'ANTLR With ActionScript Target'), ('antlr-cpp', 'ANTLR With CPP Target'), ('antlr-csharp', 'ANTLR With C# Target'), ('antlr-java', 'ANTLR With Java Target'), ('antlr-objc', 'ANTLR With ObjectiveC Target'), ('antlr-perl', 'ANTLR With Perl Target'), ('antlr-python', 'ANTLR With Python Target'), ('antlr-ruby', 'ANTLR With Ruby Target'), ('apacheconf', 'ApacheConf'), ('applescript', 'AppleScript'), ('as', 'ActionScript'), ('as3', 'ActionScript 3'), ('aspectj', 'AspectJ'), ('aspx-cs', 'aspx-cs'), ('aspx-vb', 'aspx-vb'), ('asy', 'Asymptote'), ('autoit', 'AutoIt'), ('awk', 'Awk'), ('basemake', 'Base Makefile'), ('bash', 'Bash'), ('bat', 'Batchfile'), ('bbcode', 'BBCode'), ('befunge', 'Befunge'), ('blitzbasic', 'BlitzBasic'), ('blitzmax', 'BlitzMax'), ('boo', 'Boo'), ('brainfuck', 'Brainfuck'), ('bro', 'Bro'), ('bugs', 'BUGS'), ('c', 'C'), ('c-objdump', 'c-objdump'), ('ca65', 'ca65'), ('cbmbas', 'CBM BASIC V2'), ('ceylon', 'Ceylon'), ('cfengine3', 'CFEngine3'), ('cfm', 'Coldfusion HTML'), ('cfs', 'cfstatement'), ('cheetah', 'Cheetah'), ('clay', 'Clay'), ('clojure', 'Clojure'), ('cmake', 'CMake'), ('cobol', 'COBOL'), ('cobolfree', 'COBOLFree'), ('coffee-script', 'CoffeeScript'), ('common-lisp', 'Common Lisp'), ('console', 'Bash Session'), ('control', 'Debian Control file'), ('coq', 'Coq'), ('cpp', 'C++'), ('cpp-objdump', 'cpp-objdump'), ('croc', 'Croc'), ('csharp', 'C#'), ('css', 'CSS'), ('css+django', 'CSS+Django/Jinja'), ('css+erb', 'CSS+Ruby'), ('css+genshitext', 'CSS+Genshi Text'), ('css+lasso', 'CSS+Lasso'), ('css+mako', 'CSS+Mako'), ('css+myghty', 'CSS+Myghty'), ('css+php', 'CSS+PHP'), ('css+smarty', 'CSS+Smarty'), ('cuda', 'CUDA'), ('cython', 'Cython'), ('d', 'D'), ('d-objdump', 'd-objdump'), ('dart', 'Dart'), ('delphi', 'Delphi'), ('dg', 'dg'), ('diff', 'Diff'), ('django', 'Django/Jinja'), ('dpatch', 'Darcs Patch'), ('dtd', 'DTD'), ('duel', 'Duel'), ('dylan', 'Dylan'), ('dylan-console', 'Dylan session'), ('dylan-lid', 'DylanLID'), ('ebnf', 'EBNF'), ('ec', 'eC'), ('ecl', 'ECL'), ('elixir', 'Elixir'), ('erb', 'ERB'), ('erl', 'Erlang erl session'), ('erlang', 'Erlang'), ('evoque', 'Evoque'), ('factor', 'Factor'), ('fan', 'Fantom'), ('fancy', 'Fancy'), ('felix', 'Felix'), ('fortran', 'Fortran'), ('fsharp', 'FSharp'), ('gas', 'GAS'), ('genshi', 'Genshi'), ('genshitext', 'Genshi Text'), ('glsl', 'GLSL'), ('gnuplot', 'Gnuplot'), ('go', 'Go'), ('gooddata-cl', 'GoodData-CL'), ('gosu', 'Gosu'), ('groff', 'Groff'), ('groovy', 'Groovy'), ('gst', 'Gosu Template'), ('haml', 'Haml'), ('haskell', 'Haskell'), ('haxeml', 'Hxml'), ('html', 'HTML'), ('html+cheetah', 'HTML+Cheetah'), ('html+django', 'HTML+Django/Jinja'), ('html+evoque', 'HTML+Evoque'), ('html+genshi', 'HTML+Genshi'), ('html+lasso', 'HTML+Lasso'), ('html+mako', 'HTML+Mako'), ('html+myghty', 'HTML+Myghty'), ('html+php', 'HTML+PHP'), ('html+smarty', 'HTML+Smarty'), ('html+velocity', 'HTML+Velocity'), ('http', 'HTTP'), ('hx', 'Haxe'), ('hybris', 'Hybris'), ('idl', 'IDL'), ('iex', 'Elixir iex session'), ('igor', 'Igor'), ('ini', 'INI'), ('io', 'Io'), ('ioke', 'Ioke'), ('irc', 'IRC logs'), ('jade', 'Jade'), ('jags', 'JAGS'), ('java', 'Java'), ('jlcon', 'Julia console'), ('js', 'JavaScript'), ('js+cheetah', 'JavaScript+Cheetah'), ('js+django', 'JavaScript+Django/Jinja'), ('js+erb', 'JavaScript+Ruby'), ('js+genshitext', 'JavaScript+Genshi Text'), ('js+lasso', 'JavaScript+Lasso'), ('js+mako', 'JavaScript+Mako'), ('js+myghty', 'JavaScript+Myghty'), ('js+php', 'JavaScript+PHP'), ('js+smarty', 'JavaScript+Smarty'), ('json', 'JSON'), ('jsp', 'Java Server Page'), ('julia', 'Julia'), ('kconfig', 'Kconfig'), ('koka', 'Koka'), ('kotlin', 'Kotlin'), ('lagda', 'Literate Agda'), ('lasso', 'Lasso'), ('lhs', 'Literate Haskell'), ('lighty', 'Lighttpd configuration file'), ('live-script', 'LiveScript'), ('llvm', 'LLVM'), ('logos', 'Logos'), ('logtalk', 'Logtalk'), ('lua', 'Lua'), ('make', 'Makefile'), ('mako', 'Mako'), ('maql', 'MAQL'), ('mason', 'Mason'), ('matlab', 'Matlab'), ('matlabsession', 'Matlab session'), ('minid', 'MiniD'), ('modelica', 'Modelica'), ('modula2', 'Modula-2'), ('monkey', 'Monkey'), ('moocode', 'MOOCode'), ('moon', 'MoonScript'), ('mscgen', 'Mscgen'), ('mupad', 'MuPAD'), ('mxml', 'MXML'), ('myghty', 'Myghty'), ('mysql', 'MySQL'), ('nasm', 'NASM'), ('nemerle', 'Nemerle'), ('nesc', 'nesC'), ('newlisp', 'NewLisp'), ('newspeak', 'Newspeak'), ('nginx', 'Nginx configuration file'), ('nimrod', 'Nimrod'), ('nsis', 'NSIS'), ('numpy', 'NumPy'), ('objdump', 'objdump'), ('objective-c', 'Objective-C'), ('objective-c++', 'Objective-C++'), ('objective-j', 'Objective-J'), ('ocaml', 'OCaml'), ('octave', 'Octave'), ('ooc', 'Ooc'), ('opa', 'Opa'), ('openedge', 'OpenEdge ABL'), ('perl', 'Perl'), ('perl6', 'Perl6'), ('php', 'PHP'), ('plpgsql', 'PL/pgSQL'), ('postgresql', 'PostgreSQL SQL dialect'), ('postscript', 'PostScript'), ('pot', 'Gettext Catalog'), ('pov', 'POVRay'), ('powershell', 'PowerShell'), ('prolog', 'Prolog'), ('properties', 'Properties'), ('protobuf', 'Protocol Buffer'), ('psql', 'PostgreSQL console (psql)'), ('puppet', 'Puppet'), ('py3tb', 'Python 3.0 Traceback'), ('pycon', 'Python console session'), ('pypylog', 'PyPy Log'), ('pytb', 'Python Traceback'), ('python', 'Python'), ('python3', 'Python 3'), ('qml', 'QML'), ('racket', 'Racket'), ('ragel', 'Ragel'), ('ragel-c', 'Ragel in C Host'), ('ragel-cpp', 'Ragel in CPP Host'), ('ragel-d', 'Ragel in D Host'), ('ragel-em', 'Embedded Ragel'), ('ragel-java', 'Ragel in Java Host'), ('ragel-objc', 'Ragel in Objective C Host'), ('ragel-ruby', 'Ragel in Ruby Host'), ('raw', 'Raw token data'), ('rb', 'Ruby'), ('rbcon', 'Ruby irb session'), ('rconsole', 'RConsole'), ('rd', 'Rd'), ('rebol', 'REBOL'), ('redcode', 'Redcode'), ('registry', 'reg'), ('rexx', 'Rexx'), ('rhtml', 'RHTML'), ('rst', 'reStructuredText'), ('rust', 'Rust'), ('sass', 'Sass'), ('scala', 'Scala'), ('scaml', 'Scaml'), ('scheme', 'Scheme'), ('scilab', 'Scilab'), ('scss', 'SCSS'), ('shell-session', 'Shell Session'), ('smali', 'Smali'), ('smalltalk', 'Smalltalk'), ('smarty', 'Smarty'), ('sml', 'Standard ML'), ('snobol', 'Snobol'), ('sourceslist', 'Debian Sourcelist'), ('sp', 'SourcePawn'), ('spec', 'RPMSpec'), ('splus', 'S'), ('sql', 'SQL'), ('sqlite3', 'sqlite3con'), ('squidconf', 'SquidConf'), ('ssp', 'Scalate Server Page'), ('stan', 'Stan'), ('systemverilog', 'systemverilog'), ('tcl', 'Tcl'), ('tcsh', 'Tcsh'), ('tea', 'Tea'), ('tex', 'TeX'), ('text', 'Text only'), ('trac-wiki', 'MoinMoin/Trac Wiki markup'), ('treetop', 'Treetop'), ('ts', 'TypeScript'), ('urbiscript', 'UrbiScript'), ('vala', 'Vala'), ('vb.net', 'VB.net'), ('velocity', 'Velocity'), ('verilog', 'verilog'), ('vgl', 'VGL'), ('vhdl', 'vhdl'), ('vim', 'VimL'), ('xml', 'XML'), ('xml+cheetah', 'XML+Cheetah'), ('xml+django', 'XML+Django/Jinja'), ('xml+erb', 'XML+Ruby'), ('xml+evoque', 'XML+Evoque'), ('xml+lasso', 'XML+Lasso'), ('xml+mako', 'XML+Mako'), ('xml+myghty', 'XML+Myghty'), ('xml+php', 'XML+PHP'), ('xml+smarty', 'XML+Smarty'), ('xml+velocity', 'XML+Velocity'), ('xquery', 'XQuery'), ('xslt', 'XSLT'), ('xtend', 'Xtend'), ('yaml', 'YAML')], default='python', max_length=100)),
                ('style', models.CharField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful'), ('default', 'default'), ('emacs', 'emacs'), ('friendly', 'friendly'), ('fruity', 'fruity'), ('manni', 'manni'), ('monokai', 'monokai'), ('murphy', 'murphy'), ('native', 'native'), ('pastie', 'pastie'), ('perldoc', 'perldoc'), ('rrt', 'rrt'), ('tango', 'tango'), ('trac', 'trac'), ('vim', 'vim'), ('vs', 'vs')], default='friendly', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
